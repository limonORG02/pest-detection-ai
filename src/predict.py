import tensorflow as tf
from preprocess import load_and_preprocess_image
import sys

if len(sys.argv) < 2:
    print("❌ Usage: python predict.py path_to_image")
    sys.exit(1)

model = tf.keras.models.load_model("models/pest_cnn.h5")
img = load_and_preprocess_image(sys.argv[1])
img = img.reshape(1, 128, 128, 3)

pred = model.predict(img)[0][0]
print("🐛 Вредитель обнаружен!" if pred > 0.5 else "🌿 Вредителей не найдено.")
