print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys, girls, result_boys, result_girls, result = ('', ) * 5
index = 0


def error_message():
  print('Необходимо ввести натуральное число!!!')


while boys == '':
  try:
    boys = int(input('Введите кол-во мальчиков: '))
    if boys < 0:
      error_message()
      boys = ''
  except ValueError:
    error_message()

while girls == '':
  try:
    girls = int(input('Введите кол-во девочек: '))
    if girls < 0:
      error_message()
      girls = ''
  except ValueError:
    error_message()

#Строим две строки с символами малчиков и девочек
for elem in range(boys):
  result_boys += 'B'
for elem in range(girls):
  result_girls += 'G'

#Строим общую строку в зависимости от количества мальчиков и девочек
if boys >= girls:
  for element in range(boys):
    if element < girls:
      result += result_boys[element] + result_girls[element]
    else:
      result += result_boys[element]
elif girls > boys:
  for element in range(girls):
    if element < boys:
      result += result_girls[element] + result_boys[element]
    else:
      result += result_girls[element]
      
#Если в конце строки есть повторяющиеся символы, перемещаем последний с конца строки в соответствующее место для соблюдения соседства мальчиков и девочек по условию задачи. 
#Как только перместить символ с конца строки невозможно при соблюдении условия соседства, выводим сообщение и прерываем цикл
if boys > girls:
  while (result[-2:] == 'BB'):
    index = result.rfind('GBG')
    if index >= 1:
      result = result[:(index + 1)] + 'B' + result[(index + 1):]
      result = result[:-1]
    if index == -1:
      print('Ответ: Нет решения')
      break
elif girls > boys:
  while (result[-2:] == 'GG'):
    index = result.rfind('BGB')
    if index >= 1:
      result = result[:(index + 1)] + 'G' + result[(index + 1):]
      result = result[:-1]
    if index == -1:
      print('Ответ: Нет решения')
      break

print()
if index > 0:
  print(f'Ответ: {result}')
