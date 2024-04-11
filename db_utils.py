import pymysql.cursors

# Function to connect to the MySQL database and return data
def execute_sql_query(sql_query):
    # Connect to your database
    connection = pymysql.connect(
        host = 'localhost', # your host name
        user = 'root', # your username
        password = 'pa$$w0rd', # your MySQL password
        database = 'storedata', # your database name
        cursorclass = pymysql.cursors.DictCursor
    )

    # Return all rows from executed query and execute queries by using cursor object
    try:
        with connection.cursor() as cursor:

            cursor.execute(sql_query)
            result = cursor.fetchall()
            connection.commit()
            return result

    except pymysql.Error as error:
        print(f"Error while connecting to MySQL: {error}")
        return None

    # Close cursor and connection
    finally:
            connection.close()

# Example SQL query
query = "SELECT * FROM sales WHERE id = 5;" # Modify this SQL query to print result to terminal
result = execute_sql_query(query)
print(result)

