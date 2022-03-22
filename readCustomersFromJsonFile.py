import json

def readJsonFile(filename) :
    data = ""
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
    except IOError:
        print("could not read file")
    return data



data = readJsonFile('customers.json')
lenCustomers = len(data['customers']['customer'])

for i in range(0,lenCustomers) :
    print(f"{i+1}. Customer ID : {data['customers']['customer'][i]['customerID']}", end = " -->")
    print(f" {data['customers']['customer'][i]['customerName']}", end = ", ")
    print(f"{data['customers']['customer'][i]['customerAddress']}, {data['customers']['customer'][i]['customerCity']}, {data['customers']['customer'][i]['customerState']}", end = " -->")
    print(f" {data['customers']['customer'][i]['customerPhone']}\n")

