import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load CSV file
def load_data(file):
    df = pd.read_csv(file)
    return df

# Function to show data statistics
def show_statistics(df):
    st.write("### Data Statistics")
    st.write(df.describe())

# Function to visualize data
def visualize_data(df):
    st.write("### Data Visualization")
    fig = px.scatter_matrix(df, title="Scatter Matrix")
    st.plotly_chart(fig)

st.title("Data visualization")

# File upload
st.sidebar.title("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    df = load_data(uploaded_file)

    # Show data
    st.write("### Displaying Data")
    st.write(df)

    # Show statistics
    show_statistics(df)

    # Visualize data
    visualize_data(df)
