import os
import shutil
import random

def split_dataset(source_dir, train_dir, test_dir, split_ratio=0.8):
    for category in os.listdir(source_dir):
        path = os.path.join(source_dir, category)
        if not os.path.isdir(path):
            continue

        imgs = os.listdir(path)
        random.shuffle(imgs)
        split_point = int(len(imgs) * split_ratio)
        train_imgs = imgs[:split_point]
        test_imgs = imgs[split_point:]

        os.makedirs(os.path.join(train_dir, category), exist_ok=True)
        os.makedirs(os.path.join(test_dir, category), exist_ok=True)

        for img in train_imgs:
            shutil.copy(os.path.join(path, img), os.path.join(train_dir, category, img))
        for img in test_imgs:
            shutil.copy(os.path.join(path, img), os.path.join(test_dir, category, img))

    print("✅ Dataset split completed.")

if __name__ == "__main__":
    split_dataset("data", "data/train", "data/test")
