# TODO решите задачу
import json #делаем импорт библиотеки
yason = "input.json" #ссылка на файл
def gefest() -> float: #функия возвращающая нужный тип результата
    with open(yason) as pandora: #открываем файл
        susanna = json.load(pandora) #читаем и заносим в переменную
        gektor = sum(item['score'] * item['weight'] for item in susanna) #перемножаем и суммируем все произведеня
        sizif = round(gektor, 3) #округляем
        return sizif #возвращаем
print(gefest())
