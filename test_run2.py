import sys
import os

# Add the mc_ode_solver folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mc_ode_solver')))

# test_run.py

from mc_ode_solver import MonteCarloODESolver, plot_solution
from mc_ode_solver.benchmarks import linear_ode

# Set up the solver for a linear ODE: dy/dt = -2y
solver = MonteCarloODESolver(ode_func=linear_ode, y0=1, t_span=(0, 10), method='quasi_monte_carlo', num_samples=1000)

# Solve the ODE
t_vals, solutions = solver.solve()

# Plot the solution
plot_solution(t_vals, solutions, title="Linear ODE Solution using Quasi-Monte Carlo")
