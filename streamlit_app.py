import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



st.title('CSV File Upload and Analysis')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded successfully!")

    # Save the file temporarily
    with open("uploaded_file.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Send the file to the Flask API
    with open("uploaded_file.csv", "rb") as f:
        response = requests.post("http://127.0.0.1:5000/upload", files={"file": f})
        data = response.json()

    # Display descriptive statistics
    st.subheader("Descriptive Statistics")
    desc_stats = pd.read_json(data['descriptive_statistics'])
    st.write(desc_stats)

    # Display correlation matrix
    st.subheader("Correlation Matrix")
    correlation_matrix = pd.read_json(data['correlation_matrix'])
    st.write(correlation_matrix)

    # Plot the heatmap
    st.subheader("Correlation Matrix Heatmap")
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot(plt)
