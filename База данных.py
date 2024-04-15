import sqlite3 as sql

print("1 - добавление\n2 - получение")
choice = int(input("> "))
con = sql.connect('tes.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `tes` (`name` STRING, `surname` STRING,`dopinfa` STRING)")

    if choice == 1:
        name = input("Имя\n> ")
        surname = input("Фамилия\n> ")
        dopinfa = input("Допольнительная информация\n> ")
        cur.execute(f"INSERT INTO `tes` VALUES ('{name}', '{surname}', '{dopinfa}')")
    elif choice == 2:
        cur.execute("SELECT * FROM `tes`")
        rows = cur.fetchall()
        a = 0
        for row in rows:
            a += 1
            print(a,row[0], row[1])
        s = int(input("Введите номер человека, информацию о котором вы хотите уточнить\n> "))
        a = 0
        for row in rows:
            a += 1
            print(row[0], row[1], str(":"),row[3])
    else:
        print("Вы ошиблись")

    con.commit()
    cur.close()