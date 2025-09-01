-- 001_create_exposure_positions.sql
-- BigQuery Standard SQL; assumes dataset `raw_silver`
CREATE TABLE IF NOT EXISTS `raw_silver.exposure_positions` (
  as_of_date DATE,
  counterparty_id STRING,
  product STRING,
  currency STRING,
  outstanding_amt NUMERIC,
  collateral_value NUMERIC,
  tenure_months INT64,
  risk_weight NUMERIC,
  source STRING,
  ingested_ts TIMESTAMP
);
