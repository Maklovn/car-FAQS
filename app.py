# app.py
import streamlit as st
import pandas as pd
import plotly.express as px 

# Streamlit App Header
st.title('Vehicle Data Analysis')

# Load the cleaned data from the CSV file under df
df = pd.read_csv('cleaned_dataset.csv')

# Display the dataset or a sample of it
st.subheader('Dataset Preview')
st.write(df.head())  # Display the first few rows of the dataset from the 'cleaned_dataset.csv' file

# Group by 'model_year' and fill missing values with median
df_grouped_by_year = df.groupby('model_year').transform(lambda x: x.fillna(x.median(
)))

# Checkbox to toggle the visibility of the histogram
show_histogram_price = st.checkbox('Show price Histogram')

# Conditional rendering of the first histogram
if show_histogram_price:
    # Create a combined histogram for price
    fig_price = px.histogram(df, x='price', color='condition', marginal='rug',
                   hover_data=['model_year'], title="Price based on Condition")
    st.subheader('Histogram')
    st.plotly_chart(fig_price, use_container_width=True)

# Define show_histogram_odometer here (before usage)
show_histogram_odometer = st.checkbox('Show Odometer Histogram')

# Conditional rendering of the second histogram (group by model_year and fill by median)
if show_histogram_odometer:
    # Group by 'model_year' and fill missing values with median
    df_grouped_by_year = df.groupby('model_year').transform(lambda x: x.fillna(x.median()))

    # Create a combined histogram for 'price' based on 'odometer'
    fig_odometer = px.histogram(df_grouped_by_year, x='price', color='odometer', marginal='rug',
                                title='Price based on Odometer (Median Fill)')
   
    # Display the second histogram 
    st.subheader('Odometer Histogram (Median Fill)')
    st.plotly_chart(fig_odometer, use_container_width=True)

# Checkbox to toggle the visibility of the scatter plot
show_scatter_plot = st.checkbox('Show Scatter Plot')

# Conditional rendering of the scatter plot
if show_scatter_plot:
    # Create a scatter plot using 'model' and 'model_year' columns from 'df'
    fig_scatter = px.scatter(df, x='model', y='model_year', color='condition', title='Make, year and condition')

    # Display the scatter plot 
    st.subheader('Scatter Plot')
    st.plotly_chart(fig_scatter, use_container_width=True)




