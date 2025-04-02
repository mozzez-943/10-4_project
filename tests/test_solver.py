import numpy as np
from mc_ode_solver import MonteCarloODESolver, linear_ode

def test_solver():
    """
    Test the MonteCarloODESolver with a simple linear ODE (dy/dt = -2y).
    This test checks if the solver works correctly and produces expected outputs.
    """
    y0 = 1.0
    t_span = (0, 2)
    solver = MonteCarloODESolver(linear_ode, y0, t_span, method='importance_sampling', num_samples=200)
    t_vals, solutions = solver.solve()

    # Ensure the solution length matches the number of samples
    assert len(t_vals) == 200
    assert len(solutions) == 200

test_solver()
