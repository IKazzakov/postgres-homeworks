"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os


def write_data_to_table(file_name, table_name):
    """
    Записывает данные из CSV-файла в таблицу.
    """
    path_to_data = os.path.join('north_data', file_name)
    with psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password=os.getenv('DB_HW_PSSWRD')
    ) as conn:
        with conn.cursor() as cur:
            with open(path_to_data, encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                # Удаляет заголовок
                title = next(file_reader)
                for row in file_reader:
                    cur.execute(
                        f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})",
                        row
                    )
                    conn.commit()


if __name__ == '__main__':
    write_data_to_table('customers_data.csv', 'customers')
    write_data_to_table('employees_data.csv', 'employees')
    write_data_to_table('orders_data.csv', 'orders')
