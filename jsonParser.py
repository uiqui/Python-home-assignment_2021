import json




path = 'configClear_v2.json'

resultData = []
resultPortId =[]

file = open(path, 'r')
data = json.load(file)
file.close()

dataInterface = data["frinx-uniconfig-topology:configuration"]["Cisco-IOS-XE-native:native"]["interface"]
wordsOfInterest = ["Port-channel","Ethernet"]
for key in dataInterface:
    for word in wordsOfInterest:
        if word in key:
            
            print(key)
            for value in dataInterface[key]:
                print(value["name"])
                if value["description"]:
                    resultData.append((
                        key+value["name"],#name
                        value["description"],#description optional
                        value["mtu"],#max frame size optional
                        value
                    ))
                    resultPortId.append((
                        key+value["name"],#name
                        "Port-channel"+value["Cisco-IOS-XE-ethernet:channel-group"]["number"]
                    ))
                    

                input()
           
        
