import datetime
from airflow import DAG
from airflow.models.param import Param
from airflow.operators.python import PythonOperator
from app.extract_salat_times import main

default_args = {
    "owner": "my_organization",
    "depends_on_past": False,
    "start_date": datetime.date(2022, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=1),
}

with DAG(
        dag_id="main_salat_times_pipeline",
        start_date=datetime.datetime(2022, 1, 1),
        schedule_interval=None,
        catchup=False,
        params={
            'year': Param(2022, type='integer'),
        }
) as dag:
    def get_year() -> int:
        return '{{ params.year }}'


    ingest = PythonOperator(task_id="main_salat_times", op_args=[get_year()], python_callable=main, )

    ingest
