# ======================================
# 1. Создай класс LengthValidator, который:
# принимает в __init__ минимальную и максимальную длину строки;
# в __call__ проверяет, что длина переданной строки в заданном диапазоне;
# выбрасывает ValueError, если условие не выполнено.
# Пример:
# validator = LengthValidator(3, 10)
# print(validator("python"))  # True
# print(validator("hi"))      # ValueError
# ======================================


class LengthValidator:

    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, str_len):
        if self.min_len < len(str_len) <= self.max_len:
            return f'Длинна слова в {len(str_len)} символов находится между диапазоном {self.min_len} и {self.max_len}'
        else:
            return ValueError('Условие не выполнено')

validator = LengthValidator(3, 10)
print(validator("python"))  # True
print(validator("hi"))      # ValueError


# 2. Создай класс Sumator, который:
# при первом вызове принимает число;
# каждый следующий вызов увеличивает сумму;
# хранит и возвращает текущую сумму.
# Пример:
# s = Sumator()
# print(s(5))   # 5
# print(s(10))  # 15
# print(s(-2))  # 13


class Sumator:

    def __init__(self):
        self.count = 0
    def __call__(self,number:int):
        self.count += number
        return self.count

s = Sumator()
print(s(5))  # 5
print(s(10))  # 15
print(s(-2))  # 13


# ======================================
# 3. Создай класс HasText, который:
# в __init__ принимает ожидаемую подстроку;
# в __call__ принимает текст и возвращает True, если подстрока найдена.
# Подумай как сделать так, чтобы работало как и в примере?
# Пример:
# assert HasText("Success")("Test passed: Success")  # True
# assert HasText("Error")("All OK")  # False
# ======================================

class HasText:

    def __init__(self,substring:str):
        self.substring = substring

    def __call__(self,text:str):
       return self.substring in text


assert HasText("Success")("Test passed: Success")  # True
# assert HasText("Error")("All OK") # False


# ======================================
# 4. Создай класс Book, который хранит:
# название книги (title)
# автора (author)
# Переопредели __str__ и __repr__, чтобы:
# print(book) выводил "Автор — Название"
# repr(book) показывал <Book 'Название' by Автор>
# Пример:
# book = Book("1984", "Джордж Оруэлл")
# print(book)         # Джордж Оруэлл — 1984
# print(repr(book))   # <Book '1984' by Джордж Оруэлл>
# ======================================


class Book:

    def __init__(self,title:str,author:str,):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.author} - {self.title}'

    def __repr__(self):
        return f'<Book "{self.title}" by {self.author}>'


book = Book("1984", "Джордж Оруэлл")
print(book)         # Джордж Оруэлл — 1984
print(repr(book))   # <Book '1984' by Джордж Оруэлл>

# 5. Создай класс TestUser, который содержит id, name, email.
# Переопредели __repr__, чтобы его было удобно видеть в логах автотеста:
# user = TestUser(12, "Daniil", "daniil@example.com")
# print(user)
# # <TestUser id=12 name='Daniil' email='daniil@example.com'>

class TestUser:

    def __init__(self,id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<TestUser  id={self.id} name="{self.name}" email="{self.email}">'

user = TestUser(12, "Daniil", "daniil@example.com")
print(u