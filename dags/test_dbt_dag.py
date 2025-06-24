from verify_airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG('test_dbt_dag',
         schedule_interval=None,
         catchup=False,
         default_args=default_args,
         tags=['example']) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /workspaces/itm327-codespaces-starter/dbt && dbt run'
    )
