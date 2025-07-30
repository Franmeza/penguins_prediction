import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px

st.title('Penguine Specie Prediction ML app')
st.info("This is end-to-end Machine Learning app")

with st.expander("Data"):
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write("Input Variables")
  X_raw = df.drop('species',axis = 1)
  X_raw

  st.write("Target Variables")
  y_raw = df.species
  y_raw

  st.write("Descriptive Statistics")
  des = df.describe()
  des

  st.write("More information about data")
  inf = df.info()
  inf
  
with st.expander("Data Visualization"):
  st.scatter_chart(data=df, x='bill_length_mm',y='body_mass_g',color='species')
  fig = px.box(df, x='species', y='bill_length_mm', title='Box Plot')
  st.plotly_chart(fig)

with st.expander("Data Preparation"):
  pass

with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  bill_length_mm = st.slider("Bill length (mm)",32.0,60.0,43.9)
  bill_depth_mm = st.slider("Bill depth (mm)",13.0,22.0,18.0)
  flipper_length_mm = st.slider("Flipper length (mm)",172.0,231.0,201.0)
  boddy_mass_g = st.slider("Body Mass (g)",2700.0,6300.0,4207.0)
  gender = st.selectbox("Gender",("Male","Female"))

  data = {
    'island':island,
    'bill_length_mm':bill_length_mm,
    'bill_depth_mm':bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'boddy_mass_g': boddy_mass_g,
    'gender':gender
  }

  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X_raw], axis = 0)

with st.expander("Input data"):
  st.write("**Input data**")
  input_df
  st.write("**Combined Data**")
  input_penguins

#One hot encoding for X
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins, prefix = encode)
X = df_penguins[1:]
input_row = df_penguins[:1]

#one hot encoding for y
target_mapper = {
  'Adelie':0,
  'Chinstrap':1,
  'Gentoo':2
}

def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)


  
  
