import pandas as pd
import streamlit as st

st.write('Data Frame Nilai')
df = pd.DataFrame(
    {
        'Budi': [70,80,75,85,90],
        'Andi': [60,80,90,95,100]
    },
    columns=['Budi', 'Andi']
)
st.write(df)

st.write('Line Chart Nilai')
st.line_chart(df)