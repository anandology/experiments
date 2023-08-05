import streamlit as st
import io
import pandas as pd
import seaborn as sns
from pathlib import Path



root = Path("datasets")
root.mkdir(exist_ok=True)

def get_categorical_columns(df):
    return [c for c in df.select_dtypes(include='object') if df[c].nunique() <= 10]

def pairplot(path):
    df = pd.read_csv(path)

    st.header("Pair Plot")

    with st.sidebar:
        cats = ["None"] + get_categorical_columns(df)
        hue = st.selectbox("Color By", options=cats)

    if hue == "None":
        hue = None

    ax = sns.pairplot(df, hue=hue)
    st.pyplot(ax.figure)

def upload_dataset():
    st.header("Upload a New Dataset")
    uploaded_file = st.file_uploader("Upload a CSV file", "csv")

    if uploaded_file:
        path = root.joinpath(uploaded_file.name)
        path.write_bytes(uploaded_file.read())
        return path

with st.sidebar:
    st.title("Pair Plot")

    st.markdown("""
    Application to explore the numerical columns as a pair plot.
    """)

    st.header("Select a Dataset")

    datasets = [p.name for p in root.glob("*.csv")]

    label_upload = "Upload New Dataset"
    options = [label_upload] + datasets
    file = st.selectbox("Select a dataset", options=options)

if file == label_upload:
    path = upload_dataset()
    if path:
        pairplot(path)
else:
    path = root.joinpath(file)
    pairplot(path)

