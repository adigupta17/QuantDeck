## Strategy 1: Moving Average Crossover (Trend Following)
  This strategy assumes that when a short-term trend crosses above a long-term trend, the stock price will keep moving up (a bullish signal), and vice versa for a down trend (a bearish signal).
  
  How it works: Calculate two moving averages on daily closing prices:
  
  Fast Moving Average (e.g., 20-day SMA): Captures short-term price momentum.
  
  Slow Moving Average (e.g., 50-day SMA): Captures long-term trend direction.
  
  Buy Signal: The 20-day SMA crosses above the 50-day SMA ("Golden Cross").
  
  Sell / Short Signal: The 20-day SMA crosses below the 50-day SMA ("Death Cross").


## Strategy 2: Relative Strength Index / RSI (Mean Reversion)
  This strategy assumes that stock prices bounce back to an average level after being pushed too far in one direction by momentum or news.
  
  How it works: The RSI indicator measures the speed and magnitude of recent price changes on a scale from 0 to 100 over a set period (typically 14 days).
  
  Overbought (> 70): The stock has risen too fast and is due for a price drop.
  
  Oversold (< 30): The stock has dropped too fast and is due for a rebound.
  
  Buy Signal: RSI drops below 30 and begins turning upward.
  
  Sell Signal: RSI rises above 70 and begins turning downward.


## Strategy 3: Bollinger Bands (Volatility Breakout / Mean Reversion)
  Bollinger Bands measure market volatility by creating an upper and lower boundary around a moving average.

  How it works: Calculate a 20-day Simple Moving Average (the middle band), then place the upper and lower bands 2 standard deviations away. Since ~95% of price action typically stays within 2 standard deviations, touching or breaking a band indicates an extreme move.

  Mean Reversion Approach:

  Buy Signal: Price touches or drops below the Lower Band (expects price to bounce back to the middle).

  Sell Signal: Price touches or rises above the Upper Band (expects price to fall back to the middle).

## Non Price based strategies:
volume breakout (checking for institutional buying), strategies involving referring to a volatility
