# -*- coding: utf-8 -*-
"""Bivariate analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qk9TFGYett838kP6XaLgaOMrq3HGM9OS

### **BIVARIATE ANALYSIS USING NUMPY AND PLOTLY**
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go

arr = np.array([[6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00], [4.6, 4.3, 4.5, 3.7, 3.3, 3.9, 2.6, 4.1, 3.6, 2.9, 1.6, 3.2, 4.3, 3.9, 4.5, 4.4, 4.8, 4.9]])
print("Numpy array:")
print(arr)

# convert numpy array to dataframe

df = pd.DataFrame(data = arr, index = ["Time of the day (X.hrs)", "Productivity Level(1-5)"])
print("\nPandas DataFrame:")
df

# Data Type of the above DataFrame

print(type(df))

## Taking Transpose of the above Pandas DataFrame

rdf = (df.T)
print(rdf)

# Head
rdf.head()

# Tail
rdf.tail()

#shape
rdf.shape

# bar chart using plotly

import plotly.graph_objects as go

trace = go.Bar(
x=rdf['Time of the day (X.hrs)'],
y=rdf['Productivity Level(1-5)']
)
layout = go.Layout(
height=400,
width=600,
margin=dict(l=0, r=0, t=0, b=0)
)
fig = go.Figure(data=[trace], layout=layout)
fig.show()