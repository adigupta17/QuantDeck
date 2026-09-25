"""
QuantDeck Stock & ETF Universe Configuration
Total Tickers: 60
"""

UNIVERSE = {
    # Sector: Semiconductors & Semiconductor Equipment (Count = 7)
    "NVDA": {"name": "NVIDIA Corp", "sector": "Semiconductors & Semiconductor Equipment"},
    "AMD": {"name": "Advanced Micro Devices Inc", "sector": "Semiconductors & Semiconductor Equipment"},
    "AVGO": {"name": "Broadcom Inc", "sector": "Semiconductors & Semiconductor Equipment"},
    "SKHY": {"name": "SK Hynix Inc", "sector": "Semiconductors & Semiconductor Equipment"},
    "TSM": {"name": "Taiwan Semiconductor Manufacturing", "sector": "Semiconductors & Semiconductor Equipment"},
    "ASML": {"name": "ASML Holding NV", "sector": "Semiconductors & Semiconductor Equipment"},
    "MU": {"name": "Micron Technology Inc", "sector": "Semiconductors & Semiconductor Equipment"},

    # Sector: Software & IT Services (Count = 8)
    "META": {"name": "Meta Platforms Inc", "sector": "Software & IT Services"},
    "MSFT": {"name": "Microsoft Corp", "sector": "Software & IT Services"},
    "GOOG": {"name": "Alphabet Inc", "sector": "Software & IT Services"},
    "NFLX": {"name": "Netflix Inc", "sector": "Software & IT Services"},
    "MA": {"name": "Mastercard Inc", "sector": "Software & IT Services"},
    "BABA": {"name": "Alibaba Group Holding", "sector": "Software & IT Services"},
    "PANW": {"name": "Palo Alto Networks Inc", "sector": "Software & IT Services"},
    "FTNT": {"name": "Fortinet Inc", "sector": "Software & IT Services"},

    # Sector: Computers, Phones & Household Electronics (Count = 3)
    "AAPL": {"name": "Apple Inc", "sector": "Computers, Phones & Household Electronics"},
    "SMCI": {"name": "Super Micro Computer Inc", "sector": "Computers, Phones & Household Electronics"},
    "DELL": {"name": "Dell Technologies Inc", "sector": "Computers, Phones & Household Electronics"},

    # Type: ETFs (Count = 6)
    "SPY": {"name": "State Street SPDR S&P 500 ETF", "sector": "ETF"},
    "QQQ": {"name": "Invesco QQQ Trust", "sector": "ETF"},
    "IWM": {"name": "iShares Russell 2000 ETF", "sector": "ETF"},
    "SOXX": {"name": "iShares Semiconductor ETF", "sector": "ETF"},
    "SCHD": {"name": "Schwab US Dividend Equity ETF", "sector": "ETF"},
    "XOVR": {"name": "ERShares Entrepreneurs ETF", "sector": "ETF"},

    # Sector: Banking Services (Count = 3)
    "JPM": {"name": "JPMorgan Chase & Co", "sector": "Banking Services"},
    "WFC": {"name": "Wells Fargo & Co", "sector": "Banking Services"},
    "BAC": {"name": "Bank of America Corp", "sector": "Banking Services"},

    # Sector: Investment Banking & Investment Services (Count = 3)
    "GS": {"name": "Goldman Sachs Group Inc", "sector": "Investment Banking & Investment Services"},
    "MS": {"name": "Morgan Stanley", "sector": "Investment Banking & Investment Services"},
    "BX": {"name": "Blackstone Inc", "sector": "Investment Banking & Investment Services"},

    # Sector: Oil & Gas (Count = 3)
    "VIST": {"name": "Vista Energy SAB de CV", "sector": "Oil & Gas"},
    "CVX": {"name": "Chevron Corp", "sector": "Oil & Gas"},
    "XOM": {"name": "Exxon Mobil Corp", "sector": "Oil & Gas"},

    # Sector: Automobiles & Auto Parts (Count = 3)
    "TSLA": {"name": "Tesla Inc", "sector": "Automobiles & Auto Parts"},
    "F": {"name": "Ford Motor Co", "sector": "Automobiles & Auto Parts"},
    "GM": {"name": "General Motors Co", "sector": "Automobiles & Auto Parts"},

    # Sector: Pharmaceuticals (Count = 5)
    "MRNA": {"name": "Moderna Inc", "sector": "Pharmaceuticals"},
    "ABBV": {"name": "AbbVie Inc", "sector": "Pharmaceuticals"},
    "REGN": {"name": "Regeneron Pharmaceuticals Inc", "sector": "Pharmaceuticals"},
    "LLY": {"name": "Eli Lilly and Co", "sector": "Pharmaceuticals"},
    "JNJ": {"name": "Johnson & Johnson", "sector": "Pharmaceuticals"},

    # Sector: Aerospace & Defense (Count = 2)
    "LMT": {"name": "Lockheed Martin Corp", "sector": "Aerospace & Defense"},
    "RKLB": {"name": "Rocket Lab USA Inc", "sector": "Aerospace & Defense"},

    # Sector: Diversified Retail (Count = 2)
    "AMZN": {"name": "Amazon.com Inc", "sector": "Diversified Retail"},
    "COST": {"name": "Costco Wholesale Corp", "sector": "Diversified Retail"},

    # Sector: Electronic Equipment & Parts (Count = 2)
    "GLW": {"name": "Corning Inc", "sector": "Electronic Equipment & Parts"},
    "AAOI": {"name": "Applied Optoelectronics Inc", "sector": "Electronic Equipment & Parts"},

    # Sector: Machinery, Equipment & Components (Count = 2)
    "CAT": {"name": "Caterpillar Inc", "sector": "Machinery, Equipment & Components"},
    "SYM": {"name": "Symbotic Inc", "sector": "Machinery, Equipment & Components"},

    # Sector: Professional & Commercial Services (Count = 2)
    "V": {"name": "Visa Inc", "sector": "Professional & Commercial Services"},
    "CIRC": {"name": "Circle SpA", "sector": "Professional & Commercial Services"},

    # Single-Stock Sectors
    "VTGN": {"name": "VistaGen Therapeutics Inc", "sector": "Biotechnology & Medical Research"},
    "PG": {"name": "Procter & Gamble Co", "sector": "Personal & Household Products & Services"},
    "USAR": {"name": "USA Rare Earth Inc", "sector": "Metals & Mining"},
    "SPCX": {"name": "Space Exploration Technologies", "sector": "Telecommunications Services"},
    "UPS": {"name": "United Parcel Service Inc", "sector": "Freight & Logistics Services"},
    "UNH": {"name": "UnitedHealth Group Inc", "sector": "Healthcare Providers & Services"},
    "WMT": {"name": "Walmart Inc", "sector": "Food & Drug Retailing"},
    "PEP": {"name": "PepsiCo Inc", "sector": "Beverages"},
    "COIN": {"name": "Coinbase Global Inc", "sector": "Financial Technology (Fintech) & Infrastructure"}
}

# Helper list of all tickers for quick iteration/dropdowns
TICKER_LIST = sorted(list(UNIVERSE.keys()))
