import pandas as pd
import os
from pipelines.pcaf_calculator import compute_financed_emissions

def test_compute_financed_emissions():
    """Test the complete PCAF calculation pipeline"""
    # This assumes CSV files are in the same directory as the script
    result = compute_financed_emissions()
    
    # Test that result is not None and has expected structure
    assert result is not None
    assert not result.empty
    assert 'financed_emissions_tco2e' in result.columns
    assert 'attribution_factor' in result.columns
    assert 'scope12' in result.columns
    
    # Test that we have the expected counterparties from your CSV
    expected_counterparties = {'ACME_CORP', 'BRAVO_INC', 'CASCADE_LTD'}
    actual_counterparties = set(result['counterparty_id'].unique())
    assert expected_counterparties == actual_counterparties
    
    # Test calculations for ACME_CORP (first row in your data)
    acme_row = result[result['counterparty_id'] == 'ACME_CORP'].iloc[0]
    
    # Scope12 should be 120000 + 80000 = 200000
    assert acme_row['scope12'] == 200000.0
    
    # Attribution factor should be 5000000 / 80000000 = 0.0625
    expected_attribution = 5000000.0 / 80000000.0
    assert abs(acme_row['attribution_factor'] - expected_attribution) < 0.001
    
    # Financed emissions should be 200000 * 0.0625 = 12500
    expected_financed_emissions = 200000.0 * expected_attribution
    assert abs(acme_row['financed_emissions_tco2e'] - expected_financed_emissions) < 0.001
