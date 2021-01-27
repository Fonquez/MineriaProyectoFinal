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

data['sex'] = data['sex'].map({0:'female',1:'male'})
data['chest_pain_type'] = data['chest_pain_type'].map({1:'typical_angina', 2:'atypical_angina', 3:'non_anginal_pain', 4:'asymptomatic' })
data['fasting_blood_sugar'] = data['fasting_blood_sugar'].map({0:'less_than_120mg/ml',1:'greater_than_120mg/ml'})
data['resting_electrocardiographic'] = data['resting_electrocardiographic'].map({0:'normal',1:'ST-T_wave_abnormality',2:'left_ventricular_hypertrophy'})
data['exercise_induced_angina'] = data['exercise_induced_angina'].map({0:'no',1:'yes'})
data['st_slope'] = data['st_slope'].map({1:'upsloping',2:'flat',3:'downsloping'})
data['thalassemia'] = data['thalassemia'].map({3:'normal',6:'fixed_defect',7:'reversable_defect'})
data['target'] = data['target'].map({0:'no_disease', 1:'has_disease',2:'has_disease',3:'has_disease',4:'has_disease'})

col1, col2 = st.beta_columns(2)

fig1,ax = plt.subplots()
sns.countplot(data.sex,hue=data.target)
plt.xticks(rotation=10)
col1.pyplot(fig1)

fig2,ax = plt.subplots()
sns.countplot(data.chest_pain_type,hue=data.target)
plt.xticks(rotation=10)
col2.pyplot(fig2)

fig3,ax = plt.subplots()
sns.countplot(data.fasting_blood_sugar,hue=data.target)
plt.xticks(rotation=10)
col1.pyplot(fig3)

fig4,ax = plt.subplots()
sns.countplot(data.resting_electrocardiographic,hue=data.target)
plt.xticks(rotation=10)
col2.pyplot(fig4)

fig5,ax = plt.subplots()
sns.countplot(data.exercise_induced_angina,hue=data.target)
plt.xticks(rotation=10)
col1.pyplot(fig5)

fig6,ax = plt.subplots()
sns.countplot(data.st_slope,hue=data.target)
plt.xticks(rotation=10)
col2.pyplot(fig6)

fig7,ax = plt.subplots()
sns.countplot(data.num_major_vessels,hue=data.target)
plt.xticks(rotation=10)
col1.pyplot(fig7)

fig8,ax = plt.subplots()
sns.countplot(data.thalassemia,hue=data.target)
plt.xticks(rotation=10)
col2.pyplot(fig8)

col3, col4 = st.beta_columns(2)

fig9,ax = plt.subplots()
sns.swarmplot(x=data.target,y=data.age)
col3.pyplot(fig9)

fig10,ax = plt.subplots()
sns.swarmplot(x=data.target,y=data.resting_blood_pressure)
col4.pyplot(fig10)

fig11,ax = plt.subplots()
sns.swarmplot(x=data.target,y=data.cholesterol)
col3.pyplot(fig11)

fig12,ax = plt.subplots()
sns.swarmplot(x=data.target,y=data.max_heart_rate_achieved)
col4.pyplot(fig12)

fig13,ax = plt.subplots()
sns.swarmplot(x=data.target,y=data.st_depression)
col3.pyplot(fig13)
