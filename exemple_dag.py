import sys
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importer les fonctions
from extract_1 import extract_1
from extract_2 import extract_2
from extract_3 import extract_3
from transform import transform_data
from load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

# Define the tasks
extract_1_task = PythonOperator(
    task_id='extract_1',
    python_callable=extract_1,
    dag=dag,
)

extract_2_task = PythonOperator(
    task_id='extract_2',
    python_callable=extract_2,
    dag=dag,
)

extract_3_task = PythonOperator(
    task_id='extract_3',
    python_callable=extract_3,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

# Set the task dependencies
[extract_1_task, extract_2_task, extract_3_task] >> transform_task >> load_task
