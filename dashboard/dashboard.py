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

# Plot suhu vs penyewaan dengan slider interaktif
st.subheader('Suhu vs Penyewaan Sepeda')

# Slider untuk memilih rentang suhu
min_temp, max_temp = st.slider(
    'Pilih rentang suhu',
    min_value=float(day_data['temp'].min()), 
    max_value=float(day_data['temp'].max()), 
    value=(10.0, 30.0)
)

# Menampilkan nilai minimum dan maksimum dari slider untuk debugging
st.write(f"Rentang suhu yang dipilih: {min_temp} hingga {max_temp}")

# Filter data berdasarkan suhu yang dipilih
filtered_data = day_data[(day_data['temp'] >= min_temp) & (day_data['temp'] <= max_temp)]

# Tambahkan verifikasi jumlah data setelah pemfilteran
st.write(f"Jumlah data setelah filter: {filtered_data.shape[0]} baris")

# Cek apakah ada data setelah filter
if filtered_data.shape[0] > 0:
    # Membuat scatter plot suhu vs penyewaan
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['temp'], filtered_data['cnt'], color='blue')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penyewaan Sepeda')
    ax.set_title('Scatter Plot Suhu vs Penyewaan Sepeda')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
else:
    # Menampilkan peringatan jika tidak ada data
    st.warning("Tidak ada data untuk rentang suhu yang dipilih. Coba pilih rentang suhu yang berbeda.")

# Plot penyewaan berdasarkan hari dalam minggu
st.subheader('Penyewaan Berdasarkan Hari dalam Minggu')
weekday_data = day_data.groupby('weekday')['cnt'].mean().reset_index()

# Membuat bar plot penyewaan per hari
fig2, ax2 = plt.subplots()
ax2.bar(weekday_data['weekday'], weekday_data['cnt'], color='green')
ax2.set_xlabel('Hari dalam Minggu')
ax2.set_ylabel('Rata-rata Penyewaan Sepeda')
ax2.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Minggu')

# Menampilkan plot di Streamlit
st.pyplot(fig2)
