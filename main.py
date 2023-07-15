import yfinance as yf
#import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dowjones_data = yf.download("DJI", start = "2009-03-06", end="2023-07-15")

"""
MENGEKSTRAK FITUR DAN TARGET
"""
X = dowjones_data.reset_index()["Date"].apply(lambda x: int(x.strftime('%Y%m%d'))).values.reshape(-1, 1)
y = dowjones_data["Close"].values

"""
MEMBAGI DATA MENJADI DATA LATIH DAN DATA UJI
"""
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""
MEMBANGUN MODEL SIMPLE LINEAR REGRESSION
"""
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Meminta input tanggal dari pengguna
tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
inputanTanggal = tanggal

# Mengubah format tanggal menjadi array 2 dimensi
tanggal = [[int(tanggal.replace("-",""))]]

# Membuat prediksi harga Dow Jones
y_pred = regressor.predict(tanggal)

# Menampilkan hasil prediksi
print(f"Prediksi harga Dow Jones pada tanggal {inputanTanggal}, adalah {y_pred[0]}")