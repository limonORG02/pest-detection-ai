import cv2
import numpy as np
import os

IMG_SIZE = 128

def load_and_preprocess_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0  # нормализация
    return img

def prepare_dataset(directory):
    X, y = [], []
    label_map = {"no_pests": 0, "pests": 1}

    for label in label_map:
        path = os.path.join(directory, label)
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            X.append(load_and_preprocess_image(full_path))
            y.append(label_map[label])

    return np.array(X), np.array(y)
