import numpy as np
from .samplers import importance_sampling, quasi_monte_carlo

class MonteCarloODESolver:
    """
    A solver for ordinary differential equations (ODEs) using Monte Carlo methods.
    
    The solver supports two methods for Monte Carlo integration: importance sampling and quasi-Monte Carlo.
    
    Attributes:
        ode_func (function): The ODE function to solve, where the function returns dy/dt = f(t, y).
        y0 (float): The initial condition for the ODE.
        t_span (tuple): A tuple representing the time span (t0, tf) for the solution.
        method (str): The Monte Carlo method to use ('importance_sampling' or 'quasi_monte_carlo').
        num_samples (int): The number of Monte Carlo samples to use for the integration.
    """
    
    def __init__(self, ode_func, y0, t_span, method='quasi_monte_carlo', num_samples=1000):
        """
        Initialize the solver with the given parameters.
        
        Parameters:
            ode_func (function): The ODE function to solve.
            y0 (float): The initial condition for the ODE.
            t_span (tuple): The time span for the ODE solution.
            method (str): The Monte Carlo method to use ('importance_sampling' or 'quasi_monte_carlo').
            num_samples (int): The number of Monte Carlo samples to use.
        """
        self.ode_func = ode_func
        self.y0 = y0
        self.t_span = t_span
        self.method = method
        self.num_samples = num_samples

    def solve(self):
        """
        Solve the ODE using the selected Monte Carlo method.
        
        This method iteratively computes the ODE solution at each time step using the selected
        sampling method (importance sampling or quasi-Monte Carlo).
        
        Returns:
            t_vals (np.ndarray): An array of time values.
            solutions (np.ndarray): An array of solution values corresponding to the time steps.
        """
        t0, tf = self.t_span
        t_vals = np.linspace(t0, tf, self.num_samples)
        dt = (tf - t0) / (self.num_samples - 1)  # Time step size
        
        # Initialize solution array
        solutions = np.zeros(self.num_samples)
        solutions[0] = self.y0

        # Apply chosen sampling method
        for i in range(1, self.num_samples):
            t_current = t_vals[i-1]
            y_current = solutions[i-1]
            
            if self.method == 'importance_sampling':
                solutions[i] = importance_sampling(self.ode_func, t_current, y_current, dt)
            elif self.method == 'quasi_monte_carlo':
                solutions[i] = quasi_monte_carlo(self.ode_func, t_current, y_current, dt)
            else:
                raise ValueError(f"Unknown method: {self.method}")

        return t_vals, solutions
