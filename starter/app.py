import streamlit as st
import pandas as pd
import matplotlib as plt

st.title('Supermarket Data')

@st.cache
def load_data(nrows):
    data = pd.read_csv('supermarket.csv', nrows=nrows)
    return data

data = load_data(896)

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