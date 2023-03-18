import streamlit as st
import pandas as pd

st.write('Data Frame Nilai')
df = pd.DataFrame(
    {
        'Budi': [70,80,75,85,90],
        'Andi': [60,80,90,95,100]
    },
    columns=['Budi', 'Andi']
)
st.write(df)

st.write('Bar Chart Nilai')
st.bar_chart(df)