def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    obj_module = obj.__class__.__module__

    # Собираем информацию в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }

    return info


# Пример создания своего класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)


# Создаем объект класса
my_object = MyClass(10)

# Получаем информацию об объекте
object_info = introspection_info(my_object)
print(object_info)

# Проверяем информацию о числе
number_info = introspection_info(42)
print(number_info)