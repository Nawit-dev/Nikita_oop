
# ======================================
# 1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле.
# ======================================
# class Cat:
#     def speak(self):
#         return 'Мяу!'
#
# class Dog:
#     def speak(self):
#         return 'Гав!'
#
# class Duck:
#     def speak(self):
#         return 'Кря!'
#
#
# animals = [Cat(),Dog(),Duck()]
#
# for animal in animals:
#     print(animal.speak())
# print('\nЗадание 2')
# # ======================================
# # 2. Создай базовый класс Shape
# # Создай три класса-наследника: Square, Rectangle, Triangle,
# # в каждом реализуй метод get_pr().
# # Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# # можно обойти в цикле и вызвать get_pr() у каждого.
# # ======================================
#
#
# class Shape:
#     pass
#
# class Square(Shape):
#     def get_pr(self):
#         return 'test 1'
# class Rectangle(Shape):
#     def get_pr(self):
#         return 'test 2'
# class Triangle(Shape):
#     def get_pr(self):
#         return 'test 3'
#
#
# shapes = [Square(), Rectangle(), Triangle()]
#
# for shap in shapes:
#     print(shap.get_pr())
# print('\nЗадание 3')
#
# # ======================================
# # 3. Сделай класс Shape абстрактным.
# # Переопредели get_pr() как @abstractmethod.
# # Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
# # ======================================
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_pr(self):
#         return 'test Shape'
#
# class Square(Shape):
#     def get_pr(self):
#         return 'test 1'
# class Rectangle(Shape):
#     def get_pr(self):
#         return 'test 2'
# class Triangle(Shape):
#     def get_pr(self):
#         return 'test 3'
#
#
# # shapes = Shape()
# # print(shapes)
# print('\nЗадание 4')
# # ======================================
# # 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# # Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# # Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
# # ======================================
#
#
# class A:
#     def __init__(self):
#         super().__init__()
#         print("init A")
# class B:
#     def __init__(self):
#         super().__init__()
#         print("init B")
# class C:
#     def __init__(self):
#         super().__init__()
#         print("init C")
#
# class D(A, B, C):
#     def __init__(self):
#         super().__init__()
#         print("init D")
#
# d = D()
# print(D.__mro__)
# print('\nЗадание 5')
#
# # ======================================
# # 5. Создай MixinLog (как в уроке).
# # Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
# # Создай класс, который наследует оба класса. Создай экземпляр этого класса.
# # ======================================
#
# class MixinLog:
#     def log(self,message):
#         print(f'[Log]: {message}')
# class HotelBooking(MixinLog):
#     def __init__(self, guest_name, room_number, nights, price_per_night):
#         self.guest_name = guest_name
#         self.room_number = room_number
#         self.nights = nights
#         self.price_per_night = price_per_night
#         self.is_confirmed = False
#         self.log(f'Отель бронирует {guest_name}') #MixinLog
#
#     def total_price(self):
#         """Рассчитывает общую стоимость проживания"""
#         return self.nights * self.price_per_night
#
#     def confirm_booking(self):
#         """Подтверждает бронирование"""
#         self.is_confirmed = True
#         print(f"Бронирование для {self.guest_name} подтверждено. Номер {self.room_number}.")
#         self.log(f'Бронирование для {self.guest_name} подтверждено. Номер {self.room_number}.') #MixinLog
#     def cancel_booking(self):
#         """Отменяет бронирование"""
#         self.is_confirmed = False
#         print(f"Бронирование для {self.guest_name} отменено.")
#
#     def info(self):
#         """Выводит информацию о бронировании"""
#         status = "Подтверждено" if self.is_confirmed else "Ожидает подтверждения"
#         return (f"Гость: {self.guest_name}\n"
#                 f"Номер: {self.room_number}\n"
#                 f"Ночей: {self.nights}\n"
#                 f"Цена за ночь: {self.price_per_night} руб.\n"
#                 f"Статус: {status}\n"
#                 f"Итого: {self.total_price()} руб.")
#
# class Goods(HotelBooking, MixinLog):
#     def __init__(self, guest_name, room_number, nights, price_per_night):
#         super().__init__(guest_name, room_number, nights, price_per_night)
#
# booking1 = Goods("Иван Иванов", 203, 3, 4500)
# print(booking1.info())
# booking1.confirm_booking()
# print(booking1.info())
# print('\nЗадание 6')
#
# # ======================================
# # 6. В Goods и MixinLog реализуй print_info().
# # Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# # Измени порядок наследования — изменилась ли логика?
# # ======================================
#
# class MixinLog:
#     def info(self,text_info):
#         print(f'[INFO]: {text_info}')
# class Goods(MixinLog):
#     def __init__(self,text):
#         self.text = text
#         self.info(f'Информация выведена: {self.text}')
# class NoteBook(Goods, MixinLog): #Если поменять местами, то будет ошибка TypeError, т.к. в MixinLog нет __init__
#     pass
#
# d = NoteBook('Завтра будет дождь')
# print('\nЗадание 7')
#
# # ======================================
# # 7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# # Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# # и выведи сообщение: "На ноль делить нельзя!"
# # ======================================
#
# def numbers(a:int,b:int):
#     try:
#         return round(a / b)
#     except ZeroDivisionError: return 'На ноль делить нельзя!'
#     except ValueError: return  'Ошибка ввода: введите два числа через пробел'
#
# # a = int(input('Введите первое число '))
# # b = int(input('Введите второе число '))
# # print(numbers(a, b))
#
# # ======================================
# # 8. Расширь программу из Задания 1:
# # Добавь обработку ошибки (как называется ошибка найди сам),
# # если пользователь ввёл не числа, а текст.
# # Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
# # ======================================
#
#
# def numbers(a:int,b:int):
#     try:
#         return round(a / b)
#     except ZeroDivisionError: return 'На ноль делить нельзя!'
#
# try:
#     a,b = map(int, input('Введите два числа через пробел: ').split())
#     print(numbers(a,b))
# except ValueError:
#     print('Ошибка ввода: введите два числа через пробел')
#
#
# # ======================================
# # 9. Модифицируй код так, чтобы после обработки конкретных ошибок
# # был ещё один общий except, который перехватывает все остальные ошибки и выводит:
# # "Произошла неизвестная ошибка"
# # ======================================
#
#
# def numbers(a: int, b: int):
#     try:
#         return round(a / b)
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'
#
# try:
#     a, b = map(int, input('Введите два числа через пробел: ').split())
#     print(numbers(a, b))
# except ValueError:
#     print('Ошибка ввода: введите два числа через пробел')
#
# except Exception:
#     print('Произошла неизвестная ошибка')
#
#
# # ======================================
# # 10. При перехвате исключений из 7 и 8 заданий,
# # сохрани ошибку в переменную e и выведи её текст:
# # ======================================
# def numbers(a:int,b:int):
#     try:
#         return round(a / b)
#     except ZeroDivisionError as e:
#         print(e)
#         return 'На ноль делить нельзя!'
#
# try:
#     a,b = map(int, input('Введите два числа через пробел: ').split())
#     print(numbers(a,b))
# except ValueError as v:
#     print(v)
#     print('Ошибка ввода: введите два числа через пробел')

