import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполняем таблицу 10 записями
#for i in range(1, 11):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500
#for i in range(1, 11, 2):
#    cursor.execute(f'UPDATE Users SET balance = 500 WHERE id IN ({i})')

# Удаляем каждую 3ю запись в таблице начиная с 1й
#for i in range(1, 11, 3):
#    cursor.execute(f'DELETE FROM Users WHERE id IN ({i})')

# Делаем выборку всех записей, где возраст не равен 60
#cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')

#users = cursor.fetchall()

# Выводим результаты в консоль
#for row in users:
#    username, email, age, balance = row
#    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

#Удаляем пользователя с id=6
cursor.execute('DELETE FROM Users WHERE id = ?', ('6',))

#Считаем количество пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

#Считаем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]

#Cредний баланс всех пользователей 1 метод:
print(f'Средний баланс всех пользователей (1 метод): {all_balance / total_users}')

#Cредний баланс всех пользователей 2 метод:
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей (2 метод): {avg_balance}')

connection.commit()
connection.close()
