# encoding: utf-8
'''
@author: binky
@file: datatools.py
@time: 2023/8/30 23:09
@desc:
'''

import sqlite3
import os


# 连接到 SQLite 数据库
# 数据库文件是 test.db，如果文件不存在，会自动在当前目录创建


def create_database(db_name):
	if not os.path.exists(db_name):
		conn = sqlite3.connect(db_name)
		print(f"Database {db_name} created successfully")
		conn.close()
	else:
		print(f"Database {db_name} already exists")


def create_table(db_name, table_name):
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name}
           (KEY TEXT PRIMARY KEY NOT NULL,
           VALUE           TEXT NOT NULL);
    ''')
	print(f"Table {table_name} created successfully in database {db_name}")
	conn.close()


def insert_data(db_name, table_name, key, value):
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	cursor.execute(f"INSERT INTO {table_name} (KEY, VALUE) VALUES (?, ?)", (key, value))
	conn.commit()
	print(f"Data inserted successfully into table {table_name} in database {db_name}")
	conn.close()


def update_data(db_name, table_name, key, value):
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	cursor.execute(f'''
    INSERT INTO {table_name} (KEY, VALUE)
    VALUES (?, ?)
    ON CONFLICT(KEY) DO UPDATE SET VALUE = ?;
    ''', (key, value, value))
	conn.commit()
	print(f"Data updated successfully in table {table_name} in database {db_name}")
	conn.close()


def delete_data(db_name, table_name, key):
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	cursor.execute(f"DELETE FROM {table_name} WHERE KEY = ?", (key,))
	conn.commit()
	print(f"Data deleted successfully from table {table_name} in database {db_name}")
	conn.close()


def find_data(db_name, table_name, key):
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM {table_name} WHERE KEY = ?", (key,))
	data = cursor.fetchone()
	print(f"Data fetched successfully from table {table_name} in database {db_name}")
	conn.close()
	return data

# create_database("test.db")
# create_table('test.db', 'KeyValueTable')
# insert_data('test.db', 'KeyValueTable', 'myKey', 'myValue')
# update_data('test.db', 'KeyValueTable', 'myKey', 'myValue2')
# delete_data('test.db', 'KeyValueTable', 'myKey')
# data = find_data('test.db', 'KeyValueTable', 'myKey')
# print(data)
