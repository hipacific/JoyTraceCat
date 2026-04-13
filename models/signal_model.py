import pandas as pd
import numpy as np

class StockSignalModel:
    def __init__(self, data):
        self.data = data

    def moving_average(self, window):
        return self.data['close'].rolling(window=window).mean()

    def rsi(self, period=14):
        delta = self.data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def macd(self, short_window=12, long_window=26, signal_window=9):
        short_ema = self.data['close'].ewm(span=short_window, adjust=False).mean()
        long_ema = self.data['close'].ewm(span=long_window, adjust=False).mean()
        macd = short_ema - long_ema
        signal = macd.ewm(span=signal_window, adjust=False).mean()
        return macd, signal

    def volume_analysis(self):
        # Simple volume analysis
        return self.data['volume'].rolling(window=20).mean()

    def generate_signals(self):
        self.data['MA'] = self.moving_average(window=14)
        self.data['RSI'] = self.rsi(period=14)
        self.data['MACD'], self.data['Signal'] = self.macd()
        self.data['Volume_MA'] = self.volume_analysis()

        # Generating Buy/Sell signals
        self.data['Signal'] = 0
        self.data['Signal'][((self.data['MACD'] > self.data['Signal']) & (self.data['RSI'] < 30))] = 1  # Buy signal
        self.data['Signal'][((self.data['MACD'] < self.data['Signal']) & (self.data['RSI'] > 70))] = -1  # Sell signal
        return self.data

# Example Usage:
# data = pd.DataFrame({'close': [...], 'volume': [...]})  # Replace [...] with actual data
# model = StockSignalModel(data)
# signals = model.generate_signals()