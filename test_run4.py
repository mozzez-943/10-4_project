import sys
import os

# Add the mc_ode_solver folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mc_ode_solver')))

# test_run.py

from mc_ode_solver import MonteCarloODESolver, plot_solution
from mc_ode_solver.benchmarks import nonlinear_ode

# Solve the ODE using Importance Sampling
solver_is = MonteCarloODESolver(ode_func=nonlinear_ode, y0=1, t_span=(0, 10), method='importance_sampling', num_samples=1000)
t_vals_is, solutions_is = solver_is.solve()

# Solve the ODE using Quasi-Monte Carlo
solver_qmc = MonteCarloODESolver(ode_func=nonlinear_ode, y0=1, t_span=(0, 10), method='quasi_monte_carlo', num_samples=1000)
t_vals_qmc, solutions_qmc = solver_qmc.solve()

# Plot the results for comparison
plot_solution(t_vals_is, solutions_is, title="Importance Sampling Solution for Nonlinear ODE")
plot_solution(t_vals_qmc, solutions_qmc, title="Quasi-Monte Carlo Solution for Nonlinear ODE")
