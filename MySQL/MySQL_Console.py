import mysql.connector

host = "localhost"     # or your MySQL server IP
user = "root"          # your MySQL username
password = "manager" # your MySQL password
database = "sunbeam"   # database to connect to


try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        autocommit=True
    )

    print("Connected to MySQL database!")

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Example: Fetch tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Tables in database:", tables)
    while True:
        query = input("Enter Query : ")
        if query == "exit":
            break
        # Example: Fetch some data
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print(f"Query OK, {cursor.rowcount} row(s) affected.")
    cursor.close()
    conn.close()
    print("Connection closed.")

except mysql.connector.Error as err:
    print("Error:", err)