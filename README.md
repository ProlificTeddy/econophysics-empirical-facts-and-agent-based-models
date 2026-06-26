# Econophysics: Empirical Facts and Agent-Based Models

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Paper](https://img.shields.io/badge/Research-Paper-green)](https://arxiv.org/pdf/0909.1974v2)

Welcome to the implementation of the concepts discussed in the research paper **"Econophysics: Empirical Facts and Agent-Based Models"** by Anirban Chakraborti, Ioane Muni Toke, Marco Patriarca, and Frederic Abergel. This repository provides a Python-based implementation of the key models and empirical analyses outlined in the paper, enabling researchers and enthusiasts to explore the fascinating intersection of economics and physics.

---

## 📜 Overview of the Paper

Econophysics is an interdisciplinary field that applies methods from physics to solve problems in economics and finance. This paper provides a comprehensive review of empirical findings and theoretical models in Econophysics, focusing on:

1. **Empirical Facts**: Statistical properties of financial time series, such as fat-tailed distributions, volatility clustering, and autocorrelation. The paper also explores order book dynamics and asset correlations using techniques like random matrix theory and graph theory.
   
2. **Agent-Based Models**: Simulations of financial markets using multi-agent systems. The paper highlights three key areas:
   - **Order-Driven Markets**: Models inspired by behavioral finance and market microstructure theory.
   - **Kinetic Theory Models**: Explaining wealth distribution dynamics.
   - **Game Theory Models**: Including the classic minority game and related problems.

This repository implements a subset of these models and empirical analyses, providing tools to reproduce key findings and experiment with agent-based simulations.

---

## 🚀 How It Works

The implementation is divided into two main components:

### 1. **Empirical Analysis**
   - **Stylized Facts**: Analyze financial time series data to identify statistical properties such as fat tails, volatility clustering, and autocorrelation.
   - **Order Book Dynamics**: Simulate and study the statistical properties of order books in financial markets.
   - **Asset Correlations**: Use random matrix theory and graph theory to explore correlations between financial assets.

### 2. **Agent-Based Models**
   - **Order-Driven Market Simulation**: Implement agent-based models of financial markets where agents interact through an order-driven mechanism.
   - **Wealth Distribution**: Simulate kinetic theory models to study the dynamics of wealth distribution in a population.
   - **Minority Game**: Implement game theory-based models to study decision-making in competitive environments.

The Python script `implementation.py` provides modular functions for each of these components, allowing users to run simulations, analyze data, and visualize results.

---

## 🛠️ Usage Instructions

### Prerequisites

Ensure you have Python 3.8 or later installed on your system. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Running the Script

The main script `implementation.py` includes functions for both empirical analysis and agent-based modeling. Below is a step-by-step guide to using the script:

#### 1. **Empirical Analysis**
To analyze financial time series data:
```bash
python implementation.py --mode empirical --data_path path/to/your/data.csv
```
Arguments:
- `--mode`: Set to `empirical` for statistical analysis of financial data.
- `--data_path`: Path to the CSV file containing financial time series data.

#### 2. **Order-Driven Market Simulation**
To simulate an order-driven market:
```bash
python implementation.py --mode order_market --agents 100 --steps 1000
```
Arguments:
- `--mode`: Set to `order_market` for simulating order-driven markets.
- `--agents`: Number of agents in the simulation.
- `--steps`: Number of simulation steps.

#### 3. **Wealth Distribution Simulation**
To simulate wealth distribution dynamics:
```bash
python implementation.py --mode wealth_distribution --agents 100 --iterations 1000
```
Arguments:
- `--mode`: Set to `wealth_distribution` for simulating wealth dynamics.
- `--agents`: Number of agents in the population.
- `--iterations`: Number of iterations for the simulation.

#### 4. **Minority Game Simulation**
To simulate the minority game:
```bash
python implementation.py --mode minority_game --agents 101 --rounds 500
```
Arguments:
- `--mode`: Set to `minority_game` for simulating the minority game.
- `--agents`: Number of agents participating in the game.
- `--rounds`: Number of rounds in the simulation.

### Output
The script generates visualizations and data files for each simulation or analysis. Outputs are saved in the `results/` directory.

---

## 📂 Project Structure

```
econophysics/
├── implementation.py    # Main Python script
├── requirements.txt     # Python dependencies
├── data/                # Directory for input datasets
├── results/             # Directory for output results and visualizations
├── README.md            # Project documentation
```

---

## 📈 Example Usage

### Empirical Analysis
```bash
python implementation.py --mode empirical --data_path data/financial_data.csv
```
Output: Visualizations of fat tails, volatility clustering, and autocorrelation saved in `results/`.

### Order-Driven Market Simulation
```bash
python implementation.py --mode order_market --agents 100 --steps 1000
```
Output: Time series of market prices and order book states saved in `results/`.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the implementation or add new features, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or feedback, please reach out via GitHub issues or email.

Happy exploring the fascinating world of Econophysics! 🌍✨