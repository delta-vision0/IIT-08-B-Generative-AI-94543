import mysql.connector
import streamlit as st
import Call_groq as cg

host = "localhost"     # or your MySQL server IP
user = "root"          # your MySQL username
password = "manager" # your MySQL password
database = "sunbeam"   # database to connect to


def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        autocommit=True
    )

st.title("MySQL UI")
try:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    st.sidebar.title("MySQL DataBase")
    st.sidebar.success("Connected !")

    cursor.execute("Select * from employees")
    tables = cursor.fetchall()
    table_names = [list(t.values())[0] for t in tables]
    st.table(tables)
    user_input = st.chat_input("Enter Query : ")
    query = cg.generate_mysql_query(tables,user_input)
    # Example: Fetch some data
    if query:
        st.info(f"Executing : {query}")
        cursor.execute(query)
        if cursor.with_rows:
            rows = cursor.fetchall()
            if rows:
                st.dataframe(rows)
            else:
                st.warning("No Results Found.")
            st.success(f"Query OK, {cursor.rowcount} row(s) affected.")
            st.header("Explaination")
            explain = cg.explain_query_result(user_input,query,rows,cursor.rowcount)
            st.write(explain)
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print("Error:", err)