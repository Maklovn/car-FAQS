# app.py
import streamlit as st
import pandas as pd
import plotly.express as px 

# Streamlit App Header
st.title('Vehicle Data Analysis')

# Load the cleaned data from the CSV file under df
df = pd.read_csv('vehicles_us.csv')

# Display the dataset or a sample of it
st.subheader('Dataset Preview')
st.write(df.head())  # Display the first few rows of the dataset

# Checkbox to toggle the visibility of the histogram
show_histogram_price = st.checkbox('Show price Histogram')

# Conditional rendering of the first histogram 
if show_histogram_price:
    # create a combined histogram for price
    fig_price = px.histogram(df, x='price', color='condition', marginal='rug',
                   hover_data=['model_year'], title="Price based on Condition")
    st.subheader('Histogram')
    st.plotly_chart(fig_price, use_container_width=True)

# Create a combined histogram 
fig = px.histogram(df, x='price', color='odometer', marginal='rug',
                   hover_data=['model_year'], title='Price Based on Odometer')

# Checkbox toggle the visibility of the second histogram 
show_histogram_odometer = st.checkbox('Show Odometer Histogram')

# Conditional rednering of the second histogram 
if show_histogram_odometer:
    # Create a combined histogram
    fig_odometer = px.histogram(df, x='price', color='odometer', marginal='rug',
                                hover_data=['model_year'], title='Price based on Odometer')
   
    # Display the second histogram 
    st.subheader('Odometer Histogram')
    st.plotly_chart(fig_odometer, use_container_width=True)

# Checkbox to toggle teh visibility of the scatter plot
show_scatter_plot = st.checkbox('Show Scatter Plot')

# Conditional rendering of the scatter plot
if show_scatter_plot:
    # Display the scatter plot 
    st.subheader('Scatter Plot')
    st.plotly_chart(fig, use_container_width=True) # Use st.plotly_chart for the scatter plot
