"""
STOCK PATH GENERATOR

This file generates simulated stock price paths using
Geometric Brownian Motion (GBM).

The model assumes:
- Stock prices grow at the risk-free rate.
- Prices experience random market shocks.
- Prices can never become negative.

Output:
An assortment of simulated stock prices where:
Rows    = time steps (days)
Columns = simulation paths
"""
import numpy as np

# Generate stock price paths using Geometric Brownian Motion (GBM).
def generate_paths(
        S0,
        r,
        sigma,
        T,
        steps,
        n_paths):

    dt = T / steps

    paths = np.zeros((steps + 1, n_paths))

    paths[0] = S0

    for t in range(1, steps + 1):
        #creates random numbers from normal distribution
        Z = np.random.standard_normal(n_paths)
        # GBM Stock Price Model:
        # Previous Price × e^(drift + randomness)
        #
        # Drift      = (r - 0.5*sigma^2)*dt
        #              Expected growth of the stock
        #
        # Randomness = sigma*sqrt(dt)*Z
        #              Random market movement
        #
        # Result:
        # Simulates one possible stock price movement over the next time step
        paths[t] = paths[t - 1] * np.exp(
            (r - 0.5 * sigma ** 2) * dt
            + sigma * np.sqrt(dt) * Z
        )

    return paths