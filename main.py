import DatabaseHandler
import JsonParser

import psycopg2
import json
import sys
import configparser

path = 'configClear_v2.json'
pathConfig = 'config.ini'

db = DatabaseHandler.DatabaseHandler(psycopg2, configparser, sys, pathConfig)
parser = JsonParser.JsonParser(json, sys)

resultData, resultPortId = parser.getInterfaceJson(path)

if resultData:
    db.deleteInterface()
    db.insertIntoInterfaceTable(resultData, resultPortId)
