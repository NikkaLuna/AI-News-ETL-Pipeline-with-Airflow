# AI News ETL Pipeline Using Python and SQLite

## Overview

This project demonstrates the creation of an ETL (Extract, Transform, Load) data pipeline using Python, SQLite, and Apache Airflow. The purpose of this pipeline is to extract news data from the News API, transform the data for better usability, and load it into an SQLite database. Apache Airflow is used to automate and orchestrate the entire ETL process, making it possible to run the pipeline daily without manual intervention.

## Project Objectives

- **Create an ETL Pipeline**: Develop a pipeline that extracts news articles from the News API, transforms the data, and loads it into an SQLite database.
- **Data Extraction**: Use Python's `requests` library to pull news articles related to AI from the News API.
- **Data Transformation**: Clean and format the extracted data, ensuring it's in a structured format suitable for loading into the database.
- **Data Loading**: Load the transformed data into an SQLite database.
- **Automation**: Utilize Apache Airflow to automate the ETL process, ensuring that the pipeline runs daily.

## Skills and Technologies

- **Data Pipeline Engineering**
- **Data Extraction**
- **Data Manipulation**
- **Data Cleaning**
- **Data Loading**
- **Apache Airflow for Automation**
- **SQLite Database Management**
- **Python Programming**

## Project Structure

- **`ETL.ipynb`**: Jupyter notebook containing the step-by-step process of creating the ETL pipeline, including data extraction, transformation, and loading.
- **`dags/Ed_news_1.py`**: Python script used in Apache Airflow to automate the ETL pipeline.
- **`.vscode/`**: Configuration files for the VS Code development environment.

## Project Details

### 1. Data Extraction

The pipeline begins by extracting news articles related to AI using the News API. The extracted data includes attributes like the article's source, author, title, URL, publication date, and content.

### 2. Data Transformation

The transformation process includes cleaning the data and structuring it into a format suitable for loading into a database. Specific tasks include:

- Formatting dates
- Cleaning author names
- Extracting relevant fields from the raw data

### 3. Data Loading

The cleaned and structured data is loaded into an SQLite database. The database schema includes fields such as the source, author name, news title, URL, publication date, and content.

## Demonstration with Data

To provide a clear demonstration of the ETL pipeline's functionality, the images below showcase how the pipeline processes and transforms news data.


![JSON Structure for Article](https://github.com/NikkaLuna/AI-News-ETL-Pipeline-with-Airflow/blob/main/JSON%20Structure%20for%20Article.png)

*This image shows the raw JSON data extracted from the News API, specifically representing a news article. This will extract attributes like the article's source, author, title, URL, publication date, and content.*<br><br>


![Tabular Representation of Data](https://github.com/NikkaLuna/AI-News-ETL-Pipeline-with-Airflow/blob/main/Tabular%20Representation%20of%20Data.png)

*This image displays the transformed data in a tabular format after it has been structured for loading into the SQLite database, formatting the dates, cleaning author names, and extracting relevant fields from the raw data.*

### 4. Automation with Apache Airflow

Apache Airflow is used to schedule and run the ETL pipeline daily. The pipeline is defined as a Directed Acyclic Graph (DAG) in Airflow, and tasks are managed using Python operators. Airflow handles task dependencies and ensures that the data is extracted, transformed, and loaded in the correct order.

## Installation and Setup

### Prerequisites

- Python 3.x
- SQLite
- Apache Airflow
- News API Key
- Jupyter Notebook

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/News-ETL-Pipeline-with-Python-and-SQLite.git
    cd News-ETL-Pipeline-with-Python-and-SQLite
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python3 -m venv airflow_env
    source airflow_env/bin/activate  # On macOS and Linux
    airflow_env\Scripts\activate.bat  # On Windows
    pip install -r requirements.txt
    ```

3. **Set Up Apache Airflow**:
    - Follow the official Apache Airflow installation guide to install and configure Apache Airflow in your environment.
    - Ensure you have version 2.0 or above.

4. **Configure API Key**:
    - Open the dags/Ed_news_1.py file.
    - Replace "your_api_key_here" with your actual News API key.

5. **Run the ETL Pipeline**:
    - Start the Airflow web server and scheduler:
      ```bash
      airflow standalone
      ```
    - Open the Airflow UI, trigger the `news_etl` DAG, and monitor the ETL process.
    
## Jupyter Notebook

This project includes a Jupyter Notebook (ETL.ipynb) that demonstrates the full implementation of the ETL pipeline. The notebook is used to extract, transform, and load AI-related news articles from the News API into an SQLite database. You can run this notebook locally using Jupyter or any compatible environment.  Be sure to activate the virtual environment before running the notebook.

### Prerequisites:

Ensure you have Jupyter Notebook installed. You can install it using pip:
    ```
    pip install notebook
    ```

Running the Notebook:

1. Navigate to the project directory.
2. Activate your virtual environment (see Installation and Setup section).

4. Start the Jupyter Notebook server:
    ```bash
    jupyter notebook
    ```

5. Open ETL.ipynb in your browser and follow along with the code cells.

## Usage

Once the pipeline is running, it will automatically extract, transform, and load the latest news articles related to AI into the SQLite database daily. You can query the SQLite database to analyze the data further.

### Example Query

To help you get started with querying the SQLite database, here is a simple example:

**Fetch All Articles Published on a Specific Date:**

```sql
SELECT title, author, publication_date
FROM news_articles
WHERE publication_date = '2024-08-01';
```

*This query retrieves the title, author, and publication date of all news articles published on August 1, 2024.*

Fetch Articles by a Specific Author:

```sql
SELECT title, url, publication_date
FROM news_articles
WHERE author = 'John Doe';
```
*This query returns the title, URL, and publication date of all news articles written by the author "John Doe.*

Fetch the Latest 10 Articles:

```sql
SELECT title, author, publication_date
FROM news_articles
ORDER BY publication_date DESC
LIMIT 10;
```
*This query lists the most recent 10 news articles in the database, ordered by their publication date.*

## Environment Setup

This repository does not include the full Airflow environment due to size constraints. However, you can easily recreate the environment by following the instructions above to install the required Python packages and configure Apache Airflow.

## Contributions

Feel free to fork this repository and submit pull requests with improvements or new features. If you encounter any issues, please open an issue on the repository.
