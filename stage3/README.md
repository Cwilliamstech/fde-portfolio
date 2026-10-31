# Stage 3: Legacy Data Extraction & ETL

An invoice pipeline over synthetic PDFs.

## What's here
- `extract.py`: extracts text from PDFs, cleans vendor/total/date, quarantines duplicates, loads into SQLite. Flags scanned PDFs that have no text layer.
- `invoices/`: synthetic invoices, a manifest, and OCR test output.
- `invoice_dbt/`: dbt model `flagged_invoices` (total > 3000) with not_null/unique tests.
- invoice_pipeline.py: Airflow DAG that runs extract.py, then dbt run + test, daily.

## Design notes
- Reconcile against a manifest: 8 files vs 7 loaded rows, with the gap explained by a duplicate.
- OCR output can't be trusted like a text layer, so uncertain scans go to human review.
- Airflow ran the pipeline as a DAG: extract, then dbt run + test.