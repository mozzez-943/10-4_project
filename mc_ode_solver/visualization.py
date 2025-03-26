# visualization.py
import matplotlib.pyplot as plt

def plot_solution(t_vals, solutions, title="ODE Solution", xlabel="Time", ylabel="Solution"):
    """
    Plot the solution of the ODE over time.
    """
    plt.plot(t_vals, solutions, label="Solution")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

def plot_confidence_intervals(t_vals, solutions, confidence_interval, title="Confidence Interval"):
    """
    Plot the confidence intervals for the ODE solution.
    """
    lower_bound = solutions - confidence_interval
    upper_bound = solutions + confidence_interval
    plt.fill_between(t_vals, lower_bound, upper_bound, alpha=0.2, label="Confidence Interval")
    plt.plot(t_vals, solutions, label="Solution")
    plt.xlabel("Time")
    plt.ylabel("Solution")
    plt.title(title)
    plt.legend()
    plt.show()
