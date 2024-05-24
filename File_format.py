import random
# Вводим количество участников в каждой команде
team1_num = int(input('Укажите количество игороков команды "Мастера кода" '))
team2_num = int(input('Укажите количество игороков команды "Волшебники данных" '))

# Определяем количество решенных задач
score1 = random.randrange(30 , 50, 1)
score2 = random.randrange(30 , 50, 1)

# Узнаем время решения задач каждой командой
team1_time = random.randrange(1000 , 3000, 1) + random.random()
team2_time = random.randrange(1000 , 3000, 1) + random.random()

# Общее количество решенных задач
tasks_total = score1+score2
# Среднее время на решение одной задачи
time_avg = round((team1_time+team2_time)/tasks_total, 2)

# Определяем победителя
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды "Мастера кода"!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды "Волшебники данных"!'
else:
    challenge_result = 'Ничья!'

# Выводим результаты на экран
print('В команде "Мастера кода" участников: %s !' % (team1_num) )
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num) )

print('Команда "Волшебники данных" решила задач: {} !'.format(score2))
print('"Волшебники данных" решили задачи за {} секунд !'.format(round(team2_time, 2)))

print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
