import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now imports will work
from pipelines.pcaf_calculator import compute_financed_emissions

def main():
    """Run PCAF calculator locally"""
    print("🚀 Running PCAF Calculator - Day 2 Local Execution")
    print("=" * 60)
    
    result = compute_financed_emissions()
    
    if result is not None:
        print("\n📊 PCAF Calculation Summary:")
        print(f"Total counterparties processed: {len(result)}")
        print(f"Total portfolio exposure: ${result['outstanding_amt'].sum():,.0f}")
        print(f"Total financed emissions: {result['financed_emissions_tco2e'].sum():,.2f} tCO2e")
        
        print("\n📋 Detailed Results:")
        print(result[['counterparty_id', 'outstanding_amt', 'evic', 'scope12', 
                     'attribution_factor', 'financed_emissions_tco2e']].to_string(index=False))
    else:
        print("❌ Failed to calculate financed emissions")

if __name__ == "__main__":
    main()
