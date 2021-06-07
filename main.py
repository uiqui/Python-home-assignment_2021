#custom classes
import DatabaseHandler
import JsonParser
#libs
import psycopg2
import json
import sys
import configparser


lengthFlag = not (len(sys.argv) == 3)
if lengthFlag:
    sys.exit()

pathJson = sys.argv[1]
pathConfig = sys.argv[2]

db = DatabaseHandler.DatabaseHandler(psycopg2, configparser, sys, pathConfig)
parser = JsonParser.JsonParser(json, sys)

resultData, resultPortId = parser.getInterfaceJson(pathJson)

if resultData:
    #db.deleteInterface() #for testing purposes
    db.insertIntoInterfaceTable(resultData, resultPortId)
