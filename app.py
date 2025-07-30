import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('Penguine Specie Prediction ML app')
st.info("This is end-to-end Machine Learning app")

with st.expander("Data"):
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write("Input Variables")
  X_raw = df.drop('Species',axis = 1)
  X_raw

  st.write("Target Variables")
  y_raw = df.species
  y_raw

  st.write("Descriptive Statistics")
  des = df.describe()
  des
  
with st.expander("Data Visualization"):
  pass
  
with st.expander("Input Data"):
  pass

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