# ======================================
# 11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
# Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
# ======================================


try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    print(a/b)
except ArithmeticError:
   print('Нельзя делить на ноль')
except ValueError:
    print("Нужно вводить только числа")


# ======================================
# 12. Запроси у пользователя два числа и выполни деление.
# Если деление прошло успешно без ошибок — выведи
# "Деление выполнено успешно" через (но не в блоке try)
# ======================================
# ======================================
# 13. Расширь код из Задания 12:
# Добавь блок, в котором будет выводиться
# "Работа программы завершена", независимо от успеха деления.
# ======================================

try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    print(a/b)
except ArithmeticError:
   print('Нельзя делить на ноль')
else:
    print("Деление выполнено успешно")
print('Работа программы завершена') #Задание 13

# ======================================
# 14. Реализуй две вложенные конструкции:
# Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
# Внутренний try/except ловит деление на ноль.
# ======================================

try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    print(a/b)
except ValueError:
    print("Нужно вводить только числа")
except:
    try:
        print(a / b)
    except ArithmeticError:
        print('Нельзя делить на ноль')

# ======================================
# 15. Вынеси обработку деления в отдельную функцию divide(x, y)
# с собственным try/except.
# Во внешнем коде обработай только ошибку ввода.


def divide(x, y):
    try:
        print(x / y)
    except ArithmeticError:
        print('Нельзя делить на ноль')

try:
    x = int(input("Введите число: "))
    y = int(input("Введите число: "))
    divide(x,y)
except ValueError:
    print("Нужно вводить только числа")

























