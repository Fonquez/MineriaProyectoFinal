import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv("pokemon.csv")
st.write(data)

import matplotlib.pyplot as plt
import plotly.express as px

<<<<<<< HEAD
plot = px.histogram(data,x="base_total",y="is_legendary")
=======
plot = sns.histplot(data,x=data.base_total,y=data.is_legendary)
>>>>>>> 5c88a68b483e3cd30145ce075a22aa2362507066

st.plotly_chart(plot)