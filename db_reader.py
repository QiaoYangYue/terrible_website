#database reader
import sqlite3

table_name = "ping_results" #['ping_results', 'sqlite_sequence']
db_file = 'ping_data.db'
data_rearranged = {}
connection_count = {}
unique_ips = set()
data = {}

def read_db(db_file, table_name):
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()
  for ip in db_file:
    cursor.execute("SELECT timestamp, delay FROM ping_results WHERE ip = ? ORDER BY timestamp DESC", (ip,))
    data[ip] = cursor.fetchall()
  cursor.close()
  conn.close()
  return data

def get_ips():
   ip_addresses = []
   file_name = 'ips.txt'
   file = open(file_name, "r")
   ips_list = file.readlines()
   file.close()
   for ip in ips_list:
      ip_list = ip.strip("\n").strip(" ")
      if ip_list:
        ip_addresses.append(ip0)
        return ip_addresses


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

def data_arranger(data):
  '''
  Gets the data and arranges it by end point
  '''
  data_rearranged = {}
  connection_count = {}
  ips = {}
  ip_id = 1
  counter = 0

  for id, url, signal_strength, timestamp in data:
    if url not in data_rearranged:
        ips[ip_id] = (url,ip_id)
        data_rearranged[counter] = []
        ip_id += 1 
        counter += 1       
    else:
        data_rearranged[counter].append((signal_strength, timestamp))
        counter += 1       


  return data_rearranged, connection_count, unique_ips




if __name__ == "__main__":
  data = read_db(db_file,table_name)
  #data_arranger(data)
  print(data_rearranged)
  print(data)
  #tables = get_table_names(db_file)
  #print(tables)


'''
Ok so we have, a bunch of endpoint? times they where accessed, and their signal strengths at each time?
What we want to do, is to create a dictionary, and then from the db, add unique endpoints into an entry? 
From there we will have a bunch of signal strengths and times accessed
then we can use mpl to like, make a scatter plot of each one, with the times as the x and the signal strength as the y
then we want to have that as an element on a website
simple as
'''
