"""
VISUALIZATION MODULE

This file contains plotting functions used to
visualize Monte Carlo simulation results.

Charts:
- Simulated stock price paths
- Distribution of final stock prices

Purpose:
Help understand how stock prices evolve
and how outcomes are distributed.
"""
import matplotlib.pyplot as plt


def plot_paths(paths):

    plt.figure(figsize=(10, 6))

    plt.plot(paths)

    plt.title("Monte Carlo Stock Price Paths")

    plt.xlabel("Time Step")

    plt.ylabel("Stock Price")

    plt.grid(True)

    plt.show()

#what are the POSSIBLE prices after one year
def plot_histogram(final_prices):

    plt.figure(figsize=(10, 6))

    plt.hist(final_prices, bins=50)

    plt.title("Distribution of Final Prices")

    plt.xlabel("Final Stock Price")

    plt.ylabel("Frequency")

    plt.grid(True)

    plt.show()