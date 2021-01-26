import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv("pokemon.csv")
st.write(data)

import matplotlib.pyplot as plt
import plotly.express as px

plot = px.histogram(data,x="base_total",y="is_legendary")

st.plotly_chart(plot)