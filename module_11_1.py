import requests
import numpy as np

#Библиотека Requests
print(f'Библиотека Requests')
# Запросим данные с сайта https://urban-university.ru/ и выведим их в консоль

# URL для запроса

url = 'https://urban-university.ru/'

try:
    # Отправка GET-запроса
    response = requests.get(url)

    # Проверка успешности запроса
    response.raise_for_status()  # Это вызовет ошибку, если запрос не успешен (статус-код не 200)

    # Выводим содержимое страницы в консоль
    print(response.text)

except requests.exceptions.RequestException as e:
    # Обработка исключений
    print(f'Произошла ошибка при запросе: {e}')

# Библиотека NumPy
print(f'\nБиблиотека NumPy')
# Создаем массив чисел от 0 до 9
arr = np.arange(10)
print("Исходный массив:")
print(arr)

# Выполняем математические операции
# 1. Сложение
added_arr = arr + 5
print("\nПосле сложения 5:")
print(added_arr)

# 2. Умножение
multiplied_arr = arr * 2
print("\nПосле умножения на 2:")
print(multiplied_arr)

# 3. Возведение в квадрат
squared_arr = arr ** 2
print("\nПосле возведения в квадрат:")
print(squared_arr)

# 4. Вычисление среднего
mean_value = np.mean(arr)
print("\nСреднее значение массива:")
print(mean_value)

# 5. Максимальное и минимальное значение
max_value = np.max(arr)
min_value = np.min(arr)
print("\nМаксимальное значение в массиве:")
print(max_value)
print("Минимальное значение в массиве:")
print(min_value)

# 6. Сумма всех элементов
sum_value = np.sum(arr)
print("\nСумма всех элементов массива:")
print(sum_value)
