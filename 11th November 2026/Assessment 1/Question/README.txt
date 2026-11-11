AZURE DATABRICKS - THEME PARK OPERATIONS ASSESSMENT

CONTENTS
- theme_park_databricks_assessment.pdf  : participant handout, 50 exercises + capstone, no answers
- park_entries.csv                      : 121 raw records including intentional quality issues
- attractions.json                     : 10 newline-delimited JSON attraction records with nested fields
- attraction_maintenance.csv           : 28 maintenance records
- park_entry_changes.csv               : 10 MERGE source records (5 existing, 5 new)
- park_entries_incremental.csv          : 12 append-only records for a later pipeline run
- databricks_dataset_setup.py          : Databricks notebook source file, setup only

QUICK START
1. Upload the five data files to one folder in a Unity Catalog Volume.
2. Import databricks_dataset_setup.py into your Databricks workspace, or paste its cells into a notebook.
3. Edit CATALOG, SCHEMA, and BASE_PATH in the first notebook cell.
4. Run the setup once. It creates tp_entries_raw, tp_attractions, tp_maintenance,
   and tp_entry_changes as Delta tables in your selected catalog/schema.
5. Complete the participant handout in order. Create separate working tables
   for UPDATE/DELETE/MERGE. Do not modify tp_entries_raw until incremental loading.
6. For pipeline tasks, use Lakeflow Spark Declarative Pipelines (formerly DLT).
   SQL and Python pipelines must have different output table names.
7. Append park_entries_incremental.csv to tp_entries_raw only AFTER the initial
   pipeline update, then run another triggered pipeline update.

NOTES
- The source intentionally contains a duplicate entry ID, missing values,
  invalid numerical values, and an unknown attraction ID for data-quality tasks.
- attractions.json is JSON Lines / newline-delimited JSON, not a single JSON array.
- A compatible Unity Catalog Volume and permission to create tables/pipelines are required.
- External tables and in-place Parquet conversion are conditional on an approved
  external location; don't use internal __unitystorage paths.
- Time Travel needs retained data files; avoid destructive VACUUM during assessment.
- Structured Streaming rate-source exercises need compatible compute.
- This package does not contain solutions.
