x = float (input('Введите координату точки по оси Х(не используйте ноль, иначе точка будет лежать на оси и не будет принадлежать какой-либо четверти):'))
y = float (input('Введите координату точки по оси Y(не используйте ноль, иначе точка будет лежать на оси и не будет принадлежать какой-либо четверти):'))
if x==0 or y==0:
    print ('Вы ввели нулевое значение!')
elif x>0 and y>0:
    print ('Ваша точка находится в 1-й координатой четверти')
elif x<0 and y<0:
    print ('Ваша точка находится в 3-й координатой четверти')
elif x<0 and y>0:
    print ('Ваша точка находится в 2-й координатой четверти')
else:
    print ('Ваша точка находится в 4-й координатой четверти')