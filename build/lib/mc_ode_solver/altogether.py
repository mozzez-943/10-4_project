import numpy as np
import matplotlib.pyplot as plt

# Benchmark ODEs
def linear_ode(t, y):
    """ Simple linear ODE: dy/dt = -2y """
    return -2 * y

def nonlinear_ode(t, y):
    """ Nonlinear ODE: dy/dt = y^2 - 1 """
    return y**2 - 1

# Updated Sampler functions
def importance_sampling(ode_func, t, y, dt, num_samples=1000):
    """
    Perform importance sampling for the ODE solver with proper time step integration.
    
    Parameters:
    - ode_func: Function representing dy/dt = f(t, y)
    - t: Current time step
    - y: Current state
    - dt: Time step size
    - num_samples: Number of importance samples
    
    Returns:
    - Next state estimate
    """
    # Sample from proposal distribution (reduced scale for stability)
    samples = np.random.normal(loc=y, scale=0.1, size=num_samples)
    
    # Compute importance weights
    weights = np.exp(-(samples - y)**2)  # Simplified weights
    weights /= np.sum(weights)  # Normalize weights

    # Compute ODE value
    dydt = ode_func(t, y)
    
    # Euler step with weighted perturbation
    y_next = y + dydt * dt + np.sum((samples - y) * weights) * np.sqrt(dt)
    
    return y_next

def quasi_monte_carlo(ode_func, t, y, dt, dim=1, scramble=True):
    """
    Use a quasi-random sequence for Monte Carlo integration with proper time step.
    
    Parameters:
    - ode_func: Function representing dy/dt = f(t, y)
    - t: Current time step
    - y: Current state
    - dt: Time step size
    - dim: Dimensionality of the sequence
    - scramble: Whether to scramble the sequence
    
    Returns:
    - Next state estimate
    """
    # Generate a pseudo-QMC sample
    # For simplicity using fixed values distributed in [0, 1]
    samples = np.linspace(0.1, 0.9, 5)  # Multiple samples for stability
    
    # Compute ODE value
    dydt = ode_func(t, y)
    
    # Euler step with QMC perturbation
    perturbation = np.mean(samples) - 0.5  # Center around 0
    y_next = y + dydt * dt + perturbation * np.sqrt(dt)
    
    return y_next

# Updated Solver class
class MonteCarloODESolver:
    def __init__(self, ode_func, y0, t_span, method='quasi_monte_carlo', num_samples=1000):
        """Initialize the solver."""
        self.ode_func = ode_func
        self.y0 = y0
        self.t_span = t_span
        self.method = method
        self.num_samples = num_samples

    def solve(self):
        t0, tf = self.t_span
        t_vals = np.linspace(t0, tf, self.num_samples)
        dt = (tf - t0) / (self.num_samples - 1)  # Time step size
        
        # Initial solution array
        solutions = np.zeros(self.num_samples)
        solutions[0] = self.y0

        # Perform Monte Carlo sampling based on the chosen method
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

# Visualization function
def plot_solution(t_vals, solutions, title="ODE Solution", xlabel="Time", ylabel="Solution"):
    """Plot the solution of the ODE over time."""
    plt.plot(t_vals, solutions, label="Monte Carlo Solution")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Test function
def run_test():
    # Parameters
    y0 = 1.0
    t_span = (0, 2)
    
    # Create and run solver with both methods
    solver1 = MonteCarloODESolver(linear_ode, y0, t_span, method='importance_sampling', num_samples=200)
    t_vals1, solutions1 = solver1.solve()
    
    solver2 = MonteCarloODESolver(linear_ode, y0, t_span, method='quasi_monte_carlo', num_samples=200)
    t_vals2, solutions2 = solver2.solve()
    
    # Analytical solution for comparison
    analytical = y0 * np.exp(-2 * t_vals1)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals1, solutions1, 'b-', label='Importance Sampling')
    plt.plot(t_vals2, solutions2, 'g-', label='Quasi-Monte Carlo')
    plt.plot(t_vals1, analytical, 'r--', label='Analytical')
    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.title('Linear ODE Solution: dy/dt = -2y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Calculate errors
    error1 = np.mean(np.abs(solutions1 - analytical))
    error2 = np.mean(np.abs(solutions2 - analytical))
    print(f"Mean absolute error (Importance Sampling): {error1:.6f}")
    print(f"Mean absolute error (Quasi-Monte Carlo): {error2:.6f}")
    
    # Test nonlinear ODE
    y0_nl = 0.0
    t_span_nl = (0, 3)
    
    solver_nl = MonteCarloODESolver(nonlinear_ode, y0_nl, t_span_nl, method='importance_sampling', num_samples=300)
    t_vals_nl, solutions_nl = solver_nl.solve()
    
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals_nl, solutions_nl, 'b-', label='Monte Carlo')
    plt.axhline(y=-1, color='r', linestyle='--', label='Asymptotic Value')
    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.title('Nonlinear ODE Solution: dy/dt = y² - 1')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_test()