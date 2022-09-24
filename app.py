import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import preprocessing
import tweepy

df = pd.read_excel("fo_mktlots.xlsx")

paanch_minute = preprocessing.pichle_5_min(df)

st.sidebar.title("Twitter-Sentiment-Analysis")

time = 'Last 5 minutes count'

if(time == 'Last 5 minutes count'):
    st.header("Previous 5 minutes count")
    st.bar_chart(data = paanch_minute, x = 'keyword' ,y = 'count')
