# Задача 1: Фабрика функций
def create_operation(operation):
    if operation == "multiplication":
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "division":
        def division(x, y):
            return x / y
        return division


my_func_multiplication = create_operation("multiplication")
print(my_func_multiplication(3, 2))

try:
    my_func_division = create_operation("division")
    print(my_func_division(18, 9))

    my_func_division = create_operation("division")
    print(my_func_division(18, 0))
except ZeroDivisionError as exc:
    print('Error:', exc)




# Задача 2 лямбда
multiply = lambda x: x ** 2
print(multiply(4))

def multiply_def(x):
   return x ** 2
print(multiply_def(4))





# Задача 3: Вызываемые oбъекты
class Rect:

   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
       return f'Стороны: {self.a}, {self.b} \nПлощадь: {self.a * self.b}'

area_of_a_rectangle = Rect(2, 4)
print(area_of_a_rectangle())