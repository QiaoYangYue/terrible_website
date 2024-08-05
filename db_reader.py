#database reader
import sqlite3

table_name = "ping_results" #['ping_results', 'sqlite_sequence']
db_file = 'ping_data.db'


def read_db(db_file, table_name):
  
  """
  Reads data from an SQLite database.
  Args:
    db_file: The path to the database file.
  Returns:
    A list of tuples containing the data from the database.
  """
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  # Replace with your desired query
  try:
    cursor.execute("SELECT * FROM ping_results")
    data = cursor.fetchall()
  except sqlite3.OperationalError as e:
    print(f"Error querying table: {e}")
    results = None
    return "nothing"

  cursor.close()
  conn.close()
  return data

def get_table_names(db_file):
  """
  Gets a list of table names from an SQLite database.
  Args:
    db_file: The path to the database file.
  Returns:
    A list of table names.
  """
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()

  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  table_names = [table[0] for table in cursor.fetchall()]

  cursor.close()
  conn.close()
  return table_names

if __name__ == "__main__":
  data = read_db(db_file,table_name)
  print(data)
  #tables = get_table_names(db_file)
  #print(tables)
