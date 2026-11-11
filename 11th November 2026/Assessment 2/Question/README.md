# Azure Databricks Hands-on Assessment - City Water Network Monitoring

## Files
- `assessment.pdf` - 55 exercises + final capstone, no solutions or marks
- `databricks_setup.py` - Databricks notebook source that creates the required Delta tables
- `water_meter_readings.csv` - 157 initial readings (including deliberate data-quality anomalies)
- `water_zones.json` - 11 newline-delimited JSON zone records with nested location fields
- `water_service_requests.csv` - 36 maintenance/service requests
- `water_reading_changes.csv` - 12 MERGE/UPSERT change records
- `water_readings_incremental.csv` - 18 new append-only readings
- `assessment_questions.md` - editable text version of the questions

## Databricks setup
1. In your Unity Catalog-enabled Azure Databricks workspace, choose a catalog and schema where you can create tables and volumes.
2. Create a managed Volume named `assessment_files` (or use an existing volume). For example, in a SQL cell:
   `CREATE VOLUME IF NOT EXISTS rithika_databricks.default.assessment_files;`
   Change catalog/schema as appropriate.
3. Create a folder named `water_network` in the volume and upload all five CSV/JSON data files into it. Example base path:
   `/Volumes/rithika_databricks/default/assessment_files/water_network/`
4. Import `databricks_setup.py` as a Databricks notebook (or paste its cells into a Python notebook).
5. Adjust the `catalog`, `schema`, `volume`, and `folder` widgets and run the notebook ONCE. It will create the source, working, zone, request, change-staging, and incremental-staging Delta tables.
6. Give participants the assessment PDF. They should use separate copies for destructive exercises.

## Important
- This assessment includes deliberate duplicates, nulls, an unknown zone ID, invalid measurements, and a zone with no readings.
- Do not rerun setup after beginning the assessment: it overwrites initial tables and resets their histories.
- Keep `water_meter_readings_source` append-only once the Lakeflow pipeline is running. Use `water_meter_readings_work` for MERGE/updates/deletes.
- Lakeflow SQL/Python source definitions belong in a Lakeflow pipeline, not ordinary notebook cells.
- Streaming `rate` demonstrations require compatible compute. Global temp views and VACUUM DRY RUN depend on runtime and compute support.
- Use a Unity Catalog Volume for Parquet; do not modify Databricks-managed `__unitystorage` paths.
- No exercise solutions are included.
