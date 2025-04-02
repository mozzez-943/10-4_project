def linear_ode(t, y):
    """
    Define a simple linear ODE: dy/dt = -2y.
    
    Parameters:
        t (float): Current time step (not used in the linear ODE, but required for generality).
        y (float): Current state (solution) of the system.
    
    Returns:
        dydt (float): The rate of change of y at time t.
    """
    return -2 * y

def nonlinear_ode(t, y):
    """
    Define a nonlinear ODE: dy/dt = y^2 - 1.
    
    Parameters:
        t (float): Current time step (not used in the nonlinear ODE, but required for generality).
        y (float): Current state (solution) of the system.
    
    Returns:
        dydt (float): The rate of change of y at time t.
    """
    return y**2 - 1
