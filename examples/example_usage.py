from mc_ode_solver import MonteCarloODESolver, linear_ode, nonlinear_ode
import matplotlib.pyplot as plt

y0 = 1.0
t_span = (0, 2)

# Create and solve with importance sampling
solver = MonteCarloODESolver(linear_ode, y0, t_span, method='importance_sampling', num_samples=200)
t_vals, solutions = solver.solve()

# Plot results
plt.plot(t_vals, solutions)
plt.xlabel('Time')
plt.ylabel('Solution')
plt.title('Monte Carlo ODE Solution')
plt.show()
