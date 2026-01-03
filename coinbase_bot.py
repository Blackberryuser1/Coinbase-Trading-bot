import os
import ccxt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COINBASE_API_KEY")
API_SECRET = os.getenv("COINBASE_API_SECRET")
API_PASSPHRASE = os.getenv("COINBASE_API_PASSPHRASE")  # if required by your key setup
TESTNET = os.getenv("COINBASE_SANDBOX", "true").lower() in ("1", "true", "yes")

# ccxt id is 'coinbase' for Coinbase Advanced Trade API
exchange = ccxt.coinbase({
    "apiKey": API_KEY,
    "secret": API_SECRET,
    "password": API_PASSPHRASE,
    "enableRateLimit": True,
})

# Optional: if you configure sandbox URL manually (depends on your account)
if TESTNET:
    # Check ccxt docs for latest sandbox support, this is placeholder
    exchange.set_sandbox_mode(True)

exchange.load_markets()

def place_coinbase_order(side: str, symbol: str, amount: float):
    """
    Place a crypto market order on Coinbase.
    symbol example: 'BTC/USDT', 'ETH/USD'
    amount is in base asset units.
    """
    if side not in ["buy", "sell"]:
        raise ValueError("Invalid side for Coinbase order")

    order = exchange.create_order(
        symbol=symbol,
        type="market",
        side=side,
        amount=amount
    )
    return order