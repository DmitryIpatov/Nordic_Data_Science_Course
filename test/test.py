# print ('hello')
# test comment

# n = 1_000
# print (n)
# print(int(5/3))
#
# print(round((5/3),1))


# print (round(5.8)) #6

# help(round(1.1))

# def f(x):
#     x = x*2
#     return x
#
# print(f(3))



# s = input('enter name: ')
# print('hello,', s, '!')

# s = 'Я люблю писать программы'
# print('J'+s[4:])

# s = 'test'
# print(s=='test')
# print('e' in s)
#
#
# def some_func():
#     """Не делаем ничего
#     """
#     pass
#
# help(some_func())

# body mass index
weight = (input('enter weight: '))
if len(weight)>0:
    weight = float(weight)
else:
    print('weight required')


height = input('enter height in cm: ')
if len(height)>0:
    height=float(height)/100
else:
    print('height required')

def calc_bmi(weight, height):
    bmi = weight/(height)**2
    return bmi

def bmi_info(bmi_index):
    descr = ''
    if bmi_index>40:
        cat = 'сильное ожирение'
        risk = 'серьезный'
    elif 30 < bmi_index < 39.9:
        cat = 'ожирение'
        risk = 'высокий'
    elif 25 < bmi_index < 29.9:
        cat = 'избыточный вес'
        risk = 'умеренный'
    elif 18.5 < bmi_index < 24.9:
        cat = 'норма'
        risk = 'низкий'
    elif bmi_index < 18.5:
        cat = 'недостаточный'
        risk = 'умеренный'
    descr = 'весовая категория: '+cat, 'риск: '+risk
    return descr

x = calc_bmi(weight=weight, height=height)
y = bmi_info(x)


print('BMI=' , round(x,2), y)