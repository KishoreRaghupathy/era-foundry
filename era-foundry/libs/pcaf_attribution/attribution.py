from __future__ import annotations


def attribution_factor(outstanding_amt: float | int, evic: float | int | None) -> float:
    """Compute attribution factor per PCAF (loan share of EVIC).
    Falls back to 0 if EVIC is missing or zero (to avoid divide-by-zero).
    """
    try:
        if evic is None or float(evic) == 0.0:
            return 0.0
        return float(outstanding_amt) / float(evic)
    except Exception:
        return 0.0


def financed_emissions(scope12: float | int, attribution: float | int) -> float:
    """Financed emissions = scope 1+2 * attribution factor.
    (Scope 3 optional, handled later.)
    """
    try:
        return float(scope12) * float(attribution)
    except Exception:
        return 0.0
