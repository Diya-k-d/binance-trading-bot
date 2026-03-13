# Binance Futures Testnet Trading Bot

A Python CLI-based trading bot that interacts with the Binance Futures Testnet API to place MARKET and LIMIT orders.

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL positions
- Command-line interface (CLI) input
- Input validation for order parameters
- Logging of API requests and responses
- Modular code structure for maintainability

## Project Structure

trading_bot/
│
├── bot
│   ├── client.py        # Binance API client
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
