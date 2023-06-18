#!/bin/bash

# Создание данных
python data_creation.py

# Предобработка данных
python data_preprocessing.py

# Подготовка и обучение модели
python model_preparation.py

# Тестирование модели
python model_testing.py
