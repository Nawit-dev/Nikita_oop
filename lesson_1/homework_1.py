# ++++++++++++++++++++++++++++++++++++++
# Классы и атрибуты
# ++++++++++++++++++++++++++++++++++++++
# ======================================
# 1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.


class Dog:
    'Класс для создания разных видов собак'
    species = "canis"
    legs = 4
dog1 = Dog()
dog2 = Dog()


dog2.species = 'Мультипу'

print(dog1.species)
print(dog2.species)
print(Dog.species)
print(dog1.__dict__)
print(dog2.__dict__)
print()
print('Задание 2')

# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.

print(Dog.__doc__)
dog1.name = 'Лесси'
dog1.age = 24
print(dog1.name)
print(dog1.age)
del dog1.name
# print(dog1.name) - Получаем ошибку, т.к. данный атрибут удален
print()
print('Задание 3')

# 3. Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():
#
# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.

class User:
    role = "guest"
    active = True

setattr(User,'role', 'admin')
print(User.role)
print(getattr(User,'active'))
setattr(User,'email','test@yandex.ru')
print(User.email)
delattr(User,'role')
print(getattr(User,'role', 'не найден'))
print(User.__dict__)


