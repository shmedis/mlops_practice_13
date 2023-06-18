import numpy as np
from sklearn.preprocessing import StandardScaler

# Загрузка данных
train_data = np.loadtxt("train/train_data.csv", delimiter=",")
test_data = np.loadtxt("test/test_data.csv", delimiter=",")

# Предобработка данных
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# Сохранение предобработанных данных
np.savetxt("train/train_data_preprocessed.csv", train_data, delimiter=",")
np.savetxt("test/test_data_preprocessed.csv", test_data, delimiter=",")
