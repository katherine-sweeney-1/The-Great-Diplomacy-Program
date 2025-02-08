import mysql.connector

def create_sql_db(username):
    sql_db = mysql.connector.connect(
    user = username,
    #password = password,
    database = "tgdp_testintg"
    )
    return sql_db