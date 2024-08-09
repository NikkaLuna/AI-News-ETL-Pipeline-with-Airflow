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

## Demonstration with Fictionalized Data

To provide a clear demonstration of the ETL pipeline's functionality, the images below showcase how the pipeline processes and transforms fictionalized and masked news data. This demonstrates data masking techniques, ensuring that sensitive information is protected during data processing.


![JSON Structure for Article](https://github.com/NikkaLuna/AI-News-ETL-Pipeline-with-Airflow/blob/main/JSON%20Structure%20for%20Article.png)

*This image shows the raw JSON data extracted from the News API, specifically representing a news article. This will extract attributes like the article's source, author, title, URL, publication date, and content.*


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

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/News-ETL-Pipeline-with-Python-and-SQLite.git
    cd News-ETL-Pipeline-with-Python-and-SQLite
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python3 -m venv airflow_env
    source airflow_env/bin/activate
    pip install -r requirements.txt
    ```

3. **Install the required Python packages:
    ```bash
    pip install -r requirements.txt

4. **Set Up Apache Airflow**:
    Follow the instructions to install and configure Apache Airflow in your environment.

5. **Configure API Key**:
    Add your News API key in the `Ed_news_1.py` file.

6. **Run the ETL Pipeline**:
    - Start the Airflow web server and scheduler:
      ```bash
      airflow standalone
      ```
    - Open the Airflow UI, trigger the `news_etl` DAG, and monitor the ETL process.

## Usage

Once the pipeline is running, it will automatically extract, transform, and load the latest news articles related to AI into the SQLite database daily. You can query the SQLite database to analyze the data further.

## Environment Setup

This repository does not include the full Airflow environment due to size constraints. However, you can easily recreate the environment by following the instructions above to install the required Python packages and configure Apache Airflow.

## Contributions

Feel free to fork this repository and submit pull requests if you have any improvements or new features to suggest.
