import mysql.connector as con
import subprocess
import re
from time import sleep
try:
    from config import nmap_command_args, connection_data as data
except:
    print("ERROR : connection data not imported from config.py")
    sleep(1)
    exit()


print()
print('"""""""""""""""""""""""""""""""""""""""""""""""""""')
print('"""""" Welcome to AutoNmap Script """""""""""""""""')
print('"""""""""""""""""""""""""""""""""""""""""""""""""""')
print()
print('"""""""""""""""""""""""""""""""""""""""""""""""""""')
print('"  PLEASE FOLLOW INSTRUCTIONS ON FILE README.txt  "')
print('"""""""""""""""""""""""""""""""""""""""""""""""""""')

if not data:
    print("ERROR : Please make sure to insert Data in Config.py")
    exit()

print("Connecting to Database : {} , as User : {}".format(str(data['database_name']), str(data['username'])))
sleep(1)
print("...")
sleep(1)
print("..")
sleep(1)
print(".")

try:
    mycon = con.connect(
        host=data['hostname'],
        user=data['username'],
        passwd=data['password'],
        database=data['database_name']
    )

except Exception as e:
    print("ERROR : {}".format(str(e)))
    print("ERROR : Please make sure to insert correct connection data in Config.py")
    exit()

sleep(1)
print("Connected !")
sleep(1)
print("Loading subdomains from table : {} , column : {}".format(data['table_name'], data['subdomains_column_name']))

mycursor = mycon.cursor()

mycursor.execute("SELECT {} FROM {}".format(data['subdomains_column_name'], data['table_name']))

results = list(mycursor)

for row in results:
    this_subdomain = str(row[0])
    print("Scanning Ports for Subdomain [{}]".format(this_subdomain))
    try:
        proc = subprocess.run(["nmap","{}".format(this_subdomain)], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print("ERROR : nmap tool not installed or not working!")
        print(str(e))
    output = proc.stdout
    sentences = output.split("\n")
    all_ports = ""
    for i in sentences:
        words = i.split(" ")
        for x in words:
            if re.match(r"[0-9]+\/[a-z]+", x):
                port = str(str(x).split("/")[0])
                if len(all_ports) == 0:
                    all_ports += port
                else:
                    all_ports += ","
                    all_ports += port
    if len(all_ports) > 0:
        print("Found Ports : ", all_ports)
        try:
            mycursor.execute("UPDATE {} SET {}='{}' WHERE {}='{}'".format(data['table_name'],data['ports_column_name'],all_ports,data['subdomains_column_name'],this_subdomain))
            mycon.commit()
            print("Ports inserted in table")
            print("----------------------------------------")
        except Exception as e:
            print("ERROR : Can't Insert ports in database")
            print(str(e))
    else:
        print("No Ports Found")
        print("----------------------------------------")
        continue
sleep(1)
print("Done Looping through all subdomains!")
sleep(1)
print("Please checkout the table for inserted ports")
print("Thanks for using this script")
