import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from app.salat_times_ingestion import main
from airflow.operators.bash import BashOperator
from airflow.models import Variable

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
            'year': 2022,
        }
) as dag:

    ingest = PythonOperator(task_id="main_salat_times", python_callable=main, op_args=("{{params.year}}",))
    load_to_db = BashOperator(
        task_id='export_data_to_db',
        bash_command='pipenv run python3 app/salat_times_to_db.py '
                     '--connection %s' % Variable.get("dev_connection")
    )

    ingest >> load_to_db
