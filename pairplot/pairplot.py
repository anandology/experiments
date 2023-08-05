import streamlit as st
import io
import pandas as pd
import seaborn as sns
from pathlib import Path


st.title("Pair Plot")

st.markdown("""
Application to explore the numerical columns as a pair plot.
""")

root = Path("datasets")
root.mkdir(exist_ok=True)

def get_categorical_columns(df):
    return [c for c in df.select_dtypes(include='object') if df[c].nunique() <= 10]

def pairplot(uploaded_file):
    path = root.joinpath(uploaded_file.name)
    path.write_bytes(uploaded_file.read())
    df = pd.read_csv(path)

    cats = ["None"] + get_categorical_columns(df)
    hue = st.selectbox("Color By", options=cats)
    if hue == "None":
        hue = None

    ax = sns.pairplot(df, hue=hue)
    st.pyplot(ax.figure)


st.header("Select a Dataset")
uploaded_file = st.file_uploader("Select Dataset", "csv")

if uploaded_file:
    st.header("Pair Plot")
    pairplot(uploaded_file)
