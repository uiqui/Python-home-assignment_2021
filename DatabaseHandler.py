
#self.psycopg2 = import psycopg2
class DatabaseHandler:
    def __init__(self, psycopg2):
        self.psycopg2 = psycopg2


    def __connect(self):
        con = self.psycopg2.connect(
                database="interfaceDB",
                user= "postgres",
                password="postgress",
                port="5432"
            )
        return con


    def __updatePortId(self, portIdList):
        try:
            con = self.__connect()
            cur = con.cursor()
            
            for pair in portIdList:
                sql_select_query = """SELECT id FROM interface WHERE name = %s"""
                str1 = str(pair[1])
                cur.execute(sql_select_query, [str1])
                portId = cur.fetchone()
                sql_update_query = """UPDATE interface SET port_channel_id = %s where name = %s"""
                cur.execute(sql_update_query, [portId, pair[0]])            
            con.commit()
            
        except (Exception, self.psycopg2.Error) as error:
            print("Error in update operation", error)
        finally:
            if cur:
                cur.close()
            if con:
                con.close()



    # data to insert
    # portIdList to add after insert
    def insertIntoInterfaceTable(self, data, portIdList):
        try:
            con = self.__connect()
            cur = con.cursor()

            sql_insert_query = """ INSERT INTO interface (name, description, config, max_frame_size) 
                                VALUES (%s, %s, %s, %s) """

            result = cur.executemany(sql_insert_query, data)
            con.commit()

            #port_channel_id
        except (Exception, self.psycopg2.Error) as error:
            print("Failed inserting record into interface table {}".format(error))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
        self.__updatePortId(portIdList)


    def deleteInterface(self):
        con = self.__connect()
        cur = con.cursor()

        cur.execute("DELETE FROM interface WHERE TRUE")
        con.commit()

        cur.close()
        con.close()


    def selectPrint(self):
        con = self.__connect()
        cur = con.cursor()

        cur.execute("select * from interface")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        con.close()