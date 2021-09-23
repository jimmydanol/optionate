import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("This is the Nonsense")

st.header("This is a Cedar Beeters")

st.subheader("Subheader")
st.write("This is regular text")

'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
st.dataframe(df)

st.sidebar.title("Options")

option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'wallstreetbets', 'stocktwits', 'chart', 'pattern'))

if option == 'stocktwits':
    pass
    r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/AAPL.json")

    data = r.json()

    for message in data['messages']:
        st.write(message['body'])
        st.write(message['created_at'])
        st.write(message['user']['username'])

    

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)