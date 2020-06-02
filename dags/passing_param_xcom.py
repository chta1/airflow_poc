
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import logging

from datetime import datetime

with DAG('passing_param_with_xcom_dag', description='Passing Param With XCOM DAG', schedule_interval=None, start_date=datetime(2020, 5, 28),
         catchup=False) as dag:
    def push_function(**context):
        msg='This is my message'
        print("message to push: '%s'" % msg)
        task_instance = context['task_instance']
        task_instance.xcom_push(key="the_message", value=msg)

    push_task = PythonOperator(task_id='push_task', python_callable=push_function, provide_context=True)

    def pull_function(**kwargs):
        ti = kwargs['ti']
        msg = ti.xcom_pull(task_ids='push_task',key='the_message')
        print("received message: '%s'" % msg)

    pull_task = PythonOperator(task_id='pull_task', python_callable=pull_function, provide_context=True)

    push_task >> pull_task