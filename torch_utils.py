from PIL import Image
import numpy as np
import torch
from torchvision import transforms
from io import BytesIO
from torchvision import models, transforms
classes = ['color', 'cut', 'good', 'hole', 'metal_contamination', 'thread']

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()  # This will convert PIL image to tensor
])

# Load the model and modify the final layer
# You can change model_path to use a specific fold model
model_path = 'C:/Users/makerofdreams/Desktop/Demo/app_for_textile/model_fold1.pth'
model = models.resnet50(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, len(classes))
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

def transform_image(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert('L')  # Grayscale
    image = image.resize((64, 64))  # Resize to match original shape
    image = np.stack([np.array(image)] * 3, axis=2)  # (H, W, 3)
    image = Image.fromarray(image.astype(np.uint8))  # ✅ Back to PIL
    return transform(image).unsqueeze(0)  # (1, 3, 224, 224)

# Get prediction
def get_prediction(image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        return predicted, classes[predicted.item()]