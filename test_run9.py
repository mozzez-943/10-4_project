# In test_solver.py
import unittest
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Add the parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from package
from mc_ode_solver.solver import MonteCarloODESolver
from mc_ode_solver.benchmarks import linear_ode, nonlinear_ode

# Test class as shown previously

class TestMonteCarloODESolver(unittest.TestCase):
    def setUp(self):
        # Disable plotting for tests
        plt.ioff()
    
    def test_linear_ode_importance_sampling(self):
        """Test solver with linear ODE using importance sampling."""
        y0 = 1.0
        t_span = (0, 1)
        solver = MonteCarloODESolver(linear_ode, y0, t_span, method='importance_sampling', num_samples=100)
        t_vals, solutions = solver.solve()
        
        # Expected solution for dy/dt = -2y is y = y0*e^(-2t)
        expected = y0 * np.exp(-2 * t_vals)
        # Allow for some error due to stochastic nature
        max_error = np.max(np.abs(solutions - expected)) / np.max(np.abs(expected))
        self.assertLess(max_error, 0.2, f"Max relative error {max_error} exceeds threshold")
    
    def test_nonlinear_ode_quasi_monte_carlo(self):
        """Test solver with nonlinear ODE using quasi-Monte Carlo."""
        y0 = 0.0
        t_span = (0, 1)
        solver = MonteCarloODESolver(nonlinear_ode, y0, t_span, method='quasi_monte_carlo', num_samples=100)
        t_vals, solutions = solver.solve()
        
        # For the ODE dy/dt = y^2 - 1 with y(0) = 0, solution approaches -1
        self.assertTrue(solutions[-1] < -0.5, "Solution should approach -1")
    
    def test_convergence_with_increasing_samples(self):
        """Test if increasing samples improves accuracy."""
        y0 = 1.0
        t_span = (0, 1)
        
        errors = []
        sample_sizes = [100, 500, 1000]
        
        for n in sample_sizes:
            solver = MonteCarloODESolver(linear_ode, y0, t_span, method='importance_sampling', num_samples=n)
            t_vals, solutions = solver.solve()
            
            expected = y0 * np.exp(-2 * t_vals)
            error = np.mean(np.abs(solutions - expected))
            errors.append(error)
        
        # Verify errors decrease with more samples
        self.assertTrue(errors[0] > errors[-1], "Error should decrease with more samples")
    
    def test_invalid_method(self):
        """Test behavior with invalid method."""
        solver = MonteCarloODESolver(linear_ode, 1.0, (0, 1), method='invalid_method')
        with self.assertRaises(Exception):
            solver.solve()

if __name__ == '__main__':
    unittest.main()