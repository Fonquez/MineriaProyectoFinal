import streamlit as st
import numpy as np
import pandas as pd

poke = pd.read_csv("pokemon.csv")
st.write(poke)

import matplotlib.pyplot as plt
import plotly.express as px

no_leg = poke[(poke['is_legendary'] == 0)]
leg = poke[(poke['is_legendary'] == 1)]

fig, ax = plt.subplots(figsize=(15, 8))
ax.hist(no_leg['base_total'], 10, None, ec='red', fc='none', lw=1.5, histtype='step', label='no legendary')
ax.hist(leg['base_total'], 10, None, ec='green', fc='none', lw=1.5, histtype='step', label='legendary')
ax.legend(loc='upper left')
plt.xlabel("base_total")
plt.ylabel("count")
plt.show()

st.pyplot(fig)

fig, ax = plt.subplots(figsize=(15, 8))
ax.hist(no_leg['capture_rate'], 10, None, ec='red', fc='none', lw=1.5, histtype='step', label='no legendary')
ax.hist(leg['capture_rate'], 10, None, ec='green', fc='none', lw=1.5, histtype='step', label='legendary')
ax.legend(loc='upper left')
plt.xlabel("capture_rate")
plt.ylabel("count")
plt.show()

st.pyplot(fig)
