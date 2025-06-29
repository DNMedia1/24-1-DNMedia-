"""Analysis module.

Contains functions for basic statistical analysis of stock data.
"""

import pandas as pd


def moving_average(series: pd.Series, window: int) -> pd.Series:
    """Return moving average of the series."""
    return series.rolling(window=window).mean()
