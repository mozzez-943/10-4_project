from montecarlo_ode_solver.solver import MonteCarloODESolver
from montecarlo_ode_solver.benchmarks import linear_ode, nonlinear_ode
from montecarlo_ode_solver.visualization import plot_solution

# Choose a problem and method
ode_func = linear_ode  # or nonlinear_ode
solver = MonteCarloODESolver(ode_func, y0=1, t_span=(0, 10), method='quasi_monte_carlo', num_samples=1000)

# Solve the ODE
t_vals, solutions = solver.solve()

# Visualize the solution
plot_solution(t_vals, solutions)
