import re
import requests
import pandas as pd
from python.tools.credentials import Credentials


class AVQuery(Credentials):

    def __init__(self):
        Credentials.__init__(self)
        self.credentials_api_something3()
        self.email = getattr(self, 'ALPHAVANTAGE_PAU')['email']
        self.api_key = getattr(self, 'ALPHAVANTAGE_PAU')['api_key']
        self.root_url = 'https://www.alphavantage.co/query'

        self.function = {'function': None}
        self.symbol = {'symbol': None}
        self.interval = {'interval': None}
        self.adjusted = {'adjusted': 'true'}
        self.outputsize = {'outputsize': 'compact'}
        self.datatype = {'datatype': 'json'}

    def intraday_data(self, **kwargs):
        for kwarg, arg in kwargs.items():
            if re.search('^function$', kwarg):
                self.function = {kwarg: arg}
            elif re.search('^symbol$', kwarg):
                self.symbol = {kwarg: arg}
            elif re.search('^interval$', kwarg):
                self.interval = {kwarg: arg}
            elif re.search('^adjusted$', kwarg):
                self.adjusted = {kwarg: arg}
            elif re.search('^outputsize$', kwarg):
                self.outputsize = {kwarg: arg}
            elif re.search('^datatype$', kwarg):
                self.datatype = {kwarg: arg}
            else:
                pass

        url = f"{self.root_url}?" \
              f"{list(self.function.keys())[0]}={self.function['function']}&" \
              f"{list(self.symbol.keys())[0]}={self.symbol['symbol']}&" \
              f"{list(self.interval.keys())[0]}={self.interval['interval']}&" \
              f"{list(self.adjusted.keys())[0]}={self.adjusted['adjusted']}&" \
              f"{list(self.outputsize.keys())[0]}={self.outputsize['outputsize']}&" \
              f"{list(self.datatype.keys())[0]}={self.datatype['datatype']}&" \
              f"apikey={self.api_key}"

        r = requests.get(url)
        data = r.json()
        return data

    def daily_data(self, **kwargs):
        for kwarg, arg in kwargs.items():
            if re.search('^function$', kwarg):
                self.function = {kwarg: arg}
            elif re.search('^symbol$', kwarg):
                self.symbol = {kwarg: arg}
            elif re.search('^adjusted$', kwarg):
                self.adjusted = {kwarg: arg}
            elif re.search('^outputsize$', kwarg):
                self.outputsize = {kwarg: arg}
            elif re.search('^datatype$', kwarg):
                self.datatype = {kwarg: arg}
            else:
                pass

        url = f"{self.root_url}?" \
              f"{list(self.function.keys())[0]}={self.function['function']}&" \
              f"{list(self.symbol.keys())[0]}={self.symbol['symbol']}&" \
              f"{list(self.adjusted.keys())[0]}={self.adjusted['adjusted']}&" \
              f"{list(self.outputsize.keys())[0]}={self.outputsize['outputsize']}&" \
              f"{list(self.datatype.keys())[0]}={self.datatype['datatype']}&" \
              f"apikey={self.api_key}"

        r = requests.get(url)
        raw_data = r.json()

        data = self.processing(raw_data)

        return data

    @staticmethod
    def processing(d: dict):

        # d['Meta Data']['1. Information']
        # d['Meta Data']['2. Symbol']
        # d['Meta Data']['3. Last Refreshed']
        # d['Meta Data']['4. Output Size']
        # d['Meta Data']['5. Time Zone']

        price_data = list(d.keys())[1]
        tmp = [d[price_data][x] for x in d[price_data]]
        for x, y in zip(d[price_data], tmp):
            y['time'] = x
        df_data = pd.DataFrame(tmp)

        df_data.columns = [d['Meta Data']['2. Symbol'] + '_' + re.findall(r'[a-z]+', i)[0] for i in df_data.columns]

        df_data[f"{d['Meta Data']['2. Symbol']}_time"] = pd.to_datetime(df_data[f"{d['Meta Data']['2. Symbol']}_time"], format='%Y-%m-%d')

        df_data.set_index(f"{d['Meta Data']['2. Symbol']}_time", drop=True, inplace=True)

        return df_data


avq = AVQuery()
daily = avq.daily_data(symbol='IBM', function='TIME_SERIES_DAILY', outputsize='full')
daily2 = avq.daily_data(symbol='XOM', function='TIME_SERIES_DAILY', outputsize='full')
