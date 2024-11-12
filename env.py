import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical stock data
symbol = ('2883.tw')
data = yf.download(symbol, start='2023-11-08', end='2024-11-08', progress=False)