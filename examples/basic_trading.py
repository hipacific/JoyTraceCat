import pandas as pd
import numpy as np

class BasicSignalModel:
    def __init__(self):
        pass

    def analyze_tickers(self, tickers):
        results = []
        for ticker in tickers:
            # Here you would normally fetch the stock data,
            # but we'll generate some dummy data for this example.
            prices = self.fetch_stock_data(ticker)
            signals = self.generate_signals(prices)
            results.append({
                'ticker': ticker,
                'signals': signals
            })
        return results

    def fetch_stock_data(self, ticker):
        # Simulate fetching stock data as a pandas Series
        dates = pd.date_range(start='2026-01-01', periods=100)
        prices = pd.Series(data=np.random.rand(100) * 100, index=dates)
        return prices

    def generate_signals(self, prices):
        signals = []
        moving_average = prices.rolling(window=5).mean()
        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i] > moving_average[i]:
                signals.append('BUY')
            elif prices[i] < moving_average[i]:
                signals.append('SELL')
            else:
                signals.append('HOLD')
        return signals

# Example usage
if __name__ == '__main__':
    model = BasicSignalModel()
    tickers = ['AAPL', 'GOOGL', 'MSFT']
    results = model.analyze_tickers(tickers)
    
    # Formatting output
    for result in results:
        print(f"Ticker: {result['ticker']}")
        for i, signal in enumerate(result['signals']):
            print(f"Date: {pd.date_range(start='2026-01-01', periods=100)[i]:%Y-%m-%d}, Signal: {signal}")
        print()