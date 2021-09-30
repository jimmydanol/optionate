import config 
import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy
import psycopg2, psycopg2.extras

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
# cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

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

option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'wallstreetbets', 'stocktwits', 'mortgage'), 3)


st.header(option)


if option == 'twitter':
    # st.subheader('twitter dashboard logic')
    # user = st.sidebar.text_input("User", value='traderstewie')
    
    for username in config.TWITTER_USERNAMES:

        user = api.get_user(username)

        tweets = api.user_timeline(username)

        st.subheader(username)
        st.image(user.profile_image_url)

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


# if option == 'wallstreetbets':
#     num_days = st.sidebar.slider('Number of days', 1, 30, 3)

#     cursor.execute("""
#         SELECT COUNT(*) AS num_mentions, symbol
#         FROM mention JOIN stock ON stock.id = mention.stock_id
#         WHERE date(dt) > current_date - interval '%s day'
#         GROUP BY stock_id, symbol   
#         HAVING COUNT(symbol) > 10
#         ORDER BY num_mentions DESC
#     """, (num_days,))

#     counts = cursor.fetchall()
#     for count in counts:
#         st.write(count)
    
#     cursor.execute("""
#         SELECT symbol, message, url, dt, source
#         FROM mention JOIN stock ON stock.id = mention.stock_id
#         ORDER BY dt DESC
#         LIMIT 100
#     """)

#     mentions = cursor.fetchall()
#     for mention in mentions:
#         st.text(mention['dt'])
#         st.text(mention['symbol'])
#         st.text(mention['message'])
#         st.text(mention['url'])
#         st.text(mention['source'])

#     rows = cursor.fetchall()

#     st.write(rows)

if option == 'mortgage':
    # st.subheader('coming soon to a screen near deez nutz')
    user = st.text_input("What's your name?", max_chars=30)
    user = user.lower()
    if user == ('cedar'):
        st.write('I love you, big guy')
    elif user == ('river'):
        st.write('I love you, big chomper') 
    else:
        st.write(f"{user}")



hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)