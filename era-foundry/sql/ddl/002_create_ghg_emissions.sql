-- 002_create_ghg_emissions.sql
CREATE TABLE IF NOT EXISTS `raw_silver.ghg_emissions` (
  counterparty_id STRING,
  year INT64,
  scope1 NUMERIC,
  scope2 NUMERIC,
  scope3 NUMERIC,
  data_quality STRING,
  source STRING,
  as_of_date DATE
);
