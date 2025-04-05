# Pytorch-practice-and-textile-detection-project-
🚀 I recently completed the incredible PyTorch Deep Learning series by Patrick Loeber on YouTube, and I’ve come a long way in understanding the inner workings of PyTorch for deep learning model development! 🔥  🧠 As I followed through the series, I maintained a detailed set of notes and a Jupyter Notebook documenting how PyTorch works
Textile Defect Detection with PyTorch
A deep learning model for detecting textile defects using microscopic images.

This repository contains a deep learning model built with PyTorch to classify textile defects from images. The model was trained on a dataset of microscopic textile images, and the entire application has been deployed as a web app using Flask (backend) and Streamlit (frontend). The app is deployed on Hugging Face Spaces for public access.

🎯 Key Features
Deep Learning Model: A ResNet50 model fine-tuned on textile defect data.

Backend: Flask API for inference.

Frontend: Streamlit web app to interact with the model and see predictions.

Deployment: Hosted for free on Hugging Face Spaces.

📦 Requirements
Make sure you have the following dependencies:

Python 3.6+

PyTorch: For training and inference

Flask: Backend to serve the model

Streamlit: Frontend for interacting with the model

Other dependencies: Requests, Pillow, numpy

Install Dependencies
To install all the dependencies, use the following:

bash
Copy
pip install -r requirements.txt
⚙️ Setup and Usage
1. Clone the Repository
Clone this repo to your local machine:

bash
Copy
git clone https://github.com/yourusername/textile-defect-detection.git
cd textile-defect-detection
2. Model Setup
The model model_fold1.pth was trained using the Textile Defect Dataset from Kaggle.

To run the app locally, make sure the model file (model_fold1.pth) is present in the root directory.

3. Running the Backend (Flask API)
Run the Flask backend to expose the model for predictions:

bash
Copy
python main.py
The API will be running on http://127.0.0.1:5000.

4. Running the Frontend (Streamlit)
Run the Streamlit app to interact with the model via the web interface:

bash
Copy
streamlit run app.py
This will open a new tab in your browser where you can upload images and see predictions.

🌐 Deployment
This app has been deployed for free on Hugging Face Spaces.

Live Demo

🔧 Customization
Modify the Model:
To retrain or use a different model, make sure to update the model file (model_fold1.pth) and ensure it’s compatible with the rest of the code.

Change Classes:
The model is trained to predict 6 types of textile defects. If you want to train the model on a different dataset or change the class labels, you will need to modify the following:

Update the classes variable in torch_utils.py and app.py.

📝 Notes
The model was trained on microscopic textile data from Kaggle. You can access the dataset here.

Make sure to use grayscale or color images as input when testing the app.

If you want to use a different dataset, make sure the input dimensions and data format match the expected input.

🚀 Acknowledgements
PyTorch: For the deep learning framework used to train the model.

Hugging Face: For providing an easy and free way to deploy models via Hugging Face Spaces.

Kaggle: For providing the dataset of textile defects.

📫 Contact
If you have any questions or suggestions, feel free to contact me via LinkedIn or open an issue in this repo.

Example of requirements.txt:
txt
Copy
streamlit
requests
Pillow
numpy
torch
torchvision
This README will guide users through the process of setting up the model, running the app locally, and understanding how the model works. It also highlights the live demo and where users can access the project.

Let me know if you'd like to add anything else, such as more detailed instructions on retraining the model or improving the app's performance! 😊






