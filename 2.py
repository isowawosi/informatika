# TODO Напишите функцию find_common_participants
def find_common_participants(n,m,j =','):
   k = n.split(j) #убираем разделители и оставляем просто список участников
   l = m.split(j)
   z = list(set(k).intersection(l)) #ищем соотвествия
   return sorted(z) #выводим отсортированный список
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, ",")
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
result2 = find_common_participants(participants_first_group, participants_second_group, "!")
print(result2)