import requests
import datetime
import pandas as pd
import logging
import re
import sqlite3
import redis
import time

import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from newsapi import NewsApiClient
from datetime import datetime, timedelta, time

news_api = NewsApiClient(api_key='your_api_key')

# Initialize Redis client for caching
cache = redis.Redis(host='localhost', port=6379, db=0)

to_date = datetime.utcnow().date()
from_date = to_date - timedelta(days=1)

dag = DAG(
    dag_id="ed_1",
    default_args={'start_date': datetime.combine(from_date, time(0, 0)), 'retries': 1},
    schedule_interval='@daily', 
)

def fetch_news_with_rate_limiting(query):
    request_count = 0
    max_requests = 100  
    start_time = time.time()

    # Attempt to fetch data from cache
    cached_data = cache.get(query)
    if cached_data:
        logging.info("Serving data from cache")
        return cached_data
    else:
        while request_count < max_requests:
            try:
                # Make API request
                result = news_api.get_everything(q=query, language="en", from_param=from_date, to=to_date)
                
                # Cache the result
                cache.set(query, result["articles"], ex=3600)  # Cache for 1 hour
                
                logging.info("Data fetched and cached successfully.")
                return result["articles"]

            except Exception as e:
                logging.error(f"Error fetching data: {e}")
                time.sleep(1)  # Add delay to handle rate limiting
                request_count += 1
            
            # Check if the rate limit period has passed
            if (time.time() - start_time) >= 3600:  # Reset every hour
                request_count = 0
                start_time = time.time()

def extract_news_data(**kwargs):
    articles = fetch_news_with_rate_limiting("AI")
    if articles:
        kwargs['task_instance'].xcom_push(key='extract_result', value=articles)
    else:
        logging.error("Failed to fetch or cache news data.")
    
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
        cursor = connection.cursor()
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
    task_id="get_news",
    python_callable=extract_news_data,
    provide_context=True,
    dag=dag
)

_transform_news_data = PythonOperator(
    task_id="transform_news",
    python_callable=transform_news_data,
    dag=dag
)

_load_news_data = PythonOperator(
    task_id="load_news",
    python_callable=load_news_data,
    dag=dag
)

_extract_news_data >> _transform_news_data >> _load_news_data
