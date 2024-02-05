import streamlit as st
import pandas as pd
import numpy as np

st.title("Sentiment analysis of tweets about us Airlines")
st.sidebar.title("Sentiment analysis of tweets about us Airlines")

st.markdown("This application is a Steamlit dashboard to analyze the sentiment of tweets 🐦")
st.sidebar.markdown("This application is a Steamlit dashboard to analyze the sentiment of tweets 🐦")

DATA_URL=("/home/rhyme/Desktop/Project/Tweets.csv")
def load_data():
    data=pd.read_csv(DATA_URL)
