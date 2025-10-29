#!/bin/bash
echo "🚀 Запуск проекта по обнаружению вредителей"
echo "1. Установка зависимостей"
pip install -r requirements.txt

echo "2. Подготовка данных"
python data/dataset_split.py

echo "3. Обучение модели"
python src/train_model.py

echo "4. Проверка точности"
python src/evaluate.py

echo "✅ Готово! Можно делать предсказания командой:"
echo "python src/predict.py path_to_image.jpg"
