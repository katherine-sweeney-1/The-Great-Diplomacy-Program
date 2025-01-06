import mysql.connector

def create_sql_db(username, password):
    sql_db = mysql.connector.connect(
    user = username,
    password = password,
    database = "diplomacy_map_data"
    )
    return sql_db

#Convert Image Data to binary
def convert_to_binary(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data

# add_blob(id, name, picture, )