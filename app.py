import streamlit as st
import pandas as pd
import numpy as np

st.title("Sentiment analysis of tweets about us Airlines")
st.sidebar.title("Sentiment analysis of tweets about us Airlines")

st.markdown("This application is a Streamlit dashboard to analyze the sentiment of tweets 🐦")
st.sidebar.markdown("This application is a Streamlit dashboard to analyze the sentiment of tweets 🐦")

DATA_URL=("D:\Study\Third year sem 6\Predictive analysis using statistics\Interactive-Dashboards-Streamlit-Python\Tweets.csv")
@st.cache_data(persist=True)
def load_data():
    data=pd.read_csv(DATA_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data=load_data()
