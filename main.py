import psycopg2

def selectPrint():
    con = connect()
    cur = con.cursor()

    cur.execute("select * from interface")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    con.close()



def connect():
    con = psycopg2.connect(
            database="interfaceDB",
            user= "postgres",
            password="postgress",
            port="5432"
        )
    return con


def insertInto(data):
    try:
        con = connect()
        cur = con.cursor()

        sql_insert_query = """ INSERT INTO interface (connection, name, description, config, type, infra_type, port_channel_id, max_frame_size) 
                            VALUES (%d, %s, %s, %s, %s, %s, %d, %d) """
        result = cur.executemany(sql_insert_query, data)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table{}".format(error))
    finally:
        if con:
            cur.close()
            con.close()


selectPrint()