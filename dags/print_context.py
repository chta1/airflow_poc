import os

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


from datetime import datetime

with DAG('print_context_dag', description='Print Context DAG', schedule_interval=None, start_date=datetime(2020, 5, 28),
         catchup=False) as dag:
    def print_context(**context):
        print(context)


    print_context = PythonOperator(task_id="print_context", python_callable=print_context, provide_context=True)


    def print_env_var():
        print(os.environ['AIRFLOW__MY_ENV'])


    print_env_var = PythonOperator(task_id="print_env_var", python_callable=print_env_var)

    print_context >> print_env_var
