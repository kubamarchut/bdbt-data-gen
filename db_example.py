import getpass
import oracledb

from languages import langs

pw = getpass.getpass("Enter password: ")
print(pw)

connection = oracledb.connect(
    user="BDBTGRC06",
    password=pw,
    dsn="194.29.170.4:1521/xe")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

cursor.executemany("insert into JEZYKI (KOD_JEZYKA, NAZWA_JEZYKA) values(:1, :2)", langs)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# Now query the rows back
for row in cursor.execute('select * from JEZYKI'):
    print(row)
