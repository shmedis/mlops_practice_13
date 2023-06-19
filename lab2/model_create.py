from sklearn.ensemble import RandomForestClassifier
import pickle
from data_collect import load_data

# Обучение модели и сохранение в файл
def train_model(train_data, target_column, save_path):
    X_train = train_data.drop(target_column, axis=1)
    y_train = train_data[target_column]

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    with open(save_path + "/model.pkl", "wb") as f:
        pickle.dump(model, f)

# Пример использования
train_file_path = "lab2/datasets/train.csv"
target_column = "Survived"
save_path = "lab2/models"
train_data = load_data(train_file_path)
train_model(train_data, target_column, save_path)