import numpy as np
import os

# Создание папок "train" и "test", если они еще не существуют
os.makedirs("train", exist_ok=True)
os.makedirs("test", exist_ok=True)

# Создание обучающей выборки
train_data = np.random.rand(100, 10)  # Пример случайной обучающей выборки
np.savetxt("train/train_data.csv", train_data, delimiter=",")

# Создание тестовой выборки
test_data = np.random.rand(50, 10)  # Пример случайной тестовой выборки
np.savetxt("test/test_data.csv", test_data, delimiter=",")
