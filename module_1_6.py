my_dict = {'Алексей':1986, 'Елена': 1988, 'Юлия': 2008, 'Марина': 2014, 'Яна':1989}
print(my_dict)
print(my_dict['Алексей'])
my_dict.update({'Василий Александрович': 1961, 'Елена Николаевна':1966})
Sister = my_dict.pop('Яна')
print(Sister)
print(my_dict)

my_set = {'Алексей', 'Елена', 'Юлия', 'Марина', 'Елена', 'Василий', 'Яна'}
print(my_set)
my_set.update({'Бакс','Сникерс'})
my_set.discard('Яна')
print(my_set)
print('пробую изменить')
