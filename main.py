import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Exploración de datos")

data = pd.read_csv("heart.csv")
data = data.iloc[:,1:]
st.write(data)
st.write(data.dtypes)
st.write(data[data.Thalessemia == "?"].Thalessemia)
st.write(data[data.Major_Vessels == "?"].Major_Vessels)
st.write("Como se puede observar, hay 6 datos faltantes, por lo que se va a aplicar un forward_fill")

data = data.replace("?", np.NaN)
data.ffill(inplace=True)
data.Major_Vessels = data.Major_Vessels.astype('int64')
data.Thalessemia = data.Thalessemia.astype('int64')
st.write(data)
st.write(data.dtypes)

data.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol',
                'fasting_blood_sugar', 'resting_electrocardiographic', 'max_heart_rate_achieved', 'exercise_induced_angina',
                'st_depression', 'st_slope', 'num_major_vessels', 'thalassemia', 'target']

data_visual = data.copy()

data_visual['sex'] = data_visual['sex'].map({0:'female',1:'male'})
data_visual['chest_pain_type'] = data_visual['chest_pain_type'].map({1:'typical_angina', 2:'atypical_angina', 3:'non_anginal_pain', 4:'asymptomatic' })
data_visual['fasting_blood_sugar'] = data_visual['fasting_blood_sugar'].map({0:'less_than_120mg/ml',1:'greater_than_120mg/ml'})
data_visual['resting_electrocardiographic'] = data_visual['resting_electrocardiographic'].map({0:'normal',1:'ST-T_wave_abnormality',2:'left_ventricular_hypertrophy'})
data_visual['exercise_induced_angina'] = data_visual['exercise_induced_angina'].map({0:'no',1:'yes'})
data_visual['st_slope'] = data_visual['st_slope'].map({1:'upsloping',2:'flat',3:'downsloping'})
data_visual['thalassemia'] = data_visual['thalassemia'].map({3:'normal',6:'fixed_defect',7:'reversable_defect'})
data_visual['target'] = data_visual['target'].map({0:'no_disease', 1:'has_disease',2:'has_disease',3:'has_disease',4:'has_disease'})

st.write("## Datos categóricos")
col1, col2 = st.beta_columns(2)

fig1,ax = plt.subplots()
sns.countplot(data_visual.sex,hue=data_visual.target)
plt.xticks(rotation=10)
col1.pyplot(fig1)

fig2,ax = plt.subplots()
sns.countplot(data_visual.chest_pain_type,hue=data_visual.target)
plt.xticks(rotation=10)
col2.pyplot(fig2)

fig3,ax = plt.subplots()
sns.countplot(data_visual.fasting_blood_sugar,hue=data_visual.target)
plt.xticks(rotation=10)
col1.pyplot(fig3)

fig4,ax = plt.subplots()
sns.countplot(data_visual.resting_electrocardiographic,hue=data_visual.target)
plt.xticks(rotation=10)
col2.pyplot(fig4)

fig5,ax = plt.subplots()
sns.countplot(data_visual.exercise_induced_angina,hue=data_visual.target)
plt.xticks(rotation=10)
col1.pyplot(fig5)

fig6,ax = plt.subplots()
sns.countplot(data_visual.st_slope,hue=data_visual.target)
plt.xticks(rotation=10)
col2.pyplot(fig6)

fig7,ax = plt.subplots()
sns.countplot(data_visual.num_major_vessels,hue=data_visual.target)
plt.xticks(rotation=10)
col1.pyplot(fig7)

fig8,ax = plt.subplots()
sns.countplot(data_visual.thalassemia,hue=data_visual.target)
plt.xticks(rotation=10)
col2.pyplot(fig8)

st.write("## Datos numéricos")
col3, col4 = st.beta_columns(2)

fig9,ax = plt.subplots()
sns.swarmplot(x=data_visual.target,y=data_visual.age)
col3.pyplot(fig9)

fig10,ax = plt.subplots()
sns.swarmplot(x=data_visual.target,y=data_visual.resting_blood_pressure)
col4.pyplot(fig10)

fig11,ax = plt.subplots()
sns.swarmplot(x=data_visual.target,y=data_visual.cholesterol)
col3.pyplot(fig11)

fig12,ax = plt.subplots()
sns.swarmplot(x=data_visual.target,y=data_visual.max_heart_rate_achieved)
col4.pyplot(fig12)

fig13,ax = plt.subplots()
sns.swarmplot(x=data_visual.target,y=data_visual.st_depression)
col3.pyplot(fig13)


st.write("# Clustering")
data_norm = (data-data.min())/(data.max()-data.min())
data_norm = data_norm.iloc[:,:-1]
st.write("Antes de continuar, hay que normalizar los datos: ")
st.write(data_norm)

from sklearn.cluster import KMeans
from yellowbrick.cluster import SilhouetteVisualizer

st.write("Se va a usar k-means para agrupar los datos. Para determinar la k se va a hacer la prueba Silhouette.")
col4, col5 = st.beta_columns(2)
for i in range(2,10):
    fig_sil, ax_sil = plt.subplots()
    model = KMeans(i)
    visualizer = SilhouetteVisualizer(model,ax=ax_sil)
    visualizer.fit(data_norm)
    if i%2 == 0:
        col4.pyplot(fig_sil)
    elif i%2 == 1:
        col5.pyplot(fig_sil)

st.write("Por lo que se puede observar, se determinó que con k=4 la agrupación es más estable")

clustering = KMeans(n_clusters = 4, max_iter=300)
clustering.fit(data_norm)

data['k-means_clusters'] = clustering.labels_

col6, col7 = st.beta_columns(2)

for i in range(0,4):
    if i%2 == 0:
        col6.write(f"Cluster {i}")
        col6.write(data[data["k-means_clusters"]==i])
    elif i%2 == 1:
        col7.write(f"Cluster {i}")
        col7.write(data[data["k-means_clusters"]==i])

for i in range(0,4):
    if i%2 == 0:
        col6.write(f"Cluster {i}")
        col6.write(data[data["k-means_clusters"]==i].mean())
    elif i%2 == 1:
        col7.write(f"Cluster {i}")
        col7.write(data[data["k-means_clusters"]==i].mean())

st.write("Cluster 0: mayoritariamente hombres, con exercise_induced_angina con historial de talasemia que tienen alta posibilidad de tener enfermedad de corazón")
st.write("Cluster 1: mujeres, sin historial de talasemia que tienen baja probabilidad de presentar la enfermedad")
st.write("Cluster 2: hombres, sin historial de talasemia que tienen baja probabilidad de presentar la enfermedad")
st.write("Cluster 3: mayoritariamente hombres que no presentan excersie_induced_angina con historial de talasemia que tienen una moderada probabilidad de presentar la enfermedad")
st.write("*El orden de los clusters puede cambiar, así como se pueden presentar pequeñas variaciones en los números, ya que k-means es susceptible a las condiciones iniciales")
