import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

st.set_page_config(
    page_title="Tugas Phyton Web Programing",
    layout="wide",
    initial_sidebar_state="expanded",  
)

st.title('API Reference')

# 1.Write and Magic
st.title('1. Write and Magic')
st.write('Write adalah command yang digunakan untuk menuliskan sesuatu dengan comad: st.write(petik text petik)')

('Sedangkan Magic adalah command yang juga digunakan untuk menuliskan sesuatu tanpa command st.write, command yang digunakan adalah : (petik text petik)')

# 2. Text Element
st.title('2.Text Element')
st.title('Text ini dibuat menggunakan st.title')
st.write('st.title adalah command yang digukanan saat ingin menuliskan text dalam format judul.')

st.header('Text ini dibuat menggunakan st.header')
st.write('st.header adalah command yang digukanan saat ingin menuliskan text dalam format header.')

st.subheader('Text ini dibuat menggunakan st.subheader')
st.write('st.subheader adalah command yang digukanan saat ingin menuliskan text dalam format subheader.')

st.caption('Text ini dibuat menggunakan st.caption')
st.write('st.caption adalah command yang digukanan saat ingin menuliskan text dalam betuk caption,footnotes, sidenotes, atau text penjelasan lainnya.')

code='''print("HelloWorld)'''
st.code(code, language='phyton')
st.write('Text Hello World di atas di buat menggunakan command code, yang berfungsi menuliskan text dalam bentuk syntax.')

st.markdown(':red[HelloWorld]')
st.write('st.markdown adalah command yang digunakan untuk memberi warna pada text')

st.write('Selain dari banyak Element Text diatas juga ada st.text yang hampir sama dengan st.write dan st.latex yang berfungsi untuk menuliskan text rumus matematika.')

# 3. Data Display Element
st.title('3. Data Display Element')
# Data Frame
st.subheader('Data Frame')

st.write('Data Nilai')
df = pd.DataFrame(
    {
        'Budi': [70,80,75,85,90],
        'Andi': [60,80,90,95,100]
    },
    columns=['Budi', 'Andi']
)
st.write(df)

# Table
st.subheader('Table')
st.write('Data Nilai')
df = pd.DataFrame(
    {
        'Budi': [70,80,75,85,90],
        'Andi': [60,80,90,95,100]
    },
    columns=['Budi', 'Andi']
)
st.table(df)

st.write('Data di atas diatas dibuat meggunakan Data Frame, selain Data Frame, command st.table juga bisa digunakan jika ingin menampilkan data dalam bentuk table.')

# Metric
st.subheader('Metric')
col1, col2 = st.columns(2)
col1.metric("Budi", "Nilai", "70")
col2.metric("Andi", "Nilai", "60")

st.write('Selain ditampilkan dalam bentuk table, data juga bisa ditampilkan dalam bentuk matriks dengan comand st.metric.')

# 4. Chart Element
st.title('4. Chart Element')
st.write('Selain ditampilkan dalam bentuk tabel atau matriks, data juga bisa ditampilkan dalam bentuk chart')

st.write('Contoh Data')
df = pd.DataFrame(
    {
        'Budi': [70,80,75,85,90],
        'Andi': [60,80,90,95,100]
    },
    columns=['Budi', 'Andi']
)
st.write(df)
# Line Chart
st.subheader('Line Chart')
st.line_chart(df)
# Bar Chart
st.subheader('Bar Chart')
st.bar_chart(df)
# Area Chart
st.subheader('Area Chart')
st.area_chart(df)

# 5. Input Widget
st.title("5. Input Widget")

st.write('Silahkan Masukan Data Diri')
# Input Text Widget
nama = st.text_input('Nama', '')
# Radio Widget
jnsklmn = st.radio(
    "Jenis Kelamin",
    ('Laki-Laki', 'Perempuan'))
# Select Box Widget
tmptlhr = st.selectbox(
    'Tempat Lahir',
    ('Jakarta', 'Luar Jakarta','Luar P.Jawa'))
# Input Number Widget
usia = st.number_input('Usia')
usia = int(usia)
# Button Widget
if st.button('Submit'):
    st.write('Halo',nama,'Yang Berjenis Kelamin',jnsklmn,'dan Bertempat Lahir di',tmptlhr,'Dengan Usia',usia)
else:
    st.write('Silahkan Submit Data Diri Anda')

# 6. Media Element
st.title('6. Media Element')

# Image
image = Image.open('https://github.com/KyRzky/Tugas-PhytonWebPrograming/blob/main/Tugas3/Horizon.jpg')
st.image(image, caption='Morning Horizon')

# 7. Layout and Container
st.title('7. Layout and Cotainer')
st.write('Layout Side Bar disamping dibuat menggunakan st.sidebar')
# Side Bar
with st.sidebar:
    with st.echo():
        st.write("Tugas Phyton Web Programing .")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("32200004_Rizky")


#8 Status Element
st.title('8. Status Element')
st.error('Menampilkan Status Eror')
st.warning('Menampilkan Status Peringatan')
st.info('Menampilkan Informasi')
st.success('Menampilkan Status Sukses')
st.snow()
st.write('Efek Salju dibuat menggunakan command st.snow()')

#9 Control Flow
st.title('9. Control Flow')
with st.form("my_form"):
    st.write("Form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Checklist Jika Benar")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Nilai", slider_val, "Checkbox", checkbox_val)

# 10. Utilities
st.title('10. Utilities')

with st.echo():
    st.write('Text ini dibuat mengguakan st.echo')
