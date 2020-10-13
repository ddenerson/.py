import sqlite3

connection = sqlite3.connect("data.db")


# function of data base creation
def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, publication_date TEXT)")


# data entry connection
def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES(? , ?);", (entry_content, entry_date))

# showing database data 
def get_entries():
    cursor = connection.execute("SELECT * FROM entries")
    return cursor
