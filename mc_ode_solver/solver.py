# solver.py
import numpy as np
from .samplers import importance_sampling, quasi_monte_carlo

class MonteCarloODESolver:
    def __init__(self, ode_func, y0, t_span, method='quasi_monte_carlo', num_samples=1000):
        """
        Initialize the solver.
        
        Parameters:
        - ode_func: Function defining the ODE (dy/dt = f(t, y))
        - y0: Initial condition (initial value of y)
        - t_span: Time span (start, end)
        - method: Monte Carlo method ('importance_sampling' or 'quasi_monte_carlo')
        - num_samples: Number of samples for Monte Carlo estimation
        """
        self.ode_func = ode_func
        self.y0 = y0
        self.t_span = t_span
        self.method = method
        self.num_samples = num_samples

    def solve(self):
        t0, tf = self.t_span
        t_vals = np.linspace(t0, tf, self.num_samples)
        
        # Initial solution array
        solutions = np.zeros(self.num_samples)
        solutions[0] = self.y0

        # Perform Monte Carlo sampling based on the chosen method
        for i in range(1, self.num_samples):
            if self.method == 'importance_sampling':
                solutions[i] = importance_sampling(self.ode_func, t_vals[i-1], solutions[i-1])
            elif self.method == 'quasi_monte_carlo':
                solutions[i] = quasi_monte_carlo(self.ode_func, t_vals[i-1], solutions[i-1])

        return t_vals, solutions
