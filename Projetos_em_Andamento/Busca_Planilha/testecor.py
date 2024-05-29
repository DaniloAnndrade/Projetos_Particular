import csv
import pandas as pd


planilha = pd.read_csv("Planilha teste.csv")

con_pl = len(planilha)

planilha['DATA']= pd.to_datetime(planilha['DATA'])

data_planilha = planilha.sort_values(by='DATA', ascending=True)

print(data_planilha)
