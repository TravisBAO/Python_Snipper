# the file is to config the network data of AX100PB3

import json

AX100PB3_initData = {
    "NetWorkConfiguration": 
    {
        "IUT_IPV4_Address": "192.168.0.102",
        "UDPPort": 47808,
        "Local_IPV4_Address": "192.168.0.114"
    },
    "ModbusMasterTestingConfiguration": 
    {
        "SerialPort": 855, # COM port ID
        "BaudRate": 9600,
        "Parity": 1,
        "SerialMode": 0,
        "SlaveID": 1
    },
    "ModbusSlaveTestingConfiguration": 
    {
        "SerialPort": 9, # COM port ID
        "BaudRate": 9600,
        "Parity": 1,
        "SerialMode": 4
    }
}

with open("C:\\Users\\z003uadu\\Desktop\\InitData.JSON", 'w') as jsonfile:
    json.dump(AX100PB3_initData,jsonfile)
