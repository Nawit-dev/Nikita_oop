import time


# ======================================
# 1. Создай две функции: inner() и outer().
# В inner() вызови деление на ноль.
# В outer() просто вызови inner().
# Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
# ======================================

# ======================================
# def inner():
#     raise ZeroDivisionError('Деление на ноль')
#
# def outer():
#     inner()
#
# outer()
# print('\nЗадание 2')


# ======================================
# 2. Добавь вокруг вызова outer() конструкцию try/except,
# чтобы перехватить исключение и вывести сообщение
# "Ошибка перехвачена на верхнем уровне".
# ======================================
def inner():
    raise ZeroDivisionError('Деление на ноль')

def outer():
    inner()

try:
    outer()
except Exception:
    print('Ошибка перехвачена на верхнем уровне')
print('\nЗадание 3')

# ======================================
# 3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
# В случае ошибки возвращай строку "Ошибка в inner".
# ======================================

def inner():
    try:
        raise ZeroDivisionError('Деление на ноль')
    except ZeroDivisionError:
        print('Ошибка в inner')

def outer():
    inner()

outer()
print('\nЗадание 4')

# ======================================
# 4. Сделай так:
# В inner() ошибка не перехватывается.
# В outer() ошибка перехватывается через try/except.
# В outer() при перехвате напечатай "Ошибка в outer".
# ======================================

def inner():
        raise ZeroDivisionError('Деление на ноль')

def outer():
    try:
        inner()
    except ZeroDivisionError:
        print('Ошибка в outer')
outer()
print('\nЗадание 5')

# ======================================
# 5. Напиши функцию get_value(), которая кидает ValueError.
# Напиши тестовую функцию test_get_value(), которая:
#
# Вызывает get_value();
# Ловит ValueError;
# Завершает тест с assert False, если исключение поймано.
# ======================================

# def get_value():
#     raise ValueError
#
# def test_get_value():
#     try:
#         get_value()
#     except ValueError:
#         assert False
#
# test_get_value()
print('\nЗадание 6')
# ======================================
# 6. Создай функцию divide(x, y).
# Если y == 0, выбрасывай ZeroDivisionError через raise.
# Иначе возвращай результат деления.
# ======================================

# def divide(x, y):
#     if y == 0:
#         raise ZeroDivisionError('Деление на ноль')
#     else:
#         return x/y
#
# result = divide(4,0)
# print(result)
print('\nЗадание 7')

# ======================================
# 7. Создай функцию sqrt(x), которая:
# Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
# Иначе возвращает квадратный корень из x.
# Проверь поведение функции через try/except.
# ======================================


import math

class NegativeNumberError(Exception):
    """пользовательское исключение"""
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError('NegativeNumberError')
    else:
        return math.sqrt(x)
try:
    result = sqrt(-1)
    print(result)
except NegativeNumberError:
    print('Ошибка')
print('\nЗадание 8')

# ======================================
# 8. Создай базовый класс MathError.
# От него унаследуй:
# NegativeNumberError
# DivisionByZeroError
# В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
# Проверь в try/except обработку ошибок через базовый класс MathError.
# ======================================

class MathError:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class NegativeNumberError(MathError):
    def safe_divide(self):
        if self.y < 0:
            raise DivisionByZeroError(f'{self.y} < 0')
        else:
            return self.x / self.y


class DivisionByZeroError(MathError, Exception):
    '''DivisionByZeroError'''
    pass

try:
    result = MathError(4,0)
    print(result)
except DivisionByZeroError:
    print('Возникла ошибка DivisionByZeroError')
print('\nЗадание 9')
# ======================================
# 9. Создай тестовую функцию test_sqrt(), которая:
# вызывает sqrt(x) с отрицательным числом;
# перехватывает NegativeNumberError;
# завершает тест с assert False и сообщением
# "Нельзя брать корень из отрицательного числа".
# ======================================


class MathError(Exception):
    def __init__(self, x:int):
        self.x = x

class NegativeNumberError(MathError):
    def __str__(self):
        return f"Нельзя брать корень из отрицательного числа {self.x}"


def sqrt(x):
     if x < 0:
         raise NegativeNumberError(x)
     else:
         return x ** 0.5


def test_sqrt():
    try:
        sqrt(-10)
        assert False,"Нельзя брать корень из отрицательного числа"
    except NegativeNumberError as e:
        return  f'{e}'
result = test_sqrt()
print(result)
print('\nЗадание 10')

# ======================================
# 10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
# Обеспечь закрытие файла через with.
# ======================================

with open('sample.txt', 'r', encoding = 'utf8')as f:
    for i in f:
        print(i, end='')

print('\nЗадание 11')


# ======================================
# 11. Создай класс BackupList, который:
# делает копию списка при входе в with,
# при выходе сохраняет изменения, если ошибок не было,
# откатывает изменения при ошибке.
# Проверь:
# успешное изменение списка;
# откат при ошибке.
# ======================================


class BackupList:
    def __init__(self, data: list):
        self.data = data

    def __enter__(self):
        self._backup = self.data.copy()
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.data[:] = self._backup
            print("Ошибка! Изменения откатились.")
        else:
            print("Изменения сохранены.")
        return False



nums = [1, 2, 3]
try:
    with BackupList(nums) as bl:
        bl.append(4)
    print("После успешного изменения:", nums)
except Exception as e:
    print("Ошибка:", e)


nums = [10, 20, 30]
try:
    with BackupList(nums) as bl:
        bl.append(99)
        raise ValueError("Что-то пошло не так!")  # искусственная ошибка
except Exception as e:
    print("Ошибка поймана:", e)

print("После ошибки:", nums)


# ======================================
# 12. Создай декоратор-класс Timer,
# который измеряет время выполнения функции и выводит результат.

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения {self.func.__name__}: {end - start:.5f} сек")
        return result


@Timer
def slow_function():
    time.sleep(2)
    print("Функция выполнена")

slow_function()





























