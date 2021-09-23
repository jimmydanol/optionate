import streamlit as st
import pandas as pd
import numpy as np

st.title("This is the Nonsense")

st.header("This is a Cedar Beeter")

st.subheader("Subheader")
st.write("This is regular text")

'''
# This is the document title

This is some _markdown_.
'''


df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
st.dataframe(df)

# st.sidebar.write(df)
