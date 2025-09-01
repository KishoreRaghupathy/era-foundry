-- 003_create_valuation_metrics.sql
CREATE TABLE IF NOT EXISTS `raw_silver.valuation_metrics` (
  counterparty_id STRING,
  year INT64,
  evic NUMERIC,
  total_assets NUMERIC,
  market_cap NUMERIC,
  source STRING
);
