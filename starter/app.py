import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.title('Supermarket Data')

def get_path(csv):
    return Path('datasets', csv)

@st.cache
def get_csv(path):
    return pd.read_csv(path)

supermarket = get_path('supermarket.csv')

data = get_csv(supermarket)

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)

st.subheader('Distribution of Store Sales and Daily Customers')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(data['store_sales'], data['daily_customer_count'])
ax.set_xlabel('Store Sales')
ax.set_ylabel('Amount of Daily Customers')
st.pyplot(fig)

st.subheader('Average Sales For All Stores')
st.header('$59,351')