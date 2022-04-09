# 1 задание

my_list = [1, 1.2, None, True, 'Text', ['list'], {'key_1':'Val_1'}]

for itam in my_list:
    print(type(itam))

# 2 задание
my_list2 = input('Введите элементы списка через запятую: ')
my_list2 = my_list2.split(',')
print(my_list2)

my_list2_len = len(my_list2) if len(my_list2) % 2 ==0 else len(my_list2)-1
i=0

while i <= my_list2_len-1:
    if i%2 ==0:
        my_list2[i], my_list2[i+1] = my_list2[i+1], my_list2[i]
        i+=1
    else:
        i+=1

print(my_list2)

# 3 задание

month = {'1':'winter', '2':'winter', '3':'spring', '4':'spring', '5':'spring', '6':'summer', '7':'summer', '8':'summer', '9':'autumn', '10':'autumn', '11':'autumn', '12':'winter'}
try:
    print(month[input('Введите номер месяца: ')])
except KeyError:
    print(f'Такого номера месяца не существует')

try:
    month_input = int(input('Введите номер месяца: '))
except:
    print(f'Такого номера месяца не существует')
    month_input = int(input('Введите номер месяца заново: '))

winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]

if month_input in winter:
    print("Winter")
elif month_input in spring:
    print('Spring')
elif month_input in summer:
    print('Summer')
elif month_input in autumn:
    print('Autumn')
else: print(f'Такого номера месяца не существует')

# 4 задание
str = input('Введите строку: ')

str_list = str.split(' ')
print(str_list)

print(str_list[1])

i=0
while i<len(str_list):
    print(f'{i+1}. {str_list[i][:10]}')
    i+=1

# 5 задание
my_list5 = [7,5,3,3,2]
tuple(my_list5)

am_inputs = int(input('Введите количество вводов в рейтинг: '))
q = 1
print(type(q))
print(type(am_inputs))

while q <= am_inputs:
    user_input = int(input('Введите значение в рейтинг: '))
    result = sorted([user_input] + (my_list5), reverse=True)
    q+=1
    print(result)

# 6 задание

import sys
import os
import json

with open('goods_base.jon', 'r') as f:
    lines = (f.readlines())

def add_good():
    goods_dict = {}
    goods_dict['Название'] = input('Введите название товара: ')
    goods_dict['Цена'] = int(input('Введите цену товара: '))
    goods_dict['Количество'] = int(input('Введите количество товара: '))
    goods_dict['Единицы измерения'] = input('Введите единицы измерения товара: ')
    new_good = (len(lines) + 1,goods_dict)
    print(type(new_good))
    json_new_good = json.dumps(new_good)
    with open('goods_base.jon', 'a',encoding='utf-8') as f:
        json.dump(new_good,f)
        f.write('\n')

print(len(lines))

add_good()


with open('goods_base.jon', 'r') as f:
    for line in lines:
        goods = tuple(json.loads(line))
        print(goods)

print(len(lines))

names = []
with open('goods_base.jon', 'r') as f:
    for line in lines:
        goods = tuple(json.loads(line))
        names.append(goods[1]['Название'])

price = []
with open('goods_base.jon', 'r') as f:
    for line in lines:
        goods = tuple(json.loads(line))
        price.append(goods[1]['Цена'])

ammount = []
with open('goods_base.jon', 'r') as f:
    for line in lines:
        goods = tuple(json.loads(line))
        ammount.append(goods[1]['Количество'])

units = []
with open('goods_base.jon', 'r') as f:
    for line in lines:
        goods = tuple(json.loads(line))
        units.append(goods[1]['Единицы измерения'])


analis = {
    'Название':[names],
    'Цена':[price],
    'Количество':[ammount],
    'Единицы измерения':[units]
}
for key,val in analis.items():
    print(key, val[0])  # не понял почему у меня массив вложен в массив, откуда второй массив взялся???

