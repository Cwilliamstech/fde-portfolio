from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="invoice_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="cd /Users/conner/fde/stage3 && /Users/conner/fde/stage3/.venv/bin/python extract.py",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /Users/conner/fde/stage3/invoice_dbt && /Users/conner/fde/stage3/.venv-dbt/bin/dbt run && /Users/conner/fde/stage3/.venv-dbt/bin/dbt test",
    )

    extract >> dbt_run