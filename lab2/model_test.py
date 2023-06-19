import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Загрузка тестового датасета из CSV файла
def load_test_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Загрузка модели из файла и выполнение прогноза на тестовых данных
def evaluate_model(test_data, target_column, model_path):
    X_test = test_data.drop(target_column, axis=1)
    y_test = test_data[target_column]

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(X_test)
    return predictions

    # Выполнение анализа качества модели и других необходимых операций

# Пример использования
test_file_path = "lab2/datasets/test.csv"
model_path = "lab2/models/model.pkl"
test_data = load_test_data(test_file_path)
target_column = 'Survived'
evaluate_model(test_data, target_column, model_path)

# Вычисление и вывод тестовых метрик
def evaluate_model(test_data, target_column, model_path):
    X_test = test_data.drop(target_column, axis=1)
    y_test = test_data[target_column]

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

# Пример использования
test_file_path = "lab2/datasets/test.csv"
model_path = "lab2/models/model.pkl"
test_data = load_test_data(test_file_path)
evaluate_model(test_data, target_column, model_path)