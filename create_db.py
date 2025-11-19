import sqlite3

connection = sqlite3.connect('dbteste.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS appointments (appointment_id int PRIMARY KEY,\
name text, description text)"

create_appointment = "INSERT INTO appointments VALUES (1, 'Primeiro', 'Descrição do primeiro agendamento')"

cursor.execute(create_table)
cursor.execute(create_appointment)

connection.commit()
connection.close()
