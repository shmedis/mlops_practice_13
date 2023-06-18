import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Загрузка обработанных данных
train_data = np.loadtxt("train/train_data_preprocessed.csv", delimiter=",")

# Разделение данных на признаки и метки
X_train = train_data[:, :-1]
y_train = train_data[:, -1]

# Создание и обучение модели
model = LogisticRegression()
model.fit(X_train, y_train)

# Сохранение модели в файл
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
