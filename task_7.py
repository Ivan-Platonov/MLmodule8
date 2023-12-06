print('Задача 7. Сумма ряда')

# Дано натуральное число N. Напишите программу для вычисления суммы N элементов последовательности по формуле 
# (-1)**n * 1/(2**n), где n — это порядковый номер элемента (расчёт начинается с нуля).

# Примеры расчётов

# При N = 4 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# Сумма равна:
# s=1- 12+14-18 = 5/8 = 0,625

# При N = 6 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# n = 4
# elem = (−1) ** 4 * (½) ** 4 = (1/16)
# n = 5
# elem = (−1) ** 5 * (½) ** 5 = (−1/32)
# Сумма равна:
# s = 1 − ½ + ¼ − ⅛ + 1/16 − 1/32 = 21/32 = 0,65625

# P. S. Не стоит выполнять расчёты каждого элемента вручную, используйте цикл.

from fractions import Fraction

number, result = ('',)*2
elem, summ = (0,)*2

def error_message():
  print('Необходимо ввести натуральное число!!!')

while number == '':
  try:
    number = int(input('Введите натуральное число: '))
    if number <= 0:
      error_message()
      number = ''
  except ValueError:
    error_message()

print(f'При N = {number} элементы выражения будут равны:')
for element in range(number):
  print(f'n = {element}')
  elem = (-1)**element * 1/(2**element)
  summ += elem
  if elem >= 0:
    print(f'elem = (−1) ** {element} * (1⁄2) ** {element} = {str(Fraction(elem))}')
  else:
    print(f'elem = (−1) ** {element} * (1⁄2) ** {element} = ({str(Fraction(elem))})')

  if element == 0:
    result += str(1)
  elif elem > 0:
    result += (' + ' + str(Fraction(elem)))
  elif elem < 0:
    result += (' - ' + str(str(Fraction(abs(elem)))))

print('Сумма равна:')
print(f's = {result} = {Fraction(summ)} = {float(summ)} ')
  