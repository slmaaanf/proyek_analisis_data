import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data
day_data = pd.read_csv('./data/day.csv')

# Antarmuka Streamlit
st.title("Analisis Penyewaan Sepeda")

# Plot suhu vs penyewaan
st.subheader('Suhu vs Penyewaan Sepeda')
fig, ax = plt.subplots()
ax.scatter(day_data['temp'], day_data['cnt'])
st.pyplot(fig)

# Plot penyewaan berdasarkan hari dalam minggu
st.subheader('Penyewaan Berdasarkan Hari dalam Minggu')
weekday_data = day_data.groupby('weekday')['cnt'].mean().reset_index()
fig2, ax2 = plt.subplots()
ax2.bar(weekday_data['weekday'], weekday_data['cnt'])
st.pyplot(fig2)
