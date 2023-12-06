print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.


# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.
def error_message():
  print('Необходимо ввести положительное число!!!')


stocks, monthes = ('', ) * 2
stocks_monthes = 0

while stocks == '':
  try:
    stocks = int(input('Сколько мешков гречки спасено?: ')) * 100
    if stocks < 0:
      error_message()
      stocks = ''
  except ValueError:
    error_message()

stocks_monthes = int(stocks / 4)

while monthes == '':
  try:
    monthes = int(input('Сколько прошло месяцев?: '))
    if monthes < 0:
      error_message()
      monthes = ''
    elif monthes > stocks_monthes:
      print('Уже ничего не осталось!')
      break
  except ValueError:
    error_message()
    
stocks -= monthes * 4

if monthes <= stocks_monthes:
  for month_count in range(monthes, stocks_monthes):
    if stocks == 4:
      print(
        f'По истечении {month_count} месяцев после крушения гречки осталось на ОДИН месяц!!!'
      )
    elif stocks < 4 and stocks > 0:
      print('Гречки не хватит даже на месяц!!!')
    elif stocks > 4:
      print(
        f'По истечении {month_count} месяцев после крушения остаток гречки {stocks} кг'
      )
    stocks -= 4
  print(f'Гречки было спасено на {month_count + 1} месяцев')