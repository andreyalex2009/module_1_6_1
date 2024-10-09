my_dict = {'Andrey' : 1977, 'Evgeniy' : 1982, 'Anton' : 1985, 'Denis' : 1980 }
print(my_dict)
print(my_dict['Andrey'])
my_dict['Grigoriy'] = 2000
print(my_dict)
my_dict.update({'Galya' : 2001, 'Macha' : 2003})
print(my_dict)
b = my_dict.pop('Evgeniy')
print(b)
print(my_dict)
my_set = {1, 2, 3, 1, 2, 'Andrey', 'Anton', (1, 2, 4,), True, 'Anton'}
print(my_set)
my_set.update([6, 20])
print(my_set)
my_set.discard(2)
print(my_set)