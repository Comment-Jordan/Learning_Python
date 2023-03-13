import pyodbc

conn= pyodbc.connect('Driver={ODBC driver 17 for SQL Server};' 
'Server=DESKTOP-AOLV73S;'
'Database=db_python;'
'UID=jordan;'
'PWD=madworld2727;')

cursor=conn.cursor();
cursor.execute('select * from una_tabla')
for fila in cursor:
    print(fila)
