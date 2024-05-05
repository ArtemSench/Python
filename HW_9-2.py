def create_operation(operation):
    if operation == "mult":
        def mult(x, y):
            return x * y
        return mult
    elif operation == "devision":
        def division(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                print('На ноль делить нельзя')

        return division
my_func_mult = create_operation("mult")
my_func_dev = create_operation("devision")

print(my_func_mult(5,4))
print(my_func_dev(8, 4))
print(my_func_dev(7,0))

squar = lambda x: x ** 2
print(squar(3))

def squaring(x):
   return x ** 2
print(squaring(3))

class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
       return self.a * self.b

rectangle = Rect(5, 7)
print(rectangle())
