import streamlit as st
import pandas as pd
import numpy as np

st.title("This is the title")

st.header("This is a header")

st.subheader("Subheader")
st.write("This is regular test")

'''
# This is the document title

This is some _markdown_.
'''


df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
st.dataframe(df)

#st.sidebar.write(df)

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

footer {
	
	visibility: hidden;
	
	}
# footer {visibility: hidden;}.stApp { bottom: 10px;} # 调整footer在底部的位置
footer:after {
	content:'goodbye'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
