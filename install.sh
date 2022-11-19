export AIRFLOW_HOME=$(pwd)/airflow
export PYTHONPATH=$(pwd)

pip install 'apache-airflow[postgres]'
python3 -m pipenv install -r requirements.txt
python3 -m pipenv shell