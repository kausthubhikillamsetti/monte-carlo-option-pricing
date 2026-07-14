"""
MAIN PROGRAM

This file runs the entire Monte Carlo simulation.

Workflow:
1. Generate thousands of possible stock price paths.
2. Price European call and put options using those paths.
3. Display simulation results.
4. Plot stock paths and final price distributions.

Run this file to execute the project.
"""
from stock_generator import generate_paths

from option_price import (
    european_call,
    european_put
)

from visual import (
    plot_paths,
    plot_histogram
)

import numpy as np

# Parameters

#current stock price
S0 = 210.96
#strike price
K = 220
#risk-free interest rate
r = 0.04
#volatility (uncertainty)
sigma = 0.313
#time to maturity (years)
T = 0.1836
# #of time intervals -> there are 252 trading days in a year
steps = 49
#of simulated futures
n_paths = 10000


# Generate paths
paths = generate_paths(
    S0,
    r,
    sigma,
    T,
    steps,
    n_paths
)


# Price options
call_price = european_call(
    paths,
    K,
    r,
    T
)

put_price = european_put(
    paths,
    K,
    r,
    T
)


print("\nEuropean Option Prices")

print("-----------------------")

print(f"Call Price = {call_price:.4f}")

print(f"Put Price  = {put_price:.4f}")


# Visualization
plot_paths(paths[:, :20])

plot_histogram(paths[-1])

from stats import probability_profit
prob_profit = probability_profit(
    paths[-1],
    K
)

print(
    f"Probability Option Expires In-The-Money: {prob_profit:.2%}"
)
from stats import value_at_risk
var95 = value_at_risk(
    paths[-1],
    confidence=95
)

print(
    f"95% VaR Stock Price = {var95:.2f}"
)
# Probability of Profit (POP)
# Measures the percentage of simulated futures where
# the stock finishes above the option's break-even price.
# Break-even = Strike Price + Option Premium

# Example:
# Strike = 105
# Premium = 8.11
# Break-even = 113.11

# POP answers: "What is the chance I actually make money?"
from stats import (
    probability_profit,
    probability_of_profit,
    value_at_risk,
    expected_shortfall
)

call_price = european_call(
    paths,
    K,
    r,
    T
)
pop = probability_of_profit(
    paths[-1],
    K,
    call_price
)
print(
    f"Probability of Profit: {pop:.2%}"
)