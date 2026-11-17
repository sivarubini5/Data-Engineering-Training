docker run -d -p 8080:8080 --name airflow apache/airflow standalone
docker ps 
docker logs airflow
docker exec -it airflow bash
cd /opt/airflow/dags

cat > factory_quality_dag.py <<'EOF'
import csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
def load_batches():
    with open("/opt/airflow/dags/factory_batches.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    print("Batches loaded:", len(rows))
    return rows
def check_quality(ti):
    batches = ti.xcom_pull(task_ids="load_batches")
    review_batches = []
    for batch in batches:
        units = int(batch["units_produced"])
        defective = int(batch["defective_units"])
        defect_percentage = (defective / units) * 100
        if defect_percentage > 5:
            review_batches.append(batch["batch_id"])
    print("Batches requiring quality review:", review_batches)
    return review_batches
def calculate_value(ti):
    batches = ti.xcom_pull(task_ids="load_batches")
    total_value = 0
    for batch in batches:
        units = int(batch["units_produced"])
        value = int(batch["value_per_unit"])
        total_value += units * value
    print("Total production value:", total_value)
    return total_value
def generate_report(ti):
    batches = ti.xcom_pull(task_ids="load_batches")
    review_batches = ti.xcom_pull(task_ids="check_quality")
    total_value = ti.xcom_pull(task_ids="calculate_value")
    print("========== MANUFACTURING QUALITY REPORT ==========")
    print("Total number of batches:", len(batches))
    print("Batches requiring quality review:", review_batches)
    print("Total production value: Rs.", total_value)
    print("==================================================")
with DAG(
    dag_id="factory_quality_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    load_task = PythonOperator(
        task_id="load_batches",
        python_callable=load_batches
    )
    quality_task = PythonOperator(
        task_id="check_quality",
        python_callable=check_quality
    )
    value_task = PythonOperator(
        task_id="calculate_value",
        python_callable=calculate_value
    )
    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )
    load_task >> [quality_task, value_task] >> report_task
EOF

cat > factory_batches.csv <<'EOF'
batch_id,units_produced,defective_units,value_per_unit
B501,100,2,350
B502,80,7,420
B503,120,4,300
B504,60,0,550
B505,90,6,400
EOF

ls -l

python -m py_compile factory_quality_dag.py

airflow dags list



