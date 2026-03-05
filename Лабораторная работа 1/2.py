list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
s = len(list_players) #нашли длины списка
rav = s//2 #поделили поровну
com1 = list_players[:rav] #выбрали первую пололвину
com2 = list_players[rav:] #выбрали втору. полвину
print(com1)
print(com2)
