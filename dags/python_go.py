import ctypes
from ctypes import *
import ctypes as c

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import logging
from airflow.models import Variable

from datetime import datetime

# lib = cdll.LoadLibrary("send_remind.so.bk")
# r = lib.Add(10, 30)

lib = cdll.LoadLibrary(r'/usr/local/airflow/dags/send_remind.so')
#lib = cdll.LoadLibrary(r'/Users/chung.ta/dev/workspace/test/airflow_poc/send_remind.so')

class GoString(c.Structure):
    _fields_ = [("p", c.c_char_p), ("n", c.c_longlong)]

# lib.SendRemind.argtypes = [GoString]
# text = b"PYTHON MESSAGE"
# gs = GoString(text, len(text))
# result = c.c_char_p(lib.SendRemind(gs))


settings = Variable.get("settings", deserialize_json=True)

# And be able to access the values like in a dictionary
print("*** Login : {}".format(settings['login']))
print("**** Role : {}".format(settings['config']['role']))

#print("**** MY_TEST_ENV : {}".format(Variable.get("MY_TEST_ENV")))


with DAG('calling_go_from_python_dag', description='Call Golang Func from Python DAG', schedule_interval=None, start_date=datetime(2020, 5, 28),
         catchup=False) as dag:

    def calling_SendRemind():
        logging.info('****** Starting to exec calling_SendRemind')

        lib.SendRemind.argtypes = [GoString]
        text = b"PYTHON MESSAGE"
        gs = GoString(text, len(text))
        result = c.c_char_p(lib.SendRemind(gs))

        print('**** >>> calling_add_from_go: SendRemind({0})'.format(text, result))
        logging.info('****** End of exec calling_SendRemind')

    def calling_add_from_go():
        logging.info('****** Starting to exec calling_add_from_go')
        print('calling_add_from_go: Add({0}, {1} is {2})'.format(10, 35, lib.Add(10, 35)))
        logging.info('****** End of exec calling_add_from_go')
        return lib.Add(10, 35)


    go_task_1 = PythonOperator(task_id='calling_add_from_go', python_callable=calling_add_from_go)
    go_task_2 = PythonOperator(task_id='calling_calling_SendRemind', python_callable=calling_SendRemind)

    go_task_1 >> go_task_2
