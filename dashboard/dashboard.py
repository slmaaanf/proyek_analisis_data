import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Memuat data menggunakan path relatif
day_data_path = os.path.join('data', 'day.csv')
day_data = pd.read_csv(day_data_path)

# Menambahkan nama hari dalam minggu untuk kejelasan
days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
day_data['weekday'] = day_data['weekday'].apply(lambda x: days_of_week[x])

# Antarmuka Streamlit
st.title("Analisis Penyewaan Sepeda")

# Tampilkan Tabel Data
st.subheader("Tabel Data")
st.dataframe(day_data)

# Tampilkan Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(day_data.describe())

# Histogram Suhu
st.subheader("Distribusi Suhu")
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(day_data['temp'], bins=30, color='skyblue', edgecolor='black')
ax_hist.set_xlabel('Suhu')
ax_hist.set_ylabel('Frekuensi')
ax_hist.set_title('Histogram Distribusi Suhu')
st.pyplot(fig_hist)

# Tren Penyewaan Sepeda Seiring Waktu
if 'date' in day_data.columns:  # Pastikan ada kolom 'date'
    day_data['date'] = pd.to_datetime(day_data['date'])
    st.subheader("Tren Penyewaan Sepeda Seiring Waktu")
    fig_trend, ax_trend = plt.subplots()
    ax_trend.plot(day_data['date'], day_data['cnt'], color='orange')
    ax_trend.set_xlabel('Tanggal')
    ax_trend.set_ylabel('Jumlah Penyewaan')
    ax_trend.set_title('Tren Penyewaan Sepeda')
    st.pyplot(fig_trend)

# Filter berdasarkan hari
selected_day = st.selectbox('Pilih Hari', days_of_week)
filtered_by_day = day_data[day_data['weekday'] == selected_day]
st.write(filtered_by_day)

# Insight
st.subheader("Insight")
st.write("Dari analisis data, kita dapat melihat bahwa penyewaan sepeda cenderung meningkat pada hari-hari tertentu, terutama pada akhir pekan.")
