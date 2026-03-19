import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load trained model
model = load_model("age_gender_model.keras")

st.title("Age and Gender Prediction")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    # Convert to grayscale safely
    gray = image.convert("L")
    gray = np.array(gray)
    # Resize
    gray = cv2.resize(gray,(128,128))

    # Normalize
    gray = gray / 255.0

    # Reshape
    gray = gray.reshape(1,128,128,1)

    # Predict
    gender_pred , age_pred = model.predict(gray)
   

    gender = "Female" if gender_pred[0][0] > 0.5 else "Male"
    age = int(np.round(age_pred[0][0]))

    st.write("Predicted Gender:", gender)
    st.write("Predicted Age:", age)