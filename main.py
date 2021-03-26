# import sqlite3
#
#
# def create_table():
#     # Create connection to database
#     conn = sqlite3.connect("lite.db")
#
#     # Place a cursor in the database so you can interact with it
#     cur = conn.cursor()
#
#     # Using the cursor create a table. item, quantity and price are the names of the columns in the table
#     # TEXT, INTEGER and REAL define the kind of data that must be entered into the columns
#     conn.execute("CREATE TABLE  IF NOT EXISTS cow(item TEXT, quantity INTEGER, price REAL)")
#
#     # Commit the changes
#     conn.commit()
#
#     # close the connection
#     conn.close()
#
#
# def insert(item, quantity, price):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     # Insert into the DB
#     cur.execute("INSERT INTO cow VALUES(?,?,?)", (item, quantity, price))
#     conn.commit()
#     conn.close()
#
# #
# def view():
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM cow")
#     rows = cur.fetchall()
#     conn.close()
#     return rows
# #
# #
# def delete(stuff):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM cow WHERE  item=?", (stuff,))
#     conn.commit()
#     conn.close()
# #
# #
# def update(quantity, price, item):
#     conn = sqlite3.connect("lite.db")
#     cur = conn.cursor()
#     cur.execute("UPDATE cow SET quantity=?, price=? WHERE item=?",(quantity, price, item))
#     conn.commit()
#     conn.close()
#
# # create_table()
# # delete("beans")
# update(15,2,"rice")
# # insert("beans", 2, 5 )
# print(view())
