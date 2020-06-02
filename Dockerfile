FROM puckel/docker-airflow:latest

RUN pip install --user psycopg2-binary
RUN pip install docker==4.1.0
RUN pip install kubernetes

ENV AIRFLOW_HOME=/usr/local/airflow

#### Build so and header files.  copy to /usr/local/airflow/
#USER root
#RUN apt-get update
#RUN apt-get install golang 1.13 -y
#WORKDIR /build
#COPY . .
#RUN env CGO_ENABLED=1 go build -v -o send_remind.so  -buildmode=c-shared .

COPY ./config/airflow.cfg /usr/local/airflow/airflow.cfg
#COPY ./include/.kube/config /usr/local/airflow/include/.kube/config
