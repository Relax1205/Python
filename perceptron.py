import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        """
        Конструктор перцептрона.
        input_size: Количество входных признаков
        learning_rate: Скорость обучения
        epochs: Количество эпох обучения
        """
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        """
        Функция активации (пороговая функция).
        Возвращает 1, если x >= 0, иначе 0.
        """
        return 1 if x >= 0 else 0

    def predict(self, x):
        """
        Метод предсказания класса для входного примера.
        x: Входные данные (массив признаков)
        return: Предсказанный класс (0 или 1)
        """
        x = np.insert(x, 0, 1)
        return self.activation(np.dot(self.weights, x))

    def train(self, X, y):
        """
        Метод обучения перцептрона.
        X: Матрица входных данных (каждая строка — это пример)
        y: Вектор целевых значений (ожидаемые классы)
        """
        for _ in range(self.epochs):
            for i in range(len(X)):
                x_i = np.insert(X[i], 0, 1)  # Добавляем bias в начало входного вектора
                y_pred = self.activation(np.dot(self.weights, x_i))  # Предсказание
                error = y[i] - y_pred  # Ошибка
                self.weights += self.learning_rate * error * x_i  # Обновление весов

# Пример использования
if __name__ == "__main__":
    # Данные для обучения (логическая функция И)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  # Ожидаемые результаты
    
    perceptron = Perceptron(input_size=2)
    perceptron.train(X, y)
    
    # Проверка предсказаний
    print("Результаты предсказаний:")
    for x in X:
        print(f"Вход: {x}, Предсказание: {perceptron.predict(x)}")
