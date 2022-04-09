# 1 задание
# name = input('Введите имя: ')
# number = int(input('Введите число: '))
#
# print(type(name))
# print(type(number))
# print(f'Пользователь ввел имя {name} и число {number}')

# 2 задание
user_time = abs(int(input('Введите время в секундах: ')))
user_hour = 0
user_min = 0

if (user_time // 3600) >= 1:
    user_hour = user_time // 3600
    user_time = user_time - user_hour * 3600

if (user_time // 60) >= 1:
    user_min = user_time // 60
    user_time = user_time - user_min * 60

print(f'{user_hour}:{user_min}:{user_time}')

# 3 задание
# number_n = int(input('Введите число: '))
# i=1
# result = []
# x=0
#
# while i<= number_n:
#     x = number_n * 10 ** (i-1) + x
#     result.append(x)
#     i+=1
# number_n_sum = sum(result)
#
# print(result)
# print(f'сумма составила: {number_n_sum}')

# 4 задание

number_m = input('Введите целое положительное число:')
m = 0
result_m = []

while m < len(number_m):
    number_m_digit = int(number_m[m])
    result_m.append(number_m_digit)
    m+=1

print(result_m)
result_m_min = 0
q=0
while q < len(result_m):
    if result_m_min < result_m[q]:
        result_m_min = result_m[q]
    q+=1

print(f'Максимальное число: {result_m_min}')
#max_m_digit = max(result_m)
#print(max_m_digit)

# 5 задание
# income = int(input('Введите выручку: '))
# costs = int(input('Введите затраты: '))
#
#
# if income > costs:
#     income_index = income / costs
#     empl = int(input('Введите количество сотрудников: '))
#     empl_income = income/empl
#     print(f'Фирма прибыльна, рентабельность составила {income_index}. \nПрибыль на одного сотрудника составила {empl_income}')

# 6 задание
a = float(input('Введите результат 1 дня: '))
b = float(input('Введите пороговый результат: '))
day_number = 1

while a <= b:
    #print(a)
    a = a * 1.1
    day_number += 1

print(f'Результат достигнут на {day_number} день')






