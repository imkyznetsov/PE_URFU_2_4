import io
import streamlit as st
from PIL import Image

def load_image():
	"""Создание формы для загрузки изображения"""
	#
	uploaded_file = st.file_uploader(
		label='Выберите изображение для распознавания')
	if uploaded_file is not None:
	
		image_data = uploaded_file.getvalue()

		st.image(image_data)

		return Image.open(io.BytesIO(image_data))
	else:
		return None

st.title('Классификация изображений')
img = load_image()
