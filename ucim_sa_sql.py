import random
import sqlite3
import sys

# Vygenerujem 100 nahodnych cislich
cisla = [random.randint(0, 100) for a in range(100)]
#print(cisla)

# Vytvorim databazu/tabulku

with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS numbers")
    c.execute("CREATE TABLE numbers (zaznam INT)")

    for i in range(100):
        c.execute("INSERT INTO numbers (zaznam) VALUES (?)", (cisla[i],))

sql = {'avg': "SELECT avg(zaznam) FROM numbers",
        'max': "SELECT max(zaznam) FROM numbers",
        'min': "SELECT min(zaznam) FROM numbers",
        'sum':"SELECT sum(zaznam) FROM numbers"}

print('Table created.')

while True:

    resp = input('Select "avg", "min", "max", "sum" or "q" >>> ')
    if resp.lower() == 'q':
        break

    if resp.lower() == 'avg':
        c = connection.cursor()
        result = c.execute(sql['avg'])
        print(result.fetchone()[0])

    if resp.lower() == 'min':
        c = connection.cursor()
        result = c.execute(sql['min'])
        print(result.fetchone()[0])

    if resp.lower() == 'max':
        c = connection.cursor()
        result = c.execute(sql['max'])
        print(result.fetchone()[0])

    if resp.lower() == 'sum':
        c = connection.cursor()
        result = c.execute(sql['sum'])
        print(result.fetchone()[0])
