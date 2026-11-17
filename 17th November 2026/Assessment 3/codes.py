docker run -d -p 8080:8080 --name airflow apache/airflow standalone
docker ps 
docker logs airflow
docker exec -it airflow bash
cd /opt/airflow/dags

cat > airport_baggage.csv <<'EOF'
bag_id,flight_no,weight_kg,screening_status
BG101,AI502,18,Clear
BG102,AI502,27,Clear
BG103,6E214,12,Review
BG104,6E214,22,Clear
BG105,UK812,25,Review
BG106,UK812,15,Clear
EOF

cat airport_baggage.csv
  bag_id,flight_no,weight_kg,screening_status
  BG101,AI502,18,Clear
  BG102,AI502,27,Clear
  BG103,6E214,12,Review
  BG104,6E214,22,Clear
  BG105,UK812,25,Review
  BG106,UK812,15,Clear
wc -l airport_baggage.csv
  7 airport_baggage.csv

cat > airport_baggage_dag.py <<'EOF'
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv
def load_baggage():
    with open('/opt/airflow/dags/airport_baggage.csv', newline='') as file:
        records = list(csv.DictReader(file))
    print('Baggage records loaded:', len(records))
    return records
def identify_review_bags(**context):
    records = context['ti'].xcom_pull(task_ids='load_baggage')
    review_bags = []
    for bag in records:
        weight = int(bag['weight_kg'])
        if bag['screening_status'] == 'Review' or weight > 23:
            review_bags.append(bag['bag_id'])
    print('Bags requiring manual review:', review_bags)
    return review_bags
def calculate_total_weight(**context):
    records = context['ti'].xcom_pull(task_ids='load_baggage')
    total_weight = 0
    for bag in records:
        total_weight += int(bag['weight_kg'])
    print('Total baggage weight:', total_weight, 'kg')
    return total_weight
def generate_report(**context):
    ti = context['ti']
    records = ti.xcom_pull(task_ids='load_baggage')
    review_bags = ti.xcom_pull(task_ids='identify_review_bags')
    total_weight = ti.xcom_pull(task_ids='calculate_total_weight')
    print('========== AIRPORT BAGGAGE SCREENING REPORT ==========')
    print('Total number of bags:', len(records))
    print('Bags requiring manual review:', review_bags)
    print('Number of bags requiring review:', len(review_bags))
    print('Total baggage weight:', total_weight, 'kg')
    print('======================================================')
with DAG(
    dag_id='airport_baggage_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    load_task = PythonOperator(
        task_id='load_baggage',
        python_callable=load_baggage
    )
    review_task = PythonOperator(
        task_id='identify_review_bags',
        python_callable=identify_review_bags
    )
    weight_task = PythonOperator(
        task_id='calculate_total_weight',
        python_callable=calculate_total_weight
    )
    report_task = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )
    load_task >> [review_task, weight_task] >> report_task
EOF

python -m py_compile airport_baggage_dag.py
airflow dags list
