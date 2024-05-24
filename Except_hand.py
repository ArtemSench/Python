def string_to_int(s): # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        print(f'Переменная "{s}" не является целым числом')

def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file: return file.read()
    except FileNotFoundError:
        print(f'Файл {filename} не найден')
    except IOError:
        print(f'Ошибка ввода\вывода файла {filename}')
def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        print ('На ноль делить нельзя')
    except TypeError:
        print('Вместо чисел - буквы, исправьте')

def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        print(f'В списке меньше {index} символов, укажите не более {len(lst)-1} символов ')
    except TypeError:
        print(f'Укажите номер символа, вместо самого символа')

string_to_int("а")
read_file('byron.txt')
divide_numbers(4,0)
divide_numbers('f',5)
access_list_element('Hello, world!', 45)
access_list_element('Hello, world!', 12)
access_list_element('Hello, world!', 'l')
