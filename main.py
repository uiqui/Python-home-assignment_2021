import DatabaseHandler
import JsonParser

import psycopg2
import json

path = 'configClear_v2.json'

db = DatabaseHandler.DatabaseHandler(psycopg2)
parser = JsonParser.JsonParser(json)

resultData, resultPortId = parser.getInterfaceJson(path)

db.deleteInterface()
db.insertIntoInterfaceTable(resultData, resultPortId)
