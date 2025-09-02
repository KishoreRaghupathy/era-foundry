from __future__ import annotations
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from pipelines.pcaf_calculator import load_raw, write_silver, compute_financed_emissions

default_args = {"owner": "era-foundry", "depends_on_past": False, "retries": 0}

with DAG(
    dag_id="pcaf_ingestion_compute",
    default_args=default_args,
    start_date=datetime(2025, 9, 1),
    schedule_interval=None,
    catchup=False,
    tags=["pcaf","day02"],
) as dag:

    def _extract():
        exposures, emissions, valuations = load_raw()
        return {"exposures_rows": len(exposures), "emissions_rows": len(emissions), "valuations_rows": len(valuations)}

    def _transform():
        exposures, emissions, valuations = load_raw()
        write_silver(exposures, emissions, valuations)

    def _compute():
        compute_financed_emissions()

    extract = PythonOperator(task_id="extract_raw", python_callable=_extract)
    transform = PythonOperator(task_id="transform_to_silver", python_callable=_transform)
    compute = PythonOperator(task_id="pcaf_compute_gold", python_callable=_compute)

    extract >> transform >> compute
