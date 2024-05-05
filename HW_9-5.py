def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        f = 0
        for i in range(2, res // 2+1):
            if (res % i == 0):
                f = f+1
        if (f <= 0):
            print('Число простое')
        else:
            print('Число составное')
        return f'Сумма чисел {res}'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)