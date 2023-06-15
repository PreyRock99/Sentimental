import pandas as pd
import numpy as np
import streamlit as st 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import plotly.express as px 
import matplotlib.pyplot as plt
import dotenv
from dotenv import load_dotenv
import os
global data

load_dotenv()

print(os.getenv('HUGGINGFACE_API'))


st.title('Sentiment Analysis Tool')

st.subheader('Vader Sentiment')

text = st.text_input('Enter a comment')
click=st.button('Compute')

print(text)

def senti(text):
    obj=SentimentIntensityAnalyzer()
    senti_dict=obj.polarity_scores(text)
    print(senti_dict)
    if senti_dict['compound']>=0.05:
        st.write("😁 Positive")
    elif senti_dict['compound']<=-0.05:
        st.write("😥 Negative")
    else:
        st.write("🙂 Neutral")
        
if click:
    senti(text)


st.header("Emotional synthesis ")

import requests

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": "Bearer " + st.secrets["Huggingface"]}
sentence = st.text_input('Enter your text')
click=st.button("calculate")


def query(sentence):
	response = requests.post(API_URL, headers=headers, json=sentence)
	return response.json()




output=query({
     "inputs": sentence
})
json_data = output

labels = [item['label'] for item in json_data[0]]
scores = [item['score'] for item in json_data[0]]

data = {'Label': labels, 'Score': scores}
df = pd.DataFrame(data)
emotion=df.iloc[0]

st.metric("Emotion",emotion['Label'],emotion['Score'])
graph=st.selectbox("Graphs",["Bar","Datagram","line"])



click=st.button("Click to plot graph")
if click:
    if graph=='line':
     st.line_chart(df)
    elif graph=='Datagram':
     st.dataframe(df)
    else:
       st.bar_chart(df)
