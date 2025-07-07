home_list =['milk', 'bread', 'tomatos', 'apple', 'icecream']
print(home_list)
home_list.append('cheese')
print(home_list)

marks=[10, 11, 12, 8, 7, 10, 9]
print('average_marks=', sum(marks)/len(marks))

names=['Petro', 'Ivan', 'Oleh', 'Roman', 'Dmytro']
names.sort()
print(names)

cities=['Lviv', 'Dnipro', 'Kyiv', 'Odesa', 'Kharkiv']
cities[1]='Rivne'
print(cities[0], cities[len(cities)-1])


subjects_nmt=['ukrainian language', 'mathematics', 'history', 'foreign language', 'biology', 'geography', 'chemistry', 'physics']
print(len(subjects_nmt))
del(subjects_nmt[4])
subjects_nmt.sort()
print(subjects_nmt)