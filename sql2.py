import MySQLdb

DB_HOST = 'DESKTOP-AOLV73S' 
DB_USER = 'jordan' 
DB_PASS = 'madworld2727' 
DB_NAME = 'db_python' 

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor() # Crear un cursor 
    cursor.execute(query) # Ejecutar una consulta 
    
    #if query.upper().startswith('SELECT'): 
    data = cursor.fetchall() # Traer los resultados de un select 
    """ else: 
        conn.commit() # Hacer efectiva la escritura de datos
        data = None """

    cursor.close() # Cerrar el cursor 
    conn.close() # Cerrar la conexión 

    return data

imp=run_query('select * from una_tabla')
print(imp)