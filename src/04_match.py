from itertools import count


file = 'csv'
country = 'US'

if file == 'csv':
    print("File is in CSV format")
elif file == 'json':
    print("File is in JSON format")
else:
    print("Unknown file format")
match file:
    case 'csv':
        print("File is in CSV format")
    case 'json':
        print("File is in JSON format")
    case _:
        print("Unknown file format")

if(file == 'csv' or file == 'json'):
    print("File is in valid format")
elif(file == 'xml' and country == 'US'):
    print("File is in XML format and country is US")