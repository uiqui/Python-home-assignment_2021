import psycopg2

def selectPrint(cur):
    cur.execute("select * from interface")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def connect():
    con = psycopg2.connect(
            database="interfaceDB",
            user= "postgres",
            password="postgress",
            port="5432"
        )
    return con


def insertInto(con, cur, data):
    sql_insert_query = """ INSERT INTO interface (connection, name, description, config, type, infra_type, port_channel_id, max_frame_size) 
                           VALUES (%d, %s, %s, %s, %s, %s, %d, %d) """
    result = cursor.executemany(sql_insert_query, data)
    connection.commit()


#cur.execute("INSERT INTO interface VALUES (2,2,3, 4, NULL, 6, 7 )")


con = connect()
cur = con.cursor()

selectPrint(cur)

cur.close()

con.close()
