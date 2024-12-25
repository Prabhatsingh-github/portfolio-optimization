# Portfolio Optimization Project

This project demonstrates portfolio optimization using Modern Portfolio Theory (MPT). The goal is to optimize a portfolio of assets to minimize risk (volatility) for a given target return, and to calculate the **Efficient Frontier**, which represents the set of optimal portfolios offering the best risk-return tradeoff.

## Features

- **Portfolio Performance Calculation**: Computes portfolio return and risk (standard deviation).
- **Efficient Frontier**: Visualizes the risk-return tradeoff of optimal portfolios.
- **Optimization**: Uses `scipy.optimize` to find the optimal portfolio weights.
- **Custom Constraints**: Allows flexibility for long-only portfolios or custom constraints.

---

## Requirements

This project requires Python 3.7 or higher and the following libraries:

- **NumPy**: For numerical calculations.
- **Pandas**: For handling and analyzing financial data.
- **SciPy**: For optimization routines.
- **Matplotlib**: For visualizing the efficient frontier.

Install the required packages using:

```bash
pip install numpy pandas scipy matplotlib
```

---

## How to Use

Follow these steps to use the portfolio optimization script:

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/portfolio-optimization
cd portfolio-optimization
```
2. **Prepare the script:**
- Open the `portfolio_optimization.py` file in your code editor.
- Replace the `returns_data` section (which generates random return data) with your own historical return data. For example:
```bash
returns_data = pd.read_csv('your_historical_data.csv').pct_change().dropna()
```
3. **Run the script**: Execute the script using python:
```bash
python portfolio_optimization.py
```
4. **Analyse the results:**
- The script will calculate the optimal portfolio weights and generate a plot of the **Efficient Frontier**.
- Review the output for insights into the optimal risk-return tradeoff.
5. **Optional customization:**
- Modify constraints in the `optimize_portfolio` function to include short-selling, sector allocation limits, or other requirements.
- Add additional analysis like the **Capital Market Line (CML)** by incorporating a risk-free rate.

---

## Code Overview

**Key Functions:**
1. `portfolio_performance(weights, mean_returns, cov_matrix)`
Calculates the expected return and volatility of a portfolio given weights, mean returns, and the covariance matrix.

2. `minimize_volatility(weights, mean_returns, cov_matrix)`
A helper function for the optimizer to minimize portfolio volatility.

3. `optimize_portfolio(mean_returns, cov_matrix, target_return)`
Finds the optimal portfolio weights for a given target return.

4. `efficient_frontier(mean_returns, cov_matrix, returns_range)`
Computes the efficient frontier by solving for optimal portfolios over a range of target returns.

---

## References

- **Modern Portfolio Theory (MPT)**: [Investopedia - Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- **SciPy Documentation**: [SciPy Optimization Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html)
- **Efficient Frontier Explanation**: [Efficient Frontier on Investopedia](https://www.investopedia.com/terms/e/efficientfrontier.asp)

---

## Contact

If you have any questions, feedback, or suggestions, feel free to reach out:

- **Name**: Prabhat Singh
- **Email**: prabhatsingh10052000@example.com
- **GitHub**: [Prabhatsingh-github](https://github.com/Prabhatsingh-github)
- **LinkedIn**: [prabhat-singh1a](https://www.linkedin.com/in/prabhat-singh1a)

---

