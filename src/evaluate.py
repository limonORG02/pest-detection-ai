import tensorflow as tf
from preprocess import prepare_dataset

model = tf.keras.models.load_model("models/pest_cnn.h5")
X_test, y_test = prepare_dataset("data/test")

loss, acc = model.evaluate(X_test, y_test)
print(f"✅ Test Accuracy: {acc*100:.2f}%")
