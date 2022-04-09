#1 задание
import json
import os
with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input("Введите текст: ")
        if text == '':
            break
        else:
            f.writelines(f'{text}\n')

# 2 задание

with open('text.txt', 'r', encoding='utf-8') as f:
    f_text = f.readlines()
    #print(f_text)
    print(f'Количество строк: {len(f_text)}')
    count_words = 0
    for el in f_text:
        words = el.split(' ')
        count_words = count_words + len(words)
    print(f'Количество слов: {count_words}')

# 3 задание

def add_workers():
    with open('workers.txt', 'a', encoding='utf-8') as f:
        while True:
            name = input('Input name: ')
            if name == "":
                break
            salary = input('Input salary: ')
            print(f'{name}:{salary}',file=f)

add_workers()

with open('workers.txt', 'r', encoding='utf-8') as f:
    workers = f.readlines()
    low_sal_workers = []
    salary = []
    for worker in workers:
        worker = worker.split(':')
        worker[1] = int(worker[1])
        salary.append(worker[1])
        if worker[1] < 20000:
            low_sal_workers.append(worker[0])
    print(low_sal_workers)
    print(sum(salary)/len(salary))

# 4 Задание
my_dict = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
numbers_en = []
numbers_ru = []

with open('4_task_en.txt', 'r', encoding='utf-8') as f:
    numbers_en = f.readlines()
    print(numbers_en)

for number in numbers_en:
    number = list(number.split(' - '))
    number[0] = my_dict[number[0]]
    numbers_ru.append(number)

with open('4_task_ru.txt', 'w', encoding='utf-8') as f:
    for number in numbers_ru:
        f.writelines(f'{number[0]} - {number[1]}')

# 5 задание

with open('5_task_ru.txt', 'w', encoding='utf-8') as f:
    my_numbers = input('Input numbers. Split space: ')
    f.writelines(my_numbers)

with open('5_task_ru.txt', 'r') as f:
    number_5 = f.read().split(' ')
    number_list = []
    for num in number_5:
        num = int(num)
        number_list.append(num)
    print(f'Сумма чисел равно: {sum(number_list)}')

# 6 задание

with open('lessons.txt', 'r', encoding='utf-8') as f:
    #print(f.readlines())
    data = f.readlines()
    lab = {}
    pr = {}
    lect = {}
    for el in data:
        subject = el.split(' ')
        subject[0] = subject[0][0:len(subject[0])-1] # Подскажите пожалуйста более простой способ удалить элемент из строки
        lect[subject[0]] = subject[1]
        pr[subject[0]] = subject[2]
        lab[subject[0]] = subject[3]
    print(f'Лекции: {lect}')
    print(f'Практические занятия: {pr}')
    print(f'Лабораторные: {lab}')

# 7 задание
firm_data = []

with open('firm_data.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    counter = 0
    #print(data)
    for el in data:
        el_data = el.split(' ')
        #print(el_data)
        firm_name = el_data[0]
        firm_form = el_data[1]
        firm_income = int(el_data[2])
        firm_costs = int(el_data[3])
        firm_margin = firm_income - firm_costs
        firm_dict = {'Firm_name' : firm_name,
        'Firm_form' : firm_form,
        'Firm_income' : firm_income,
        'Firm_costs' : firm_costs,
        'Firm_margin' : firm_margin}
        firm_data.append(firm_dict)
#print(firm_data)

margin_list = []
for el in firm_data:
    if el['Firm_margin'] > 0:
        margin_list.append(el['Firm_margin'])
print(f'Average margin: {sum(margin_list)/len(margin_list)}')

json_firm_data = json.dumps(firm_data)
print(json_firm_data)
print(type(json_firm_data))
