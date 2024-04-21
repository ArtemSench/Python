import warnings

def divide_numbers(a, b):
    try:
        print(a / b)
        if -0.1 < b < 0.1 and b != 0:
            warnings.warn('Делитель близок к нулю', UserWarning)
    except UserWarning:
        print('')
    except ZeroDivisionError:
        print('На ноль делить нельзя')

divide_numbers(3, 0.01)
divide_numbers(3, 0.0)
divide_numbers(3, 0.001)

