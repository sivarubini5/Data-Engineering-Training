# Databricks notebook source
# Azure Databricks Assessment - City Water Network Monitoring
# SETUP ONLY: this notebook creates tables, not exercise solutions.
# Upload the five data files into the Unity Catalog Volume folder before running.

# COMMAND ----------

import re
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, DoubleType, TimestampType
)

dbutils.widgets.text("catalog", "rithika_databricks")
dbutils.widgets.text("schema", "default")
dbutils.widgets.text("volume", "assessment_files")
dbutils.widgets.text("folder", "water_network")

catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
volume = dbutils.widgets.get("volume").strip()
folder = dbutils.widgets.get("folder").strip().strip("/")

for label, value in [("catalog", catalog), ("schema", schema), ("volume", volume)]:
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value):
        raise ValueError(f"Invalid {label}: use letters, digits and underscores only")
if not re.fullmatch(r"[A-Za-z0-9_/-]+", folder) or ".." in folder:
    raise ValueError("Invalid folder name")

namespace = f"`{catalog}`.`{schema}`"
base_path = f"/Volumes/{catalog}/{schema}/{volume}/{folder}"
print("Data location:", base_path)

required = [
    "water_meter_readings.csv", "water_zones.json", "water_service_requests.csv",
    "water_reading_changes.csv", "water_readings_incremental.csv"
]
try:
    available = {entry.name.rstrip("/") for entry in dbutils.fs.ls(base_path)}
except Exception as exc:
    raise RuntimeError(f"Cannot access {base_path}. Create the Volume and upload the files first.") from exc
missing = sorted(set(required) - available)
if missing:
    raise FileNotFoundError(f"Missing data files in {base_path}: {missing}")

spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"USE SCHEMA `{schema}`")

def save_delta(df, name):
    (df.write.format("delta")
       .mode("overwrite")
       .option("overwriteSchema", "true")
       .saveAsTable(f"{catalog}.{schema}.{name}"))

# COMMAND ----------

reading_schema = StructType([
    StructField("reading_id", IntegerType(), True),
    StructField("meter_id", StringType(), True),
    StructField("zone_id", StringType(), True),
    StructField("reading_time", TimestampType(), True),
    StructField("flow_lpm", DoubleType(), True),
    StructField("pressure_bar", DoubleType(), True),
    StructField("chlorine_mg_l", DoubleType(), True),
    StructField("consumption_liters", IntegerType(), True),
    StructField("reading_status", StringType(), True),
    StructField("source_system", StringType(), True),
])

def read_readings(filename):
    return (spark.read.format("csv")
        .option("header", "true")
        .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")
        .schema(reading_schema)
        .load(f"{base_path}/{filename}"))

source = read_readings("water_meter_readings.csv")
save_delta(source, "water_meter_readings_source")
save_delta(source, "water_meter_readings_work")
save_delta(read_readings("water_reading_changes.csv"), "water_reading_changes")
save_delta(read_readings("water_readings_incremental.csv"), "water_readings_incremental_staging")

# COMMAND ----------

zone_raw = spark.read.json(f"{base_path}/water_zones.json")
save_delta(zone_raw, "water_zones_raw")
zone_flat = zone_raw.select(
    "zone_id", "zone_name",
    F.col("location.city").alias("city"),
    F.col("location.district").alias("district"),
    "zone_type", "daily_capacity_liters", "active", "commissioned_on"
)
save_delta(zone_flat, "water_zones")

# COMMAND ----------

request_schema = StructType([
    StructField("request_id", IntegerType(), True),
    StructField("meter_id", StringType(), True),
    StructField("zone_id", StringType(), True),
    StructField("reported_at", TimestampType(), True),
    StructField("issue_type", StringType(), True),
    StructField("priority", StringType(), True),
    StructField("estimated_cost", DoubleType(), True),
    StructField("work_status", StringType(), True),
])
requests = (spark.read.option("header", "true")
    .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")
    .schema(request_schema)
    .csv(f"{base_path}/water_service_requests.csv"))
save_delta(requests, "water_service_requests")

# COMMAND ----------

for name in [
    "water_meter_readings_source", "water_meter_readings_work",
    "water_zones_raw", "water_zones", "water_service_requests",
    "water_reading_changes", "water_readings_incremental_staging"
]:
    print(f"{catalog}.{schema}.{name}: {spark.table(f'{catalog}.{schema}.{name}').count()} rows")
print("SETUP COMPLETE. Do not rerun after beginning exercises or pipeline ingestion.")
