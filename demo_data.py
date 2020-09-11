# import sqlite library
import sqlite3

# open a connection for demo_data.sqlite3
# make a cursor
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

#Define a function to create a table
#BY passing a parametter which is called a conn
def create_table(conn):
  cur = conn.cursor()
  create_statement = '''
    CREATE TABLE IF NOT EXISTS demo_data
    (s, x, y);
  '''
  cur.execute(create_statement)
  cur.close()
  conn.commit()
# Create a function to insert data from that table
def insert_data(conn):
  insert_statement = '''
  INSERT INTO demo_data
  VALUES ("g", 3, 9), ("v", 5, 7), ("f", 8, 7);
  '''

  cur.execute(insert_statement)
  cur.close()
  conn.commit()


cur.execute('SELECT * FROM demo_data').rowcount

query_row1 = len(cur.execute('SELECT * FROM demo_data').fetchall())

# How many rows are there where both x and y are at least 5?
query2 = '''
SELECT *
FROM demo_data
WHERE x >= 5 AND y >= 5;'''
query_row2 = len(cur.execute(query2).fetchall())

# How many unique values of y are there?
query3 = '''
SELECT COUNT(DISTINCT y)
FROM demo_data
'''
query_row3 = cur.execute(query3).fetchall()[0][0]

# Lets execute the above functions 
if __name__ == "__main__":
  conn = sqlite3.connect('demo_data.sqlite3')
  create_table(conn)
  insert_data(conn)

#print and answer all those questions regarding the business
print(f'There are {query_row1} rows in demo_data\n')
print(f'{query_row2} rows have both x and y greater or equal to 5\n')
print(f'There are {query_row3} unique values for y\n')