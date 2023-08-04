import streamlit as st
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import io
import pandas as pd

st.title("GC Viewer")

st.markdown("""
GC Viewer is a simple application to explore GC fractions
of all sequences in a FASTA file.

Select a FASTA file to get started.
""")

def gc_viewer(uploaded_file):
    f = io.TextIOWrapper(uploaded_file, encoding="utf-8")
    records = SeqIO.parse(f, "fasta")
    records = list(records)

    data = [[rec.id, gc_fraction(rec.seq)] for rec in records]
    columns = ["Seq Id", "GC Fraction"]

    df = pd.DataFrame(data, columns=columns)

    st.header("GC Fraction as Table")

    df.set_index("Seq Id", inplace=True)
    st.write(df)

    st.header("GC Fraction as Chart")
    st.bar_chart(df, y="GC Fraction")

    # for rec in records:
    #     st.subheader(rec.id)
    #     st.write(rec.seq)

st.header("Select a FASTA file")
uploaded_file = st.file_uploader("Select FASTA File", "fasta")

if uploaded_file:
    gc_viewer(uploaded_file)