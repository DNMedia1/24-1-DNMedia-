"""Command-line interface for the stock analysis tool."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Stock analysis CLI")
    parser.add_argument("symbol", help="Ticker symbol to analyze")
    args = parser.parse_args()
    # Placeholder: load data and run analysis
    print(f"Analyzing {args.symbol} ...")


if __name__ == "__main__":
    main()
