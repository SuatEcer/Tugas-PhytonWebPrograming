import streamlit as st
import pandas as pd

st.title("Silahkan Pilih Menu")

Menu = st.radio(
    "Apa Menu Yang Anda Suka?",
    ('Coffe', 'Tea', 'Juice'))

option = st.selectbox(
    'Hot or Ice',
    ('Hot', 'Ice'))

st.write('Anda Memilih',option,Menu)


