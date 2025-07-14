print("Завдання 1")
contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}
contacts["Taras"]= "063-000-11-22"# Додавання елемента до словника contacts
contacts.pop("Ivan") #Видаллення елемента словник
print(contacts.keys()) #вивести ключі елементів словника
print(contacts.values())#вивести значення елементів словника
if "Katya" in contacts: #перевірка чи значення "Katay" ' ключем словника
  print("Так, 'Katya' є один з ключів словника")
else:
  print("Ні, 'Katya' не є одним з ключів словника")
  
print("Завдання 2")
grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}
print('Максимальна оцінка =', max(grades.values()))#знаходження максимального елемента
print('список предметів, де оцінка >80:') #виведення списку предметів, де оцінка >80
spisok=[]
for i in grades.keys():
    if grades.get(i)>80:
      spisok.append(i)
print(spisok)
print("Завдання 3")
transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
print("Словник клієнтів:")
balances={}
for name, suma in transactions:
    if name in balances:
        balances[name] += suma
    else:
        balances[name] = suma

print(balances)

max_balances=max(balances.values())
for x, y in balances.items():
    if y==max_balances:
       print('Клієнт з найбільшим балансом ', x)
    if y<0:
       print('Клієнт з від\'ємним балансом ', x)

print("Завдання 4")
text = "hello world hello again hello world test world"
text_list=list(text.split())#перетворення тексту в список
text_set=set(text_list)#перетворення списку в множину
#створення словника
dict_count={}
for world in text_set:
   dict_count[world]=text_list.count(world)
print(dict_count)

print("Завдання 5")
student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}
import json
student_str=json.dumps(student)#перетворення словника в рядок
print('Рядок студент')
print(student_str)
print('Словник студент')
student_1=json.loads(student_str)#претворення рядка в словник
print(student_1)
student_1["courses"].append("history")# додавання курсу history до списку курсів
print(student_1)