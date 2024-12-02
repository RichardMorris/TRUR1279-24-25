
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        database = "test"
    ) as connection:
        print(connection)

        select_user_query = "SELECT * FROM highscores LIMIT 5"
        with connection.cursor() as cursor:
            cursor.execute(select_user_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

except Error as e:
    print(e)

