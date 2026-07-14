"""
OPTION PRICER

This file prices European options using Monte Carlo simulation.

Methods:
- European Call Option
- European Put Option

Process:
1. Take the final simulated stock prices.
2. Calculate option payoffs.
3. Average the payoffs.
4. Discount back to today's value.

Output:
Estimated fair value of the option.
"""
import numpy as np

# Calculate the Monte Carlo price of a European call option.
def european_call(paths, K, r, T):

    final_prices = paths[-1]

    payoffs = np.maximum(final_prices - K, 0)

    price = np.exp(-r * T) * np.mean(payoffs)

    return price


def european_put(paths, K, r, T):

    final_prices = paths[-1]

    payoffs = np.maximum(K - final_prices, 0)

    price = np.exp(-r * T) * np.mean(payoffs)

    return price