import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import plot, show, xticks, yticks, title, xlabel, ylabel, legend, savefig 

#------------Wczytanie danych

df = pd.read_csv(r'C:\Python\ps.csv',delimiter=';')

#-----------Tworzenie wykresu

plt.plot(df['Data'], df['Produkcja'])
xticks(['I 2010','I 2012','I 2014','I 2016','I 2018','I 2020'], fontsize='15', fontname='Arial')
yticks(fontsize='15',fontname='Arial')
title("Produkcja węgla kamiennego",fontsize='19', fontname='Calibri') 
xlabel("Rok",fontsize='16', fontname='Calibri')  
ylabel("Tony",fontsize='16', fontname='Calibri')
