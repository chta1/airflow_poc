from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import logging

from datetime import datetime


def my_func():
    logging.info('****** Starting to exec my_func')
    print('Hello from my_func')
    logging.info('****** End of exec my_func')


with DAG('on_demand_dag', description='On Demand DAG', schedule_interval=None, start_date=datetime(2020, 5, 28),
         catchup=False) as dag:
    #dummy_task = DummyOperator(task_id='dummy_task', retries=3)
    python_task = PythonOperator(task_id='python_task', python_callable=my_func)

    #dummy_task >> python_task
    python_task
