import numpy as np
from scipy.stats import norm, qmc

def importance_sampling(ode_func, t, y, num_samples=1000):
    """
    Perform importance sampling for the ODE solver.
    
    Parameters:
    - ode_func: Function representing dy/dt = f(t, y)
    - t: Current time step
    - y: Current state
    - num_samples: Number of importance samples
    
    Returns:
    - Weighted next state estimate
    """
    # Sample from proposal distribution (Gaussian centered at y)
    samples = np.random.normal(loc=y, scale=0.5, size=num_samples)
    
    # Compute importance weights using likelihood ratio
    weights = norm.pdf(samples, loc=y, scale=1.0)  # Prior Gaussian likelihood
    weights /= np.sum(weights)  # Normalize weights

    # Compute weighted estimate of the next state
    y_next = np.sum(samples * weights) + ode_func(t, y)
    
    return y_next

def quasi_monte_carlo(ode_func, t, y, dim=1, scramble=True):
    """
    Use a quasi-random Sobol sequence for Monte Carlo integration.
    
    Parameters:
    - ode_func: Function representing dy/dt = f(t, y)
    - t: Current time step
    - y: Current state
    - dim: Dimensionality of the sequence
    - scramble: Whether to scramble the sequence for better randomness
    
    Returns:
    - Next state estimate
    """
    # Generate a Sobol sequence sample
    sampler = qmc.Sobol(d=dim, scramble=scramble)
    sobol_sample = sampler.random(n=1)[0, 0]  # Extract the first sample

    # Compute the next state using the Sobol sample as a weighting factor
    y_next = y + ode_func(t, y) * sobol_sample
    
    return y_next
