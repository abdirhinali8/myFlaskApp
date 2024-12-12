import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="myflaskapp")
    print(db)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print("Database version: ", version)
    cursor.close()
    db.close()
except MySQLdb.OperationalError as e:
    print(f"Connection error: {e}")