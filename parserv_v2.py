# -*- coding: utf-8 -*-
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
        with open("output.txt", "w", encoding='utf-8') as output:
            output.writelines("\n".join(str(line) for line in lines))
        print("Результат збережен в файл: output.txt")


while True:
    print("[1] - Парсити сайт")
    print("[2] - Вивести дані з бази в текстовий файл")
    print("[3] - Видалити дані з БД")
    print("[4] - Вихід з программи")

    choice = input("Оберіть функцію: ")

    choice = choice.strip()

    if (choice == "1"):
        parse()
    elif (choice == "2"):
        intofile()
    elif (choice == "3"):
        db_clear()
    elif (choice == "4"):
        break
    else:
        print("Невірна функція.")

