import tensorflow as tf
from sklearn.model_selection import train_test_split
from preprocess import prepare_dataset
import os

def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    X, y = prepare_dataset("data/train")
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

    model = build_model()
    history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)

    os.makedirs("models", exist_ok=True)
    model.save("models/pest_cnn.h5")
    print("✅ Model saved to models/pest_cnn.h5")
