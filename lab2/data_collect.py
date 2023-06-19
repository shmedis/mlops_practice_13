import pandas as pd

# Загрузка данных из CSV файла
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Пример использования
file_path = "lab2/train.csv"
data = load_data(file_path)