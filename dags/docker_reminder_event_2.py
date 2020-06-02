from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.docker_operator import DockerOperator
import logging
#from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator


logger = logging.getLogger("airflow.task")


default_args = {
    'owner': 'airflow',
    'description': 'Use of the DockerOperator',
    'depend_on_past': False,
    'start_date': datetime(2018, 1, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('reminder_event_2_dag', default_args=default_args, schedule_interval="*/8 * * * *", catchup=False) as dag:

    t2 = DockerOperator(
        task_id='reminder_event_2',
        image='my-atlas-loans-reminder:1.3',
        command='./another-entry',
        volumes=['/var/run/docker.sock:/var/run/docker.sock'],
        tty=True,
        xcom_push=True,
        xcom_all=True,

    )

    t3 = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world event 2"'
    )

    t2 >> t3