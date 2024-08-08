import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load ResNet50 model pre-trained on ImageNet
model = ResNet50(weights="imagenet")


# Function to preprocess the image and extract features
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    features = model.predict(img, verbose=0)
    return features


# Simple dummy caption generation function
def generate_caption(features):
    # Decode the predictions of ResNet50
    decoded_preds = decode_predictions(features, top=1)
    label = decoded_preds[0][0][1]  # Get the top predicted label
    return f"A photo of a {label}"


# Example usage
img_path = "tiger.jpeg"  # Replace with your image path
features = extract_features(img_path)
caption = generate_caption(features)

# Display the image and caption
img = Image.open(img_path)
plt.imshow(img)
plt.axis("off")
plt.title(caption)
plt.show()
