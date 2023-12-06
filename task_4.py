print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

first_number, second_number, digit = ('', ) * 3
summ, count_number = (0, ) * 2

while first_number == '':
  try:
    first_number = int(input('Введите начальное число: '))
  except ValueError:
    print('Необходимо ввести число!!!')

while second_number == '':
  try:
    second_number = int(input('Введите конечное число: '))
  except ValueError:
    print('Необходимо ввести число!!!')

while digit == '':
  try:
    digit = int(input('Введите контрольное число: '))
    if digit < first_number or digit > second_number:
      print('Необходимо ввести число в диапазоне от начального до конечного!!!')
      digit = ''
  except ValueError:
    print('Необходимо ввести число!!!')

for count in range(first_number, second_number + 1):
  if count % digit == 0:
    summ += count
    count_number += 1
    
if count_number == 0:
  print('В диапазоне нет чисел, кратных контрольному числу')
else:
  print(f'Среднее арифметическое чисел из отрезка [{first_number}, {second_number}], кратных числу {digit}, равно {summ / count_number}'
  )
