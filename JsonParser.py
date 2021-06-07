
# self.json = import json
class JsonParser:
    def __init__(self, json, sys):
        self.json = json
        self.sys = sys    
    
    
    # path = path to json file
    def getInterfaceJson(self, path): 
        resultData = []
        resultPortId =[]

        try:
            file = open(path, 'r')
        except OSError:
            print ("Could not open/read file:", path)
            self.sys.exit()
        data = self.json.load(file)
        file.close()

        port_name = None
        dataInterface = data["frinx-uniconfig-topology:configuration"]["Cisco-IOS-XE-native:native"]["interface"]
        wordsOfInterest = ["Port-channel","Ethernet"]
        for key in dataInterface:
            for word in wordsOfInterest:
                if word in key:            
                    for value in dataInterface[key]:
                        name = str(key)+str(value["name"])
                        jsonData = self.json.dumps(value, separators=(',', ':'))
                        desc = None
                        max_frame = None
                        if "description" in value:
                            desc = value["description"]
                        if "mtu" in value:
                            max_frame = value["mtu"]
                        if "Cisco-IOS-XE-ethernet:channel-group" in value:
                            port_name = "Port-channel"+str(value["Cisco-IOS-XE-ethernet:channel-group"]["number"])
                        
                        resultData.append([
                            name,
                            desc,
                            jsonData,
                            max_frame
                        ])                       
                        
                        if port_name:
                            resultPortId.append([
                                name,
                                port_name
                            ])
                            port_name = None

        return resultData, resultPortId        
