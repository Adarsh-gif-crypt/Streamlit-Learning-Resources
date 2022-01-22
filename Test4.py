from pygments import highlight
import streamlit as st
import pandas as pd
import numpy as np
import time

a = [0,1,2,3,4,5,6,7,8,9]
n = np.array(a)
nd = n.reshape((2,5))

df = pd.read_csv("D:/DS/Streamlit/nba21.csv")
#st.dataframe(n)
#st.dataframe(nd)
st.dataframe(df)
#st.table(df)

@st.cache
def ret_time():
    time.sleep(5)
    return time.time()

if st.sidebar.checkbox('Run Function'):
    st.write(ret_time())
#can induce parameters and argc