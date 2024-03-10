
def test(*args, **kwargs):
    print('Введены следующие элементы', args)
test(1231, 'fdkjf', 53, 509)

def factorial(n):
    if n==1:
        return 1
    fact_min_1 = factorial(n=n-1)
    return n*fact_min_1
print(factorial(7))












