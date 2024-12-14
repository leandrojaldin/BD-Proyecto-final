from connections import *
import query

# Conexión a SQL Server
sqlserver = connect_sqlserver()
old_c = sqlserver.cursor()

# Conexión a MySQL
try:
    mysqll = connect_mysqll()
    new_c = mysqll.cursor()

    # Verificar si la base de datos ya existe para no volver a hacer la migracion
    db_name = "Gym_migrado" 
    new_c.execute(f"SHOW DATABASES LIKE '{db_name}';")
    if new_c.fetchone():  
        print(f"La base de datos '{db_name}' ya existe. La migración ya fue realizada.")
        exit()  # Salir del programa si la base de datos ya existe

    # Crear base de datos si no existe
    db_name = "Gym_migrado"
    new_c.execute(f"CREATE DATABASE {db_name};")
    new_c.execute(f"USE {db_name};") 

    # Tablas a migrar
    tables = ["CLIENTE", "SERVICIO", "INSCRIPCION", "PAGOS", "ASISTENCIA", "ENTRENADORES"]

    for table_name in tables:
        print(f"Migrando tabla: {table_name}")

        # Obtener esquema de la tabla
        old_c.execute(f"""
            SELECT COLUMN_NAME, DATA_TYPE 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = '{table_name}';
        """)
        columns = old_c.fetchall()

        # Crear tabla en MySQL
        create_table_query = f"CREATE TABLE {table_name} ("
        column_properties = []
        for column in columns:
            column_name, data_type = column

            # Mapear los tipos de datos de SQL Server a MySQL
            if data_type in ["nvarchar", "varchar"]:
                data_type = "VARCHAR(50)"
            else: data_type = data_type

            column_properties.append(f"{column_name} {data_type}")
        create_table_query += ", ".join(column_properties) + ");"
        new_c.execute(create_table_query)

        # Obtener datos de la tabla
        old_c.execute(f"SELECT * FROM {table_name};")
        rows = old_c.fetchall()

        # Insertar datos en MySQL
        if rows:
            placeholders = ", ".join(["%s"] * len(columns))  # Genera placeholders dinámicos
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            for row in rows:
                new_c.execute(insert_query, tuple(row))  # Convierte Row a tupla antes de insertar
            
            mysqll.commit()

        print(f"Tabla {table_name} migrada exitosamente.")

    # Agregar otras propiedades de las columnas y las relaciones entre tablas
    print("Aplicando modificaciones adicionales...")
    sql_script = query.other_properties()
    for statement in sql_script.split(';'):  # Divide el script en sentencias individuales
        if statement.strip():  # Ignorar líneas vacías
            new_c.execute(statement + ';')
    mysqll.commit()
    print("Modificaciones aplicadas exitosamente.")
except Error as e:
    print(f"Error en la conexión o migración: {e}")

finally:
    # Cerrar conexiones
    if sqlserver:
        old_c.close()
        sqlserver.close()
    if mysqll.is_connected():
        new_c.close()
        mysqll.close()