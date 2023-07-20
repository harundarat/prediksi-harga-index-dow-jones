import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
import joblib

# Mendapatkan data dari yahoo finance
stock_symbol = "^DJI"
stock_data = yf.download(stock_symbol, start="1992-02-01", end="2023-07-19", interval="1mo")

# Chart candlestick
fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                     open=stock_data['Open'],
                                     high=stock_data['High'],
                                     low=stock_data['Low'],
                                     close=stock_data['Close'])])

fig.update_layout(title="Chart Index Dow Jones (^DJI)",
                  xaxis_title="Date",
                  yaxis_title="Price")

st.plotly_chart(fig)

preddji = joblib.load('preddji_joblib')

tanggal = st.date_input("Masukkan Tanggal")
inputantanggal = tanggal

# # Mengubah format tanggal menjadi array 2 dimensi
# tanggal = [[int(tanggal.replace("-",""))]]

tanggal = tanggal.strftime("%Y%m%d")

# Mengubah format tanggal menjadi array 2 dimensi
tanggal = [[int(tanggal)]]


# Membuat prediksi harga Dow Jones
y_pred = preddji.predict(tanggal)

# Menampilkan hasil prediksi
st.write(f"Prediksi harga Dow Jones pada tanggla {inputantanggal}, adalah {y_pred[0]}")

