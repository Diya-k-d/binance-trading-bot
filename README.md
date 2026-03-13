# Binance Futures Testnet Trading Bot

## Setup

1. Install dependencies

pip install -r requirements.txt

2. Add API keys

Create a .env file:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key

## Run MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

## Run LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000

Logs will be saved in trading_bot.log
