# Python home assignment_2021
 job_interview

date: 6.5.2021

language:
Python 3.9

librarys:
psycopg2
json
sys
configparser

fixes:
json file, line 1890, extra ","

useage:
run main script with parameters
[0] = 'configClear_v2.json' #path to json file with data to extract and insert to database
[1] = 'config.ini'          #path to config file with credentials to log into database

#config file should contain:
#database
#user
#password
#port

app overview:
get paths to json file and configfile
pass json file interface information to database table interface