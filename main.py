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

        sql_insert_query = """ INSERT INTO interface (name, description, config, max_frame_size) 
                            VALUES (%s, %s, %s, %d) """
        result = cur.executemany(sql_insert_query, data)
        con.commit()

        #port_channel_id
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table{}".format(error))
    finally:
        if con:
            cur.close()
            con.close()


selectPrint()