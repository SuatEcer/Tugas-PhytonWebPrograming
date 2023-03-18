import streamlit as st
import pandas as pd
import numpy as np

add_selectbox = st.sidebar.selectbox(
    'Olahraga Apa yang Anda Suka?',
    ('Sepak Bola', 'Basket', 'Voli')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Tentukan Nilai Presentase',
    0.0, 100.0
)

st.write('Anda Menyukai Olahraga',add_selectbox,'Dengan Presentase Sebesar',add_slider)