from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='tutorial_dag',
    start_date=datetime(2023, 1, 1),
    schedule='@daily',  # ✅ Correct new param name
    catchup=False,
    tags=["example"]
) as dag:
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    start >> end