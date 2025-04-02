import sys
import os

# Add the mc_ode_solver folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mc_ode_solver')))

# test_run.py

from mc_ode_solver import MonteCarloODESolver, plot_solution
import numpy as np

# Custom ODE: dy/dt = sin(t) * y
def custom_ode(t, y):
    return np.sin(t) * y

# Set up the solver for the custom ODE
solver = MonteCarloODESolver(ode_func=custom_ode, y0=1, t_span=(0, 10), method='quasi_monte_carlo', num_samples=1000)

# Solve the ODE
t_vals, solutions = solver.solve()

# Plot the solution
plot_solution(t_vals, solutions, title="Solution for Custom ODE: dy/dt = sin(t) * y")
