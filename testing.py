import numpy as np
from python.apis.alphavantage import AVQuery
# from indicators import Indicator


avq = AVQuery()
df = avq.daily_data(symbol='IBM', function='TIME_SERIES_DAILY', outputsize='full')
df = df.astype('f8')
df.sort_index(ascending=True, inplace=True)

df['ret_open'] = df['BMW.DEX_open'].pct_change()
df['ret_high'] = df['BMW.DEX_high'].pct_change()
df['ret_low'] = df['BMW.DEX_low'].pct_change()
df['ret_close'] = df['BMW.DEX_close'].pct_change()
df['ret_volume'] = df['BMW.DEX_volume'].pct_change()

ohlcv_mapping = {
    'open': 'BMW.DEX_open',
    'high': 'BMW.DEX_high',
    'low': 'BMW.DEX_low',
    'close': 'BMW.DEX_close',
    'volume': 'BMW.DEX_volume'
}

bmw_indicators = Indicator(prices_df=df, ohlcv=ohlcv_mapping)

bmw_indicators.simple_moving_average(20)

# arr1 = np.array(d['VWRL.AMS_close']).astype(np.float64)

