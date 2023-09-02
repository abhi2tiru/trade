import pandas as pd
import numpy as np

profits=np.zeros(473)
tickers=pd.read_csv('tickers.csv')['tickers'].to_numpy()

ratios=pd.read_csv('mean_ratios.csv')
print(ratios['mean'])