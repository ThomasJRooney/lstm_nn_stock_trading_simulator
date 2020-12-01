import yfinance as yf
import numpy
from trader import *

class SwingMeanReversion(Stock_Trader):
    def __init__(self, symbol):
        self.symbol = symbol

    RISK_PERCENTAGE = 0.01

    def get_30dma(self):
        data = yf.download(self.symbol, '2020-01-01', '2020-02-09')
        data = data[-30:]
        return numpy.mean(data, axis = None)

    def get_10dma(self):
        data = yf.download(self.symbol, '2020-01-01', '2020-02-09')
        data = data[-10:]
        return numpy.mean(data, axis = None)

    def calculate_weights(self):
        sma_30 = self.get_30dma()
        sma_10 = self.get_10dma()
        raw_weights = (sma_30 - sma_10) / sma_30
        normalized_weights = raw_weights / raw_weights.abs().sum()
        return normalized_weights

    def trade(self):
        while(True):
            return(True)
