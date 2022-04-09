# # 3 задание
#
# x = int(input('Введите значение X: '))
# y = 0
#
# if x > 0:
#     y = x - 12
# elif x == 0:
#     y = 5
# else:
#     y = x ** 2
#
# print(f'Игрик равен: {y}')
#
# # 4 задание
#
# student_number = int(input('Введите место в списке поступающих: '))
# student_score = int(input('Введите свой результат: '))
#
# if student_number < 10:
#     print('Вы поступили!')
#     if student_score > 290:
#         print('Бонусом вам будет начисляться стипендия.')
#     else:
#         print('Но вам не хватило баллов для стипендии.')
# else:
#     print('Вы не поступили')

# # 5 задание
#
# rating = int(input('Что получил по математике? '))
#
# if rating == 2 or rating == 3:
#     print('Плохо. Марш учиться!')
# else:
#     print('Молодец! Можешь отдохнуть')

# # 6 задание
#
# number = int(input('Введите число: '))
#
# if (number // 10) != 0 and abs(number // 10) < 10:
#     print('Число двузначное')
# else:
#     print('Число не двузначное')

# # 7 задание
#
# simbol_1 = int(input('Введите первое число: '))
# simbol_2 = int(input('Введите второе число: '))
# simbol_3 = int(input('Введите третье число: '))
# counter = 1
#
# if simbol_1 == simbol_2:
#     counter += 1
#     if simbol_2 == simbol_3:
#         counter += 1
# else:
#     print('Ни одного совпадения')
# if counter > 1:
#     print(f'Совпадают {counter} символа')

# # 8 задание
#
# square = int(input('Введите площадь: '))
# cost = int(input('Введите стоимость квартиры: '))
#
# if square > 100 and cost < 10000:
#     print('Квартира соответствует')
# elif square > 80 and cost < 7000:
#     print('Квартира подходит')
# else:
#     print('Квартира не подходит')

# # 9 задание
#
# wage = int(input('Введите зарплату: '))
# tax = 0
#
# if wage > 10000:
#     tax = 10000 * 0.13
#     if wage > 50000:
#         tax += 40000 * 0.2
#         tax += (wage - 50000) * 0.3
#     else:
#         tax += (wage - 10000) * 0.2
# else:
#     tax = wage * 0.13
# print(f'Сумма налога составляет: {tax}')

# # 10 задание
#
# time = int(input('Введите время: '))
#
# if (time >= 8 and time < 10) or (time > 12 and time < 14) or (time > 15 and time < 18) or (time > 20 and time <= 22):
#     print('Почта работает')
# else:
#     print('Почта закрыта')
#
# if time < 8 or (time >= 10 and time <= 12) or (time >= 14 and time <= 15) or (time >= 18 and time <= 20) or time > 22:
#     print('Почта закрыта')
# else:
#     print('Почта открыта')
