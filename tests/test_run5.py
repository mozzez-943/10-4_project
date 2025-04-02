import sys
import os

# Add the mc_ode_solver folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mc_ode_solver')))

# test_run.py

from mc_ode_solver import MonteCarloODESolver, plot_confidence_intervals
from mc_ode_solver.benchmarks import nonlinear_ode
import numpy as np

# Set up the solver for a nonlinear ODE: dy/dt = y^2 - 1
solver = MonteCarloODESolver(ode_func=nonlinear_ode, y0=1, t_span=(0, 10), method='quasi_monte_carlo', num_samples=1000)

# Solve the ODE
t_vals, solutions = solver.solve()

# Calculate confidence intervals (for example, +/- 1 std dev)
confidence_interval = np.std(solutions)  # Simplified for demonstration
plot_confidence_intervals(t_vals, solutions, confidence_interval, title="Nonlinear ODE with Confidence Intervals")
