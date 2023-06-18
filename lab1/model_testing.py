import numpy as np
import pickle

# Загрузка обработанных данных
test_data = np.loadtxt("test/test_data_preprocessed.csv", delimiter=",")

# Разделение данных на признаки и метки
X_test = test_data[:, :-1]
y_test = test_data[:, -1]

# Загрузка модели из файла
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Оценка модели на тестовой выборке
accuracy = model.score(X_test, y_test)
print(f"Model test accuracy is: {accuracy:.3f}")
