import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Textile Defect Classifier", layout="centered")

st.title("🧵 Textile Defect Classifier")
st.write("Upload one or more textile images to predict their defect class.")

# Multiple file uploader
uploaded_files = st.file_uploader(
    "Choose image files", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

if uploaded_files:
    if st.button("🔍 Predict All"):
        for uploaded_file in uploaded_files:
            try:
                # Show preview
                image = Image.open(uploaded_file)
                st.image(image, caption=f"Image: {uploaded_file.name}", width=300)

                # Send file to Flask API
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }
                response = requests.post("http://127.0.0.1:5000/predict", files=files)

                # Handle response
                if response.status_code == 200:
                    prediction = response.json()
                    st.success(f"🎯 Prediction for `{uploaded_file.name}`: **{prediction['class_name']}**")
                else:
                    st.error(f"❌ Error on `{uploaded_file.name}`: {response.status_code} - {response.json().get('error')}")

            except Exception as e:
                st.error(f"⚠️ Failed to process `{uploaded_file.name}`: {str(e)}")
