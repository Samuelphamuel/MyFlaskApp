import pymysql.cursors

# Function to connect to the MySQL database and return data
def execute_sql_query(sql_query):
    # Connect to your database
    connection = pymysql.connect(
        host = 'localhost', # your host name
        user = 'root', # your username
        password = 'p@ssw0rd', # your MySQL password
        database = 'storedata', # your database name
        cursorclass = pymysql.cursors.DictCursor
    )

    # Return all rows from executed query and execute queries by using cursor object
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            return result

    # Close cursor and connection
    finally:
            connection.close()