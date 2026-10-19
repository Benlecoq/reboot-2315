import streamlit as st
import requests

 # Change this URL to the one of your API
API_URL = "https://reboot2315-689436528172.europe-west1.run.app/"

st.title("My awesome MVP")

st.write("Iris predictor")

sepal_length = st.slider('Select a value for Sepal length', min_value=0, max_value=4, value=1, step=1)
sepal_width = st.slider('Select a value for Sepal width',  min_value=0, max_value=4, value=1, step=1)
petal_length = st.slider('Select a value for Petal length',  min_value=0, max_value=4, value=1, step=1)
petal_width = st.slider('Select a value for Petal width',  min_value=0, max_value=4, value=1, step=1)

url = f"{API_URL}/predict"
params = {
    'x1': sepal_length,
    'x2': sepal_width,
    'x3': petal_length,
    'x4': petal_width,
}

response = requests.get(url, params=params).json()

st.write(f"This flower belongs to category {str(response['prediction'])}")
