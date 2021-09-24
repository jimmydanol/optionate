import config 
import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# st.title("This is the Nonsense")

# st.header("This is a Cedar Beeters")

# st.subheader("Subheader")
# st.write("This is regular text")

# '''
# # This is the document title

# This is some _markdown_.
# '''

df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
# st.dataframe(df)

st.sidebar.title("Options")

option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'wallstreetbets', 'stocktwits', 'chart', 'pattern'))

st.header(option)

if option == 'twitter':
    st.subheader('twitter dashboard logic')
    user = st.sidebar.text_input("User", value='traderstewie')

    tweets = api.user_timeline(user)
    for tweet in tweets:
        if '$' in tweet.text:
            words = tweet.text.split(' ')
            for word in words:
                if word.startswith('$') and word[1:].isalpha():
                    symbol = word[1:]
                    st.write(symbol)
                    st.write(tweet.text)
                    st.image(f"https://finviz.com/chart.ashx?t={symbol}")

if option == 'stocktwits':
    symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

    data = r.json()

    for message in data['messages']:
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])


    

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)