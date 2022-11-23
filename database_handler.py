from sqlite3 import connect, Error
from loguru import logger

def create_database(table_name: str):
    connection = connect('spendings_database.db')
    cursor = connection.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ([call_id] INTEGER PRIMARY KEY, [user_id] INTEGER, [category] TEXT, [amount] INTEGER)')
    connection.commit()
    connection.close()
    
def insert_into_table(table_name: str, values: list):
    try:
        connection = connect('spendings_database.db')
        cursor = connection.cursor()
        query = f'INSERT INTO {table_name} (call_id, user_id, category, amount) VALUES (?,?,?,?)'
        cursor.execute(query, values)
        connection.commit()
    except Error:
        logger.exception('Failed to connect to database table!')
    finally:
        if connection:
            connection.close()       
    
if __name__ == '__main__':
    logger.add('logfile.log', format = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}', colorize = True, backtrace = True, diagnose = True, retention = '1 month')
    create_database('spendings')