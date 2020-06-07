import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

#------------Wczytanie danych

df = pd.read_csv(r'C:\Python\ps.csv',delimiter=';')

#------------Badanie korelacji

print("Korelacja sprzedaży i zatrudnienia wynosi: {}".format(df['Zatrudnienie'].corr(df['Sprzedaz'])))
print("Korelacja produkcji i zatrudnienia wynosi: {}".format(df['Zatrudnienie'].corr(df['Produkcja'])))
print("Korelacja sprzedaży i produkcji wynosi: {}".format(df['Produkcja'].corr(df['Sprzedaz'])))

#------------Tworzenie wykresu korelacji

corrMatrix = df.corr()
sn.heatmap(corrMatrix, annot=True, square=True, vmin=0, vmax=1, robust=True)
plt.show()

#------------Podstawowe zależnosci

print("Średnia zatrudnienia wynosi: {}".format(df["Zatrudnienie"].mean()))
print("Odchylenie standardowe zatrudnienia wynosi: {}".format(df["Zatrudnienie"].std(axis = 0, skipna = True)))
print("Wariancja zatrudnienia wynosi: {}".format(df["Zatrudnienie"].var()))
print("Współczynnik zmiennosci zatrudnienia wynosi: {}".format((df["Zatrudnienie"].std())/(df["Zatrudnienie"].mean())))
print("Współczynnik asymetrii zatrudnienia wynosi: {}".format(((df["Zatrudnienie"].mean())-(df["Zatrudnienie"].mode()))/(df["Zatrudnienie"].std())))

print("Średnia sprzedaży wynosi: {}".format(df["Sprzedaz"].mean()))
print("Odchylenie standardowe sprzedaży wynosi: {}".format(df["Sprzedaz"].std()))
print("Wariancja sprzedaży wynosi: {}".format(df["Sprzedaz"].var()))
print("Współczynnik zmiennosci sprzedaży wynosi: {}".format((df["Sprzedaz"].std())/(df["Sprzedaz"].mean())))
print("Współczynnik asymetrii sprzedaży wynosi: {}".format(((df["Sprzedaz"].mean())-(df["Sprzedaz"].mode()))/(df["Sprzedaz"].std())))

print("Średnia produkcji wynosi: {}".format(df["Produkcja"].mean()))
print("Odchylenie standardowe produkcji wynosi: {}".format(df["Produkcja"].std()))
print("Wariancja produkcji wynosi: {}".format(df["Produkcja"].var()))
print("Współczynnik zmiennosci produkcji wynosi: {}".format((df["Produkcja"].std())/(df["Produkcja"].mean())))
print("Współczynnik asymetrii produkcji wynosi: {}".format(((df["Produkcja"].mean())-(df["Produkcja"].mode()))/(df["Produkcja"].std())))


print("Minimalna wartosc zatrudnienia wynosi: {}".format(df['Zatrudnienie'].min()))
print("Minimalna wartosc produkcji wynosi: {}".format(df['Produkcja'].min()))
print("Minimalna wartosc sprzedaży wynosi: {}".format(df['Sprzedaz'].min()))




