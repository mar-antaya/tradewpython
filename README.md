```markdown
# 🐂 Alpaca Paper Trading Script

This Python script demonstrates basic usage of the [Alpaca API](https://alpaca.markets/) for paper trading, including checking your account balance, placing buy/sell orders, checking open orders, and viewing current positions.

## 🔧 Prerequisites

- Python 3.7+
- An Alpaca account with API credentials
- `alpaca-trade-api` Python package

Install the required package using:

```bash
pip install alpaca-trade-api
```

## 🚀 Getting Started

1. **Clone or copy the script**.
2. **Replace** the placeholder values with your actual API credentials:

```python
API_KEY = 'your-api-key'
API_SECRET = 'your-api-secret'
```

3. **Run the script**:

```bash
python your_script_name.py
```

## 💼 What the Script Does

- Authenticates using your Alpaca API key and secret.
- Prints your cash balance.
- Buys 1 share of Apple Inc. (AAPL).
- Prints open orders.
- Displays current stock positions.
- Sells the previously bought share.

## ⚠️ Disclaimer

This script uses Alpaca's **paper trading** environment. No real money is involved. Ensure your actions comply with financial regulations and test responsibly.
```
