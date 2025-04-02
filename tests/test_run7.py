import sys
import os

# Add the mc_ode_solver folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mc_ode_solver')))

# Now you can import your modules
from mc_ode_solver.solver import MonteCarloODESolver
from mc_ode_solver.benchmarks import linear_ode, nonlinear_ode
from mc_ode_solver.visualization import plot_solution


solver_is = MonteCarloODESolver(ode_func=nonlinear_ode, y0=1, t_span=(0, 10), method='importance_sampling', num_samples=1040)
t_vals_is, solutions_is = solver_is.solve()
plot_solution(t_vals_is, solutions_is, title="Importance Sampling Solution for Nonlinear ODE")
