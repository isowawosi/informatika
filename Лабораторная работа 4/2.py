# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as m: #открываем cvn с указанием кодировки,прочитываем
        k = csv.DictReader(m) # первая строка как заголовки
        d = list(k) # переделываем в список словариков

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as h: #открываем json
        json.dump(d, h, indent=4, ensure_ascii=False) #записывваем словари в json отсттуп 4
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
