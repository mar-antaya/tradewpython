import alpaca_trade_api as tradeapi

# Authenticate the API using your API Key and Secret
API_KEY = 'api-key'  # Replace with your API key
API_SECRET = 'api-secret'  # Replace with your API secret
BASE_URL = 'https://paper-api.alpaca.markets'  # Paper trading endpoint

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Check Account Information
account = api.get_account()
print("Account Cash Balance:", account.cash)

# Place a Paper Trade Order (Buy Example)
# Let's buy 1 share of Apple (AAPL)
api.submit_order(
    symbol='AAPL',  # Stock Symbol (Apple in this case)
    qty=1,  # Number of shares to buy
    side='buy',  # Buy action
    type='market',  # Market order (executes immediately)
    time_in_force='gtc'  # Good-Til-Canceled
)
print("Buy Order Submitted for AAPL!")

# Check Open Orders
open_orders = api.list_orders(status='open')
if open_orders:
    print("Open Orders:")
    for order in open_orders:
        print(f"Order ID: {order.id} - {order.side} {order.qty} of {order.symbol} at {order.created_at}")
else:
    print("No open orders.")

# Check Positions (Current Holdings)
positions = api.list_positions()
if positions:
    print("Current Positions:")
    for position in positions:
        print(f"Symbol: {position.symbol} | Quantity: {position.qty} shares")
else:
    print("No positions held.")

# Sell the Stock (Example)
api.submit_order(
    symbol='AAPL',  # Stock Symbol
    qty=1,  # Number of shares to sell
    side='sell',  # Sell action
    type='market',  # Market order
    time_in_force='gtc'  # Good-Til-Canceled
)
print("Sell Order Submitted for AAPL!")
