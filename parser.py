#-*- coding: utf-8 -*-
import sqlite3, requests, bs4


with sqlite3.connect("base.db") as conn:
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS numbers(number TEXT, name TEXT, last_name TEXT);")


def parse():
    r = requests.get("https://8be8-45-89-89-202.eu.ngrok.io/")
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    strings = soup.find_all("p")
    for string in strings:
        all = string.text.split(",")
        number = all[0]
        name = all[1]
        last_name = all[2]
        with sqlite3.connect("base.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO `numbers` VALUES (?,?,?)", (number, name, last_name,))
        print(f"Додано в бд:\nНомер: {number}\nІм'я: {name}\nПрізвище: {last_name}\n______________________")


def db_clear():
    with sqlite3.connect("base.db") as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM `numbers`")
    print("База даних повністю очищена")

def intofile():
    with sqlite3.connect("base.db") as conn:
        lines = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM numbers")
        rows = cur.fetchall()
        for row in rows:
            number = row[0]
            name = row[1]
            last_name = row[2]
            lines.append(f"Номер: {number}\nІм'я: {name}\nПрізвище: {last_name}\n______________________\n")
        with open("output.txt", "w",encoding='utf-8') as output:
            output.writelines("\n".join(str(line) for line in lines))
        print("Результат збережен в файл: output.txt")

option = input("Виберіть функцію програми: 1 - Парсинг з сайту, 2 - Зберегти усю базу в текстовий файл, 3 - Видалити усе з бд\n")
if int(option) == 1:
    parse()
elif int(option) == 2:
    intofile()
elif int(option) == 3:
    db_clear()
