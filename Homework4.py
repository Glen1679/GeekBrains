# 1 задание
from sys import argv

# script_mame, arg_1, arg_2, arg_3 = argv
#
# for i in range(1,4):
#     argv[i] = int(argv[i])
#
# salary = (argv[1] * argv[2]) + argv[3]
#
# print(f'Salary = {salary}')

# 2 задание

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list2 = [el for el in my_list if el > my_list[(my_list.index(el)) - 1] and my_list.index(el) != 0]
print(my_list2)

# 3 задание

my_list3 = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list3)

# 4 задание

my_list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_list5 = [el for el in my_list4 if my_list4.count(el) == 1]
print(my_list5)

# 5 задание
from functools import reduce

my_list6 = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list6)


def mult(a, b):
    return a * b


print(reduce(mult, my_list6))

# 6 задание

import itertools

for el in itertools.count(int(input('Укажите число: '))):
    if el > 10:
      break
    else: print(el)

print('*' * 30)
print('Вторая часть задания')

my_list_7 = [1, 2, 3, 4, 5]
counter = 0

for el in itertools.cycle(my_list_7):
    print(el)
    counter +=1
    if counter > len(my_list_7)*2:
        break