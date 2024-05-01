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

warnings.simplefilter("always", UserWarning)
divide_numbers(3, 4)
divide_numbers(3, 8)
divide_numbers(3, 0)

warnings.simplefilter("ignore", UserWarning)
divide_numbers(3, 3)
divide_numbers(3, 0.0)
divide_numbers(3, 5)

warnings.simplefilter("error", UserWarning)
divide_numbers(6, 0)
divide_numbers(3, 0.0)
divide_numbers(3, 5)
