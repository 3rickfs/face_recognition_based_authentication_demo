import streamlit as st
import requests
import json
import base64
import os
import pandas as pd
from io import StringIO

usr_nm = st.text_input('Usuario a registrar', '')

def save_uploadedfile(uploadedfile):
     with open(os.path.join(".", "img.jpg"),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format("img.jpg"))

if st.button('Registrar'):
    st.write('Registrando usuario: ...')
    api_url = 'http://34.213.92.96:8000/registrar'

    files = {'imagen': open('img.jpg', 'rb')}
    data={'nombre': str(usr_nm)}
    response = requests.post(api_url, files=files, data=data)

    try:
        data = response.json()
        st.write(data)
    except requests.exceptions.RequestException:
        st.write(response.text)

if st.button('Procesar'):
    st.write('Procesando imagen...')
    api_url = 'http://34.213.92.96:8000/reconocer'

    files = {'imagen': open('img.jpg', 'rb')}
    st.write('Imagen cargada')
    response = requests.post(api_url, files=files)

    try:
        data = response.json()
        st.write(data)
    except requests.exceptions.RequestException:
        st.write(response.text)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    print("Cargando archivo")
    bytes_data = uploaded_file.getvalue()
    st.image(bytes_data, caption='Imagen cargada')
    save_uploadedfile(uploaded_file)


