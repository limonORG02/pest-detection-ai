import cv2
import os

def check_images(directory):
    bad_files = []
    for root, _, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            img = cv2.imread(path)
            if img is None:
                bad_files.append(path)
    return bad_files

if __name__ == "__main__":
    bad = check_images("data/test")
    if bad:
        print("❌ Плохие файлы:")
        for f in bad:
            print(f)
    else:
        print("✅ Все изображения читаются нормально!")
