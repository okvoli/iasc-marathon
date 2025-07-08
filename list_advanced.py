students=['Anna', 'Ivan', 'Olha', 'Taras', 'Katya']
grades=[95, 62, 47, 88, 53]
Max=grades[0]
index_Max=0
for i in range(1, 5):
    if grades[i]>Max:
        Max=grades[i]
        index_Max=i
print('Студент з максимальною кількістю балів: ', students[index_Max])

Count=0
for i in range(5):
    if grades[i]>60:
        print('Студент має > 60 балів' , students[i])
    if grades[i]<60:
        Count+=1
print('Кількість студентів, які отримали <60 балів ', Count)

logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
set_logs=set(logs)
list_logs=list(set_logs)
Counts=[]
for element in list_logs:
    p=logs.count(element)
    Counts.append(p)
for i in range(len(list_logs)):
    print(list_logs[i], Counts[i])
    if "error"==list_logs[i]:
        q=Counts[i]
vidsotok=q/len(logs)*100
print('Відсоток error ', f"{vidsotok:.2f}", '%')

expenses = [ ["Понеділок", 120], ["Вівторок", 80], ["Середа", 150], ["Четвер", 0], ["П’ятниця", 250], ["Субота", 300], ["Неділя", 200]]
Sum=0
for i in range(7):
    Sum+=expenses[i][1]
print("Сума витрат за тиждень ", Sum)
print('Список деів, коли витрати були більші за 100')
for i in range(7):
    if expenses[i][1]>100:
        print(expenses[i][0])