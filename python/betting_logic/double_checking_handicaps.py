import numpy as np
import pandas as pd

a = []
b = []

for i in range(0, 8):
    for j in range(0, 8):
        a.append(i)
        b.append(j)

ar = np.array(a)
br = np.array(b)

result_H_negative_1point5 = pd.DataFrame(data={'a': ar, 'b': (br-1.5), 'winner': np.maximum(ar, (br-1.5))})
result_H_negative_2 = pd.DataFrame(data={'a': ar, 'b': (br-2), 'winner': np.maximum(ar, (br-2))})


def outcome(df, side):

    if side == 'H(-1.5) is LAY':
        for idx in df.index:
            if df.loc[idx, 'a'] > df.loc[idx, 'b']:
                df.loc[idx, 'winner'] = 'LAY'
            elif df.loc[idx, 'a'] < df.loc[idx, 'b']:
                df.loc[idx, 'winner'] = '---'
            else:
                df.loc[idx, 'winner'] = 'LAY'

    if side == 'H(-2) is BACK':
        for idx in df.index:
            if df.loc[idx, 'a'] > df.loc[idx, 'b']:
                df.loc[idx, 'winner'] = '---'
            elif df.loc[idx, 'a'] < df.loc[idx, 'b']:
                df.loc[idx, 'winner'] = 'BACK'
            else:
                df.loc[idx, 'winner'] = '---'


outcome(result_H_negative_1point5, 'H(-1.5) is LAY')
outcome(result_H_negative_2, 'H(-2) is BACK')
