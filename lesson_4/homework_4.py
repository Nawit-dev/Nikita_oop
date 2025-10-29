# ======================================
# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"
# ======================================
class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == '__secret':
            raise ValueError(f'Доступ к атрибуту - {name} извне запрещен')
        return object.__getattribute__(self, name)

    def get_secret(self):
        return self.__secret

data = SecureData("пароль123")
print(data.get_secret())  # "пароль123"
print(data.__secret)      # ошибка


# ======================================
# 2. Добавь в класс SecureData метод __setattr__,
# который запрещает создание любого атрибута с именем token.
#
# Проверь:
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает
# ======================================

class SecureData:
    def __init__(self, secret):
        self.__secret = secret
    def __getattribute__(self, name):
        if name == '__secret':
            raise ValueError(f'Доступ к атрибуту - {name} извне запрещен')
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        if key == 'token':
            raise AttributeError(f'Запрет на создание атрибута - {key}')
        print(value)
        object.__setattr__(self, key, value)


    def get_secret(self):
        return self.__secret

data = SecureData("пароль123")
print(data.get_secret())  # "пароль123"
print(data.__secret)      # ошибка
data.other = "ok"      # ✅ работает
data.token = "abc123"  # ❌ AttributeError


# ======================================
# 3. Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"
# ======================================

class SafeDict:
    def __getattr__(self, name):
        return "N/A"
    def __delattr__(self, name):
        print(f'Удален атрибут {name}')

d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"

# ======================================
# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError
# ======================================
# 5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:
#
# del e.salary
# print(e.__dict__)  # salary нет

class Employee:

    def __init__(self, name,salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError(f'{self.__salary} не может быть отрицательным')
        self.__salary = value
    @salary.deleter
    def salary(self):
        print('зарплата удалена')
        del self.__salary


e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError
del e.salary
print(e.__dict__)  # salary нет


# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"

class LoginForm:

    def __init__(self):
        self._username = None

    @property
    def username(self):
        return self._username

    @username.setter
    def  username(self,value):
        print(f'{value} изменён')
        self._username = value


form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"


# 7. Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.

from datetime import datetime
class Card:

    def __init__(self):
        self.__number = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self,value):
        if len(value) == 16:
            r = '************' + value[12:]
            r1 = [r[0:4], r[4:8], r[8:12], r[12:]]
            result = ' '.join(r1)
            self.__number = result
        else:
            raise ValueError("Номер карты должен состоять из 16 цифр")

    @number.deleter
    def number(self):
        print(f"[INFO] {datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')}"
              f' Был удален номер {self.__number}')
        del self.__number

e = Card()
e.number = '1234567891011124'
assert e.number == "**** **** **** 1124"
# print(e.number)
# del e.number
try:
    e.number = "1234"
except ValueError:
    pass
else:
    raise AssertionError("Ошибка не была вызвана при коротком номере")

print(e.number)
# # Проверка deleter
del e.number


# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.


class UserData:

    def __init__(self, email:str,age:int, is_active):
        if '@'not in email:
            return ValueError("Некорректный email")
        if age >= 18:
            return ValueError('Некорректное число')
        self.__email = email
        self.__age = age
        self.__is_active = is_active

    @property
    def json(self):
        return {
            "email": self.__email,
            "age": self.__age,
            "is_active": self.__is_active
        }


# Проверка ошибки при age < 18
try:
    UserData("test@example.com", 15, True)
    assert False, "ValueError не выброшен при возрасте < 18"
except ValueError:
    pass

# Проверка ошибки при неправильном email
try:
    UserData("invalid_email", 25, True)
    assert False, "ValueError не выброшен при некорректном email"
except ValueError:
    pass

# Проверка корректности json
user = UserData("test@example.com", 30, True)
assert user.json == {
    "email": "user@example.com",
    "age": 30,
    "is_active": True
}















