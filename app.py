# app.py
import streamlit as st
import pandas as pd
import plotly.express as px 

#"Streamlit App Title"

st.title("Streamlit Web Application")

#Load Data
data = pd.read_csv("vehicles_us.csv")

#Display Data
st.write("Displaying Data:")
st.dataframe(data)

#Create Plot 
fig = px.scatter (data, title="Scatter Plot")
st.plotly_chart(fig)
