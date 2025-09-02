import sys
import os
import pandas as pd

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now imports will work
from libs.pcaf_attribution.attribution import attribution_factor, financed_emissions

def compute_financed_emissions():
    """Calculate PCAF financed emissions using CSV data files"""
    
    # Define file paths relative to project root
    data_dir = os.path.join(project_root, 'data', 'raw')
    
    exposures_file = os.path.join(data_dir, 'exposures.csv')
    emissions_file = os.path.join(data_dir, 'ghg_emissions.csv')
    valuations_file = os.path.join(data_dir, 'valuation_metrics.csv')
    
    try:
        # Load data from CSV files
        exposures = pd.read_csv(exposures_file)
        emissions = pd.read_csv(emissions_file)
        valuations = pd.read_csv(valuations_file)
        
        print(f"✅ Loaded {len(exposures)} exposures, {len(emissions)} emissions records, {len(valuations)} valuations")
        
    except FileNotFoundError as e:
        print(f"❌ Error: Could not find data file - {e}")
        print(f"Looking in directory: {data_dir}")
        return None
    
    # Calculate scope12 (scope1 + scope2)
    emissions['scope12'] = emissions['scope1'].astype(float) + emissions['scope2'].astype(float)
    
    # Get latest data per counterparty
    emissions_latest = emissions.sort_values(['counterparty_id','year'], ascending=[True, False]) \
                                .groupby('counterparty_id', as_index=False).first()
    
    valuations_latest = valuations.sort_values(['counterparty_id','year'], ascending=[True, False]) \
                                  .groupby('counterparty_id', as_index=False).first()
    
    # Merge data
    df = exposures.merge(emissions_latest[['counterparty_id','scope12','data_quality']], on='counterparty_id', how='left') \
                  .merge(valuations_latest[['counterparty_id','evic']], on='counterparty_id', how='left')
    
    # Calculate PCAF metrics
    df['attribution_factor'] = df.apply(lambda r: attribution_factor(r['outstanding_amt'], r['evic']), axis=1)
    df['financed_emissions_tco2e'] = df.apply(lambda r: financed_emissions(r.get('scope12', 0.0), r['attribution_factor']), axis=1)
    
    return df

if __name__ == "__main__":
    result = compute_financed_emissions()
    
    if result is not None:
        print("\nPCAF Financed Emissions Results:")
        print("=" * 80)
        print(result[['counterparty_id', 'outstanding_amt', 'evic', 'scope12', 
                     'attribution_factor', 'financed_emissions_tco2e']].to_string(index=False))
