# ======================================
# 1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
# Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
# Создай два объекта и задай им разные значения. Выведи информацию по каждому.
# ======================================

class Person:
    name = 'Артем'
    age = 12
    def set_data(self, name,age:int):
        self.name = name
        self.age = age

    def get_data(self):
        return f'Имя: {self.name},Возраст: {self.age}'

person1 = Person()
person1.set_data('artem', 32)
person2 = Person()
person2.set_data('Инна',25)

print(person1.get_data())
print(person2.get_data())
print(id(person1))
print(id(person2))
print('Задание 2')
# 2. Добавь в класс Point методы set_coords(x, y) и get_coords().
# Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
# После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().

class Point:
    x = 7
    y =12
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        return  self.x, self.y

p = Point()
print(p.get_coords())
p.set_coords(3,2)
print(p.get_coords())
print('Задание 3')

# 3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
# Проверь, что результат совпадает с обычным вызовом p.get_coords().

r = getattr(p, 'get_coords')
print(r())
print('Задание 4  и 5 ')
# ======================================
# 4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
# Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
# ======================================
# ======================================
# 5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
# где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
# ======================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        return f'Имя: {self.name},Возраст: {self.age}'
    # def __del__(self):
    #     print(f'Удален объект {self.name}')

mark = Person('Mark', 233)
print(mark.show_info())
print('Задание 6')

# ======================================
# 6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
# Добавь метод area(), который возвращает площадь прямоугольника.
# Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
# ======================================

class Rectangle:
    def __init__(self, width: int = 1, height: int =1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

result = Rectangle()
print(result.area())

result = Rectangle(5,3)
print(result.area())

# ======================================
# 7. Создай класс Logger, который всегда возвращает один и тот же объект.
# При создании экземпляра в __new__ выводи Создание логгера,
# а при вызове __init__ — Инициализация логгера.
# ======================================

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Создание логгера")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Инициализация логгера")


# Пример использования
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # True


