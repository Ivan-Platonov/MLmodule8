print('Задача 5. Функция')

# Перед изучением функций из программирования Саша решил оживить свои знания о функциях математики. Помогите Саше написать программу, которая будет считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца).
# Напишите программу, которая получает на вход начало и конец отрезка, а также шаг (отрицательный), а затем высчитывает функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.

# Сама функция выглядит так:
# y = x**3 + 2*x**2 - 4*x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

first_number, second_number, step_value = ('',)*3
result = 0
points_is_same = False

while first_number == '':
  try:
    first_number = int(input('Введите начало отрезка: '))
  except ValueError:
    print('Необходимо ввести число!!!')

while second_number == '':
  try:
    second_number = int(input('Введите конец отрезка: '))
  except ValueError:
    print('Необходимо ввести число!!!')

def take_step_value():
  global step_value
  while step_value == '':
    try:
      step_value = int(input('Введите значение шага: '))
      if abs(step_value) > abs(first_number) + abs(second_number):
        print('Необходимо ввести число, не превышающее по модулю размерность диапазона!!!')
        step_value = ''
    except ValueError:
      print('Необходимо ввести число!!!')
  if step_value > 0:
    step_value = -step_value

if first_number > second_number:
  start = first_number
  stop = second_number
  take_step_value()
elif first_number < second_number:
  start = second_number
  stop = first_number
  take_step_value()
else:
  points_is_same = True

if points_is_same:
  result = first_number**3 + 2*first_number**2 - 4*first_number + 1
  print(f'В точке {first_number} функция равна {result}')
else:
  for step in range(start, stop - 1, step_value):
    result = step**3 + 2*step**2 - 4*step + 1
    print(f'В точке {step} функция равна {result}')