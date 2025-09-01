import csv
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from libs.pcaf_attribution.attribution import attribution_factor, financed_emissions


from libs.pcaf_attribution.attribution import attribution_factor, financed_emissions


def test_attribution_factor_basic():
    assert attribution_factor(100, 1000) == 0.1
    assert attribution_factor(0, 1000) == 0.0
    assert attribution_factor(100, 0) == 0.0
    assert attribution_factor(100, None) == 0.0

def test_financed_emissions_basic():
    assert financed_emissions(500, 0.1) == 50.0
    assert financed_emissions(0, 0.5) == 0.0

def test_raw_csvs_exist_and_have_columns():
    # exposures
    with open('data/raw/exposures.csv', newline='') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        assert set(['as_of_date','counterparty_id','product','currency','outstanding_amt',
                    'collateral_value','tenure_months','risk_weight','source','ingested_ts']).issubset(cols)

    # ghg_emissions
    with open('data/raw/ghg_emissions.csv', newline='') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        assert set(['counterparty_id','year','scope1','scope2','scope3','data_quality','source','as_of_date']).issubset(cols)

    # valuation_metrics
    with open('data/raw/valuation_metrics.csv', newline='') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        assert set(['counterparty_id','year','evic','total_assets','market_cap','source']).issubset(cols)
