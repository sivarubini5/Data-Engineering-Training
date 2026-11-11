# Databricks notebook source
# THEME PARK OPERATIONS - DATASET SETUP
# Upload the five data files to the same Unity Catalog Volume folder first.
# Change BASE_PATH, CATALOG, and SCHEMA below to match your workspace.
# WARNING: Rerunning this notebook overwrites the initial training tables.
# Do NOT rerun it after starting the streaming pipeline.

# COMMAND ----------
from pyspark.sql.types import (StructType, StructField, StringType, IntegerType, DoubleType)

CATALOG = "main"      # Change to your catalog
SCHEMA = "default"    # Change to your schema
BASE_PATH = "/Volumes/main/default/training_files/themepark_assessment"  # Change to your folder

prefix = f"{CATALOG}.{SCHEMA}"

entry_schema = StructType([
    StructField("entry_id", IntegerType(), True),
    StructField("visitor_id", StringType(), True),
    StructField("attraction_id", StringType(), True),
    StructField("visit_date", StringType(), True),
    StructField("entry_time", StringType(), True),
    StructField("wait_minutes", IntegerType(), True),
    StructField("ride_minutes", IntegerType(), True),
    StructField("ticket_type", StringType(), True),
    StructField("ticket_price", DoubleType(), True),
    StructField("status", StringType(), True),
    StructField("booking_channel", StringType(), True)
])

maintenance_schema = StructType([
    StructField("maintenance_id", StringType(), True),
    StructField("attraction_id", StringType(), True),
    StructField("maintenance_date", StringType(), True),
    StructField("issue_type", StringType(), True),
    StructField("downtime_minutes", IntegerType(), True),
    StructField("maintenance_status", StringType(), True)
])

# COMMAND ----------
def read_csv(filename, schema):
    return (spark.read.format("csv")
            .option("header", "true")
            .schema(schema)
            .load(f"{BASE_PATH}/{filename}"))

entries = read_csv("park_entries.csv", entry_schema)
attractions = spark.read.json(f"{BASE_PATH}/attractions.json")
maintenance = read_csv("attraction_maintenance.csv", maintenance_schema)
changes = read_csv("park_entry_changes.csv", entry_schema)

# COMMAND ----------
# Source table is append-only for later streaming exercises.
entries.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{prefix}.tp_entries_raw")
attractions.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{prefix}.tp_attractions")
maintenance.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{prefix}.tp_maintenance")
changes.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{prefix}.tp_entry_changes")

# COMMAND ----------
# Inspect the tables. Keep this source unchanged until incremental loading.
for name in ["tp_entries_raw", "tp_attractions", "tp_maintenance", "tp_entry_changes"]:
    print(f"{prefix}.{name}: {spark.table(f'{prefix}.{name}').count()} rows")

display(spark.table(f"{prefix}.tp_entries_raw").limit(10))

# COMMAND ----------
# LATER, after your streaming pipeline has been created and run once:
# Read park_entries_incremental.csv with entry_schema and append it to
# tp_entries_raw. This is intentionally left for the participant to implement.
