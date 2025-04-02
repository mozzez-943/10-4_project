import numpy as np

def importance_sampling(ode_func, t, y, dt, num_samples=1000):
    """
    Perform importance sampling for the ODE solver with proper time step integration.
    
    Parameters:
        ode_func (function): The ODE function representing dy/dt = f(t, y).
        t (float): The current time step.
        y (float): The current state (solution) at time t.
        dt (float): The time step size for integration.
        num_samples (int): The number of samples to generate for importance sampling.
    
    Returns:
        y_next (float): The updated state estimate after performing importance sampling.
    """
    # Sample from a proposal distribution (normal distribution centered around y)
    samples = np.random.normal(loc=y, scale=0.1, size=num_samples)
    
    # Compute importance weights (simplified weights)
    weights = np.exp(-(samples - y)**2)
    weights /= np.sum(weights)  # Normalize weights

    # Compute the ODE value
    dydt = ode_func(t, y)
    
    # Euler step with weighted perturbation
    y_next = y + dydt * dt + np.sum((samples - y) * weights) * np.sqrt(dt)
    
    return y_next

def quasi_monte_carlo(ode_func, t, y, dt, dim=1, scramble=True):
    """
    Use a quasi-random sequence for Monte Carlo integration with proper time step.
    
    Parameters:
        ode_func (function): The ODE function representing dy/dt = f(t, y).
        t (float): The current time step.
        y (float): The current state (solution) at time t.
        dt (float): The time step size for integration.
        dim (int): The dimensionality of the sequence (default is 1).
        scramble (bool): Whether to scramble the sequence (default is True).
    
    Returns:
        y_next (float): The updated state estimate after applying quasi-Monte Carlo.
    """
    # Generate a pseudo-QMC sample (using fixed values distributed in [0, 1])
    samples = np.linspace(0.1, 0.9, 5)  # Multiple samples for stability
    
    # Compute the ODE value
    dydt = ode_func(t, y)
    
    # Apply perturbation from QMC sequence
    perturbation = np.mean(samples) - 0.5  # Center around 0
    y_next = y + dydt * dt + perturbation * np.sqrt(dt)
    
    return y_next
