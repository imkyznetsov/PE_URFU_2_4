import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions


@st.cache_data
def load_model():
    return EfficientNetB0(weights='imagenet')


def preprocess_image(img):
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x


def load_image():
    # Создание формы для загрузки изображения с использованием Streamlit
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Отображение загруженного изображения на странице
        st.image(image_data)
        # Форматирование изображения в PIL
        return Image.open(io.BytesIO(image_data))
    else:
        return None

def print_predictions(preds):
	classes = decode_predictions(preds, top=3)[0]
	for cl in classes:
		st.write(cl[1],cl[2])

# Загрузка предобученной модели
model = load_model()
# Вывод заголовка страницы
st.title('Классификация изображений, реализация с использованием Streamlit')
# Вывод формы загрузки изображения и получение изображения на вход 
img = load_image()
# Отображение кнопки для запуска распознавания
result = st.button('Распознать изображение')
# При нажтии кнопки запуск распознавания изображения
if result:
    # Предобработка изображения
    x = preprocess_image(img)
    # Распознавание изображения
    preds = model.predict(x)
    # Вывод заголовка результатов распознавания с использованием форматирования Markdown (жирный шрифт)
    st.write('Результаты распознавания:')
    # Вывод результатов распознавания
    print_predictions(preds)
