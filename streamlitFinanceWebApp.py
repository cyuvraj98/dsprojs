import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and volume of Google!
    
""")
#Ticker Symbol is an abbrev used to uniquely identify publicly traded shares of a particular stock
tickerSymbol = 'GOOGL'

#Get data ON the 'GOOGL' ticker
tickerData = yf.Ticker(tickerSymbol)

#get historical prices for this ticker ('GOOGL')
tickerDf = tickerData.history(period = "1d", start = "2010-5-31", end = "2020-5-31")
# Open High Low Close Volume Dividends Stock Splits
# Finance knowledge: A stock split increases the number of shares in a company, decreasing the stock price of each share, making the stocks seem more affordable
st.write("""
   ## Closing Price      
""")
st.line_chart(tickerDf.Close)
st.write("""
   ## Volume Price      
""")
st.line_chart(tickerDf.Volume)
