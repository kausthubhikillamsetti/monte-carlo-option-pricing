"""
STATISTICS

This file contains functions used to analyze
Monte Carlo simulation results.

Examples:
- Mean payoff
- Standard deviation
- Confidence intervals
- Simulation summary statistics

Purpose:
Measure the accuracy and stability of simulation outputs.
"""
import numpy as np


def confidence_interval(payoffs):

    mean = np.mean(payoffs)

    std = np.std(payoffs)

    n = len(payoffs)

    margin = 1.96 * std / np.sqrt(n)

    lower = mean - margin
    upper = mean + margin

    return lower, upper


def simulation_summary(payoffs):

    print("\nSimulation Statistics")

    print("----------------------")

    print("Mean Payoff:", np.mean(payoffs))
    print("Std Dev:", np.std(payoffs))
    print("Minimum:", np.min(payoffs))
    print("Maximum:", np.max(payoffs))

import numpy as np

def probability_profit(final_prices, K):

    profitable = np.sum(final_prices > K)

    probability = profitable / len(final_prices)

    return probability
def value_at_risk(final_prices, confidence=95):

    percentile = 100 - confidence

    var = np.percentile(
        final_prices,
        percentile
    )

    return var
def expected_shortfall(
        final_prices,
        confidence=95):

    var = np.percentile(
        final_prices,
        100 - confidence
    )

    tail = final_prices[
        final_prices <= var
    ]

    return np.mean(tail)

import numpy as np

def probability_of_profit(
        final_prices,
        strike,
        premium):

    breakeven = strike + premium

    profitable = np.sum(
        final_prices > breakeven
    )

    return profitable / len(final_prices)