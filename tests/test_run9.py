import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Add project directory to path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Import directly from module files without relying on __init__.py
from mc_ode_solver.solver import MonteCarloODESolver
from mc_ode_solver.benchmarks import linear_ode, nonlinear_ode
from mc_ode_solver.visualization import plot_solution

def test_linear():
    """Test the linear ODE solver and compare with analytical solution"""
    y0 = 1.0
    t_span = (0, 2)
    
    # Monte Carlo solution
    solver = MonteCarloODESolver(linear_ode, y0, t_span, method='importance_sampling', num_samples=1000)
    t_vals, solutions = solver.solve()
    
    # Analytical solution (y = e^(-2t))
    analytical = y0 * np.exp(-2 * t_vals)
    
    # scipy solution for comparison
    scipy_sol = solve_ivp(linear_ode, t_span, [y0], t_eval=t_vals)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, solutions, 'b-', label='Monte Carlo')
    plt.plot(t_vals, analytical, 'r--', label='Analytical')
    plt.plot(t_vals, scipy_sol.y[0], 'g:', label='SciPy')
    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.title('Linear ODE Solution: dy/dt = -2y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Calculate error
    mc_error = np.mean(np.abs(solutions - analytical))
    print(f"Mean absolute error: {mc_error:.6f}")

if __name__ == "__main__":
    test_linear()