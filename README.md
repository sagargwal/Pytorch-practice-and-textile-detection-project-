# Textile Defect Detection with PyTorch

**A deep learning model for detecting textile defects using microscopic images.**

This repository contains a deep learning model built with **PyTorch** to classify textile defects from images. The model was trained on a dataset of microscopic textile images, and the entire application has been deployed as a web app using **Flask** (backend) and **Streamlit** (frontend). The app is deployed on **Hugging Face Spaces** for public access.

---

## 🎯 Key Features

- **Deep Learning Model**: A ResNet50 model fine-tuned on textile defect data.
- **Backend**: Flask API for inference.
- **Frontend**: Streamlit web app to interact with the model and see predictions.
- **Deployment**: Hosted for free on Hugging Face Spaces.

---

## 📦 Requirements

Make sure you have the following dependencies:

- Python 3.6+
- **PyTorch**: For training and inference
- **Flask**: Backend to serve the model
- **Streamlit**: Frontend for interacting with the model
- **Other dependencies**: Requests, Pillow, numpy

## Install Dependencies
To install all the dependencies, use the following:



# ⚙️ Setup and Usage

## 1. Clone the Repository
Clone this repo to your local machine:

```bash
git clone https://github.com/yourusername/textile-defect-detection.git
cd textile-defect-detection
```
2. Model Setup
The model model_fold1.pth was trained using the Textile Defect Dataset from Kaggle.

To run the app locally, make sure the model file (model_fold1.pth) is present in the root directory.

3. Running the Backend (Flask API)
Run the Flask backend to expose the model for predictions:

```bash
python main.py
```
The API will be running on http://127.0.0.1:5000.

4. Running the Frontend (Streamlit)
Run the Streamlit app to interact with the model via the web interface:

```bash
streamlit run app.py
```
This will open a new tab in your browser where you can upload images and see predictions.

🌐 Deployment
This app has been deployed for free on Hugging Face Spaces.
https://huggingface.co/spaces/sagariitd/textile-defect-detector





