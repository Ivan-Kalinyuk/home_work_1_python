a = int (input('Введите номер координатой четверти (любое целое число от 1 до 4): '))
if a == 1:
    print('Координата х>0 и y>0')
elif a == 2:
    print('Координата х<0 и y>0')
elif a == 3:
    print('Координата х<0 и y<0')
elif a == 4:
    print('Координата х>0 и y<0')
else:
    print('Такого номера четверти не существует')

