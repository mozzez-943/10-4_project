# benchmarks.py
def linear_ode(t, y):
    """ Simple linear ODE: dy/dt = -2y """
    return -2 * y

def nonlinear_ode(t, y):
    """ Nonlinear ODE: dy/dt = y^2 - 1 """
    return y**2 - 1
