import argparse

from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():

    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Request Summary")
    print("---------------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)
    print("Price:", args.price)

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print(order)

    print("\nOrder executed successfully")


if __name__ == "__main__":
    main()