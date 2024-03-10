
def test(*args, **kwargs):
    print('Введены следующие элементы', args)
test(1231, 'fdkjf', 53, 509)

def factorial(n):
    if n==1:
        return 1
    fact_min_1 = factorial(n=n-1)
    return n*fact_min_1
print(factorial(7))










#input('Напишите несколько элементов разных типов')
#def fact(n):
#    input('Введите число для возведения в факториал:', n)
#    if n == 1:
#        fact_minus_1=fact(n=n-1)
#        print('Факториал заданного числа равен:', n*fact_minus_1)



