import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv("pokemon.csv")
st.write(data)

import matplotlib as plt
import seaborn as sns

plot = sns.histplot(data,x=data.base_total,y=data.is_legendary)

st.write(plot)
