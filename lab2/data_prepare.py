from sklearn.model_selection import train_test_split
import pandas as pd
from data_collect import data
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Предварительная обработка данных
def preprocess_data(data):
    # Заполнение пропущенных значений
    imputer = SimpleImputer(strategy='most_frequent')
    data['Age'] = imputer.fit_transform(data[['Age']])
    data['Embarked'] = imputer.fit_transform(data[['Embarked']])

    # Кодирование категориальных признаков
    label_encoder = LabelEncoder()
    data['Sex'] = label_encoder.fit_transform(data['Sex'])
    data['Embarked'] = label_encoder.fit_transform(data['Embarked'])

    # Масштабирование числовых признаков
    scaler = StandardScaler()
    data[['Age', 'Fare']] = scaler.fit_transform(data[['Age', 'Fare']])
    
    # Удаление лишнего
    data = data.drop(['Name', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin'], axis=1)

    return data

# Пример использования
preprocessed_data = preprocess_data(data)


# Подготовка датасета и сохранение тренировочных и тестовых данных
def prepare_dataset(data, target_column, test_size, random_state, save_path):
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)

    train_data.to_csv(save_path + "/train.csv", index=False)
    test_data.to_csv(save_path + "/test.csv", index=False)

# Пример использования
target_column = "Survived"
test_size = 0.2
random_state = 42
save_path = "/Users/dsshmelev/mlops_practice_13/lab2/datasets"
prepare_dataset(preprocessed_data, target_column, test_size, random_state, save_path)