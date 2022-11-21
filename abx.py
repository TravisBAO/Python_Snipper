xxx = "5102, 'profileName', 'description', 4941, 4930, 'statusFlags', 'reliability', 'outOfService', 'deviceType', 5092, 5094, 5104, 'eventState', 'presentValue', 5107, 'units', 'resolution', 'minPresValue', 'maxPresValue', 5105, 5106, 'covIncrement', 5000"
yyy = xxx.replace("', '", "    ").replace(", '", "    ").replace("', ", "    ").replace(", ", "    ")
print(xxx)
print(yyy)
