# utils.py
import numpy as np

def validate_ode_func(ode_func):
    """
    Validate the ODE function to ensure it is callable and returns a valid result.
    """
    try:
        test_value = ode_func(0, 1)
    except Exception as e:
        raise ValueError(f"Invalid ODE function: {e}")
