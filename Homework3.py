# 1 задание

#dividend, divider

def divide ():
    try:
        dividend = int(input('Введите Делимое: '))
        divider = int(input('Введите Делитель: '))
    except ValueError:
        print('Введены не корректные значения')
    else:
        try:
            result = dividend / divider
        except ZeroDivisionError:
            print('Деление на ноль')
        else:
            print(result)
            return result

#divide()

# 2 задание

def user_data(**kwargs):
    return kwargs
print(user_data(age = 1, name = 'mike', sername = 'Ivanov', place_of_burth = 'Moscow', email = '123@mail.ru', phone = '+79055676578'))

# 3 задание

def my_func(arg1, arg2, arg3):
    data = [arg1, arg2, arg3]
    data.remove(min(data))
    sum_args = sum(data)
    return sum_args

print(my_func(1,2,3))

# 4 задание

def my_func2(x, y):
    x = abs(float(x))
    y = -1 * abs(int(y))
    #result_1 = x ** y
    #return result_1
    result = 1
    for i in range(abs(y)):
        result = result / x
    return result

print(my_func2(9,-2))

# 5 задание

# total_sum_list = []
# while True:
#     data = input('Введите числа через пробел: ')
#     data_list = data.split(' ')
#     count = 0
#     for i in range(len(data_list)):
#         try:
#             data_list[i] = int(data_list[i])
#             count +=1
#         except:
#             current_sum = sum(data_list[:count])
#             total_sum_list.append(current_sum)
#             print(f'Итоговая сумма: {sum(total_sum_list)} Вы вышли из программы')
#             break # в данном случае break рушит цикл For, но цикл While продолжает работать, из за этого вылезает ошибка при выходе, не понял как исправить
#     current_sum = sum(data_list)
#     #print(f'current list {data_list}')
#     #print(f'Текущая сумма {current_sum}')
#     total_sum_list.append(current_sum)
#     print(f'Итоговая сумма: {sum(total_sum_list)} для выхода введите любую букву')

# 6 и 7 задание
def int_func(text):
    txt = text.capitalize()
    return txt
print(int_func('some text'))

text = input('Введите слова: ')
text_list = text.split(' ')
text_capital_list = []
for word in text_list:
    word_cap = int_func(word)
    text_capital_list.append(word_cap)
print(" ".join(text_capital_list))







