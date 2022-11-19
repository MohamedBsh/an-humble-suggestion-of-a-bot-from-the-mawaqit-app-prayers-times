export AIRFLOW_HOME=$(pwd)/airflow
export PYTHONPATH=$(pwd)

python3 -m pipenv install -r requirements.txt
python3 -m pipenv shell