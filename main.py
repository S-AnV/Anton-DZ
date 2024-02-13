# Задание:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.

# Примечание:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three



def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        d = 2
        while result % d != 0:
            d += 1
        if d == result:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(*args):
    total = sum(args)
    return total

result = sum_three(2, 3, 6)
print(result)

# Консоль:
# Простое
# 11





