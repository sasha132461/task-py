# 1) Переворот словаря
# Напишите функцию, которая принимает словарь и возвращает новый словарь, 
# в котором ключи и значения перевернуты местами

# print("key")
# y = input()
# print("value")
# x = input()
# SAS = dict()
# SAS = {
#     y: x}
# for key, value in SAS.items():
#    print(f"{key}:{value}")

# for key, value in SAS.items():
#    p = key
#    q = value
#    print(f"{q}:{p}")

# 2) Подсчет частоты слов
# Прочтите текст, введенный пользователем, и 
# подсчитайте частоту каждого слова в тексте. 
# Верните словарь, в котором ключи — это слова, 
# а значения — их частоты.

# print("Введите текст: ")
# text = input()
# letters = set()
# for n in text:
#     # set.add(element): Добавляет элемент element в множество.
#     letters.add(n)
# for n in letters:
#     # count(): исп. для подщета кол. вхождения как str
#     c = text.count(n)
#     print(f"{n}:{c}")

# 3) Объединение словарей
# Напишите функцию, которая принимает список словарей и объединяет 
# их в один словарь. Если одинаковый ключ встречается в нескольких 
# словарях, используйте значение из последнего словаря в списке.

print("Введите ключ в SAS: ")
a = input()
print("Введите значение в SAS: ")
b = input()
print("Введите ключ в SUS: ")
x = input()
print("Введите значение в SUS: ")
y = input()
SAS = dict()
SUS = dict()
SAS = {a: b}
SUS = {x: y}
  # update(): совмищает два списка в один
SAS.update(SUS)
print(SAS)

# 4) Максимальное произведение двух чисел
# Напишите функцию, которая принимает список чисел и возвращает 
# максимальное произведение двух чисел в этом списке.
# Пример: Если входной список [2, 5, -3, 7, 1], то максимальное 
# произведение двух чисел будет 35, так как 7 * 5 = 35.

# numbers = [1, 2, 3, 4, 5]
# max1_number = max(numbers)
# # remove(set): удаляє set з масиву
# numbers.remove(max1_number)
# max2_number = max(numbers)
# multi = max1_number * max2_number
# print("Умножение 2 максимальних чисел: ", multi)

# 5) Переместить нули в конец списка
# Дан список целых чисел. Напишите функцию, которая перемещает все 
# нули в конец списка, сохраняя порядок ненулевых элементов.

# numbers = [0, 2, 0, 4, 5, 0, 7, 8]
# numbers2 = []
# for n in numbers:
#     if n > 0:
#         numbers2.append(n)
#     elif n == 0:
#         numbers2.append(n)
# print(numbers2)

# 6) Проверка наличия дубликатов
# Напишите функцию, которая проверяет, содержит ли список дубликаты. 
# Ваша функция должна возвращать True, если дубликаты присутствуют, и 
# False в противном случае.

print("Введите кольора 5 м'ячей:")
colors_ball1 = str(input("1 м'яч:"))
colors_ball2 = str(input("2 м'яч:"))
colors_ball3 = str(input("3 м'яч:"))
colors_ball4 = str(input("4 м'яч:"))
balls = [colors_ball1, colors_ball2, colors_ball3, colors_ball4]
color = set()
for n in balls:
    # set.add(element): Добавляет элемент element в множество.
    color.add(n)
    # len(): подсчет кол елемента в обєкте
if len(color) < len(balls):
    True
else:
    False
if True:
    print("Есть дубликати")
elif False:
    print("Нету дубликантов")
