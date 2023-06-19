import pickle
import pandas as pd
import sklearn


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