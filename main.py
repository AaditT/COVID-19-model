import csv
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model

regions = []
dict = {}

df = pd.read_csv('data/time_series_19-covid-Confirmed.csv')
col = df.columns.tolist()
# print(col)

with open('data/time_series_19-covid-Confirmed.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[1] == "Thailand":
            thailand_row = row

thailand_dict = {col[i] : thailand_row[i] for i in range(len(col))}
thailand_dict.pop("Province/State", None)
thailand_dict.pop("Country/Region", None)
thailand_dict.pop("Lat", None)
thailand_dict.pop("Long", None)
dates = []
cases = []

for key in thailand_dict:
    thailand_dict[key] = int(thailand_dict[key])
    dates.append(key)
    cases.append(thailand_dict[key])

numbers = []

for i in range(len(dates)):
    numbers.append(i)

with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['x','cases'])
    for i in range(len(numbers)):
        spamwriter.writerow([numbers[i],cases[i]])

df = pd.read_csv("test.csv")
reg = linear_model.LogisticRegression()
reg.fit(df[['x']],df.cases)
print(reg.coef_)
print(reg.intercept_)

def model(x):
    return reg.predict([[x]])

with open('model.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['x','cases'])
    for i in range(len(numbers)):
        spamwriter.writerow([numbers[i],model(numbers[i])])

model_cases = []
model_cases_ = []

for i in range(len(numbers)):
    model_cases.append(model(numbers[i]))

for val in model_cases:
    val = list(val)[0]
    model_cases_.append(val)

fig = go.Figure()
fig.add_trace(go.Bar(x=numbers,y=cases))
fig.add_trace(go.Scatter(x=numbers,y=model_cases_))
fig.show()
