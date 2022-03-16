import pandas as pd
import numpy as np


class ComputeReturns:

    def __init__(self, prices_df: pd.DataFrame, ohlcv: dict):


class Indicator:

    def __init__(self, prices_df: pd.DataFrame, ohlcv: dict):
        self.df = prices_df
        self.open = ohlcv['open']
        self.high = ohlcv['high']
        self.low = ohlcv['low']
        self.close = ohlcv['close']
        self.volume = ohlcv['volume']

    def get_df(self):
        return self.df

    def simple_moving_average(self, n):
        """
        Calculate the moving average for the given data.
        :return:
        """
        sma = pd.Series(self.df[self.close].rolling(window=n, min_periods=n).mean(), name='SMA_close_' + str(n))
        self.df = self.df.join(sma)

    def exponential_moving_average(self, n):
        """
        Calculate the moving average for the given data.
        :return:
        """
        ema = pd.Series(self.df[self.close].ewm(span=n, min_periods=n).mean(), name='EMA_close_' + str(n))
        self.df =  self.df.join(ema)




