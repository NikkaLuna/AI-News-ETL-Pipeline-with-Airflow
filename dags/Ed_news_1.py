import requests
import datetime
import pandas as pd
import logging
import re
import sqlite3

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from newsapi import NewsApiClient
from datetime import datetime, timedelta, time

news_api = NewsApiClient(api_key='51bacf5bf7c04714890cf45a70c0aa15')
to_date = datetime.utcnow().date()
from_date  = to_date - timedelta(days=1)

dag = DAG(
    dag_id="ed_1",
    default_args={'start_date': datetime.combine(from_date, time(0, 0)), 'retries': 1},
    schedule_interval='@daily',  # Updated schedule_interval to run every daily
)

def extract_news_data(**kwargs):
    try: 
        result = news_api.get_everything(q="AI", language="en", from_param=from_date, to=to_date)
        logging.info("Connection is successful.")
        kwargs['task_instance'].xcom_push(key='extract_result', value=result["articles"])
    except:
        logging.error("Connection is unsuccessful.")
    
    

def clean_author_column(text):    
    try:
        return text.split(",")[0].title()
    except AttributeError:
        return "No Author"

def transform_news_data(**kwargs):
    article_list = []
    data = kwargs['task_instance'].xcom_pull(task_ids='get_news', key='extract_result')
    for i in data:
        article_list.append([value.get("name", 0) if key == "source" else value for key, value in i.items() 
                          if key in ["author", "title", "publishedAt", "content", "url", "source"]])

    df = pd.DataFrame(article_list, columns=["Source", "Author Name", "News Title", "URL", "Date Published", "Content"])

    df["Date Published"] = pd.to_datetime(df["Date Published"]).dt.strftime('%Y-%m-%d %H:%M:%S')

    df["Author Name"] = df["Author Name"].apply(clean_author_column)
    
    kwargs['task_instance'].xcom_push(key='transform_df', value=df.to_json())

def load_news_data(**kwargs):
    with sqlite3.connect("news_data.sqlite") as connection:
        # Creating a cursor within the context manager
        cursor = connection.cursor()
        # Example: Creating a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news_table (
                "Source" VARCHAR(30),
                "Author Name" TEXT,
                "News Title" TEXT,
                "URL" TEXT,
                "Date Published" TEXT,
                "Content" TEXT
            )
        ''')
        data = kwargs['task_instance'].xcom_pull(task_ids='transform_news', key='transform_df')

        data.to_sql(name="news_table", con=connection, index=False, if_exists="append")

_extract_news_data = PythonOperator(
    task_id = "get_news",
    python_callable = extract_news_data,
    provide_context=True,
    dag = dag
)

_transform_news_data = PythonOperator(
    task_id = "transform_news",
    python_callable = transform_news_data,
    dag = dag
)

_load_news_data = PythonOperator(
    task_id = "load_news",
    python_callable = load_news_data,
    dag = dag

)

_extract_news_data >> _transform_news_data >> _load_news_data
    