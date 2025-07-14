import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

model_path = os.path.join("models", "cnn2_model.h5")
model = load_model(model_path)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0][0]
    label = "Brain Tumor: Positive" if pred > 0.5 else "Brain Tumor: Negative"
    confidence = round(pred if pred > 0.5 else 1 - pred, 4)

    return label, confidence
