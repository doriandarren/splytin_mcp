import pymysql

def get_connection(host, user, password, database, port=3306):
    """
    Establishes and returns a connection to the MySQL database with given credentials.
    """
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",
        )
        return connection
    except pymysql.MySQLError as err:
        print(f"Connection error: {err}")
        return None