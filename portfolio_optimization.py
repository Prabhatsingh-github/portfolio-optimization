import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Function to calculate portfolio performance
def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.dot(weights, mean_returns)
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, std

# Function to minimize portfolio volatility
def minimize_volatility(weights, mean_returns, cov_matrix):
    return portfolio_performance(weights, mean_returns, cov_matrix)[1]

# Function for the optimization process
def optimize_portfolio(mean_returns, cov_matrix, target_return):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)
    
    # Initial guess for weights
    initial_weights = num_assets * [1.0 / num_assets]
    
    # Constraints: Sum of weights = 1, and portfolio return = target_return
    constraints = (
        {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},  # Sum of weights = 1
        {'type': 'eq', 'fun': lambda weights: portfolio_performance(weights, mean_returns, cov_matrix)[0] - target_return}
    )
    
    # Bounds for weights: between 0 and 1 (long-only portfolio)
    bounds = tuple((0, 1) for _ in range(num_assets))
    
    result = minimize(minimize_volatility, initial_weights, args=args, method='SLSQP', bounds=bounds, constraints=constraints)
    return result

# Function to calculate the Efficient Frontier
def efficient_frontier(mean_returns, cov_matrix, returns_range):
    efficient_portfolios = []
    for target_return in returns_range:
        efficient_portfolios.append(optimize_portfolio(mean_returns, cov_matrix, target_return))
    return efficient_portfolios

# Generate random portfolio data (for demonstration)
np.random.seed(42)
num_assets = 4
num_data_points = 1000
returns_data = np.random.randn(num_data_points, num_assets) / 100  # Simulated daily returns

# Calculate mean returns and covariance matrix
mean_returns = returns_data.mean(axis=0) * 252  # Annualized returns
cov_matrix = np.cov(returns_data.T) * 252      # Annualized covariance matrix

# Define target returns for the efficient frontier
target_returns = np.linspace(mean_returns.min(), mean_returns.max(), 50)

# Calculate Efficient Frontier
efficient_portfolios = efficient_frontier(mean_returns, cov_matrix, target_returns)

# Extract weights, returns, and volatilities for plotting
frontier_volatility = [result.fun for result in efficient_portfolios]
frontier_returns = target_returns

# Plot Efficient Frontier
plt.figure(figsize=(10, 6))
plt.scatter(frontier_volatility, frontier_returns, c=frontier_returns / np.array(frontier_volatility), cmap='viridis', marker='x')
plt.title('Efficient Frontier')
plt.xlabel('Volatility (Standard Deviation)')
plt.ylabel('Return')
plt.colorbar(label='Sharpe Ratio')
plt.grid(True)
plt.show()
