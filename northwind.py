# import sqlite library
import sqlite3

# open a connection for northwind_small.sqlite3
# make a cursor
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

# test the connection
# get all the names for all tables
query1 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"

# the ten most expensive items per unit price
query2 = """SELECT ProductName, UnitPrice FROM Product
        ORDER BY UnitPrice DESC LIMIT 10"""

# average age of an employee at the time of their hiring
query3 = """SELECT AVG(substr(HireDate, 1, 4) - substr(BirthDate, 1, 4))
        FROM Employee"""

# Stretch 
# how does the average age of an employee at hire vary by city?
query4 = """SELECT City, AVG(substr(HireDate, 1, 4) - substr(BirthDate, 1, 4))
        FROM Employee GROUP BY City"""

# What are the ten most expensive items in the db and their suppliers
query5 = """SELECT ProductName, UnitPrice, CompanyName FROM Product
        JOIN supplier
        ON Product.supplierId = Supplier.id
        ORDER BY UnitPrice DESC LIMIT 10;"""

# What is the largest category by number of unique products?
query6 = """SELECT CategoryName, COUNT(*)
        FROM Product JOIN Category
        ON Product.CategoryId = Category.Id
        GROUP BY CategoryName
        ORDER BY COUNT(*) DESC LIMIT 1"""

# Stretch 
# What is the name of the employee with the most territories?
# Use `TerritoryId`(not name, region, or other fields) as the unique identifier
# for territories.
query7 = """SELECT FirstName, LastName, COUNT(*)
        FROM Employee JOIN EmployeeTerritory
        ON Employee.Id = EmployeeTerritory.EmployeeId
        GROUP BY FirstName, LastName
        ORDER BY COUNT(*) DESC LIMIT 1"""

queries = [query1, query2, query3, query4, query5, query6, query7]

# define a function for queries
def execute_sql(queries, db_name):
    """Instantiate connection and cursor
       execute the SQL queries 
       from queries list"""
    # open a connection
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    for query in queries:
        print('execute: \n', cur.execute(query).fetchall())

#execute all queries
execute_sql(queries, 'northwind_small.sqlite3')

# commit all changes and save them
cur.close()
conn.commit()
conn.close()
