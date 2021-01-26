import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv("pokemon.csv")
st.write(data)
