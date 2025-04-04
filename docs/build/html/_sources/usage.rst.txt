Usage
=====

The ``mc_ode_solver`` package provides tools for solving ordinary differential equations.

Basic Usage
----------

Import the main solver module:

.. code-block:: python

    from mc_ode_solver import solver

Solving a Simple ODE
-------------------

.. code-block:: python

    from mc_ode_solver.solver import solve_ode
    
    # Define your ODE function (dy/dt = f(t, y))
    def example_ode(t, y):
        return -0.5 * y  # Example: dy/dt = -0.5y
    
    # Initial conditions
    t0 = 0.0
    y0 = 1.0
    
    # Time points
    t_final = 10.0
    dt = 0.1
    
    # Solve the ODE
    solution = solve_ode(example_ode, t0, y0, t_final, dt)
    
    # Access the results
    times = solution['t']
    values = solution['y']

Visualization
------------

The package includes visualization tools:

.. code-block:: python

    from mc_ode_solver.visualization import plot_solution
    
    # Plot the solution
    plot_solution(solution)

Benchmarking
-----------

Compare performance of different solvers:

.. code-block:: python

    from mc_ode_solver.benchmarks import run_benchmark
    
    # Define your ODE system
    def system(t, y):
        return [y[1], -y[0]]  # Simple harmonic oscillator
    
    # Run benchmark
    results = run_benchmark(system, t0=0, y0=[1.0, 0.0], t_final=10.0)
    
    # Display results
    print(results)

Advanced Usage
-------------

For more complex systems and advanced features, refer to the API documentation.