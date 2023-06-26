import socket
import json

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

wears=[
    "Factory New",
    "Minimal Wear",
    "Field-Tested",
    "Battle-Scarred",
    "Well-Worn"
]

item_info = {
    'name': 'AK-47 | Aquamarine Revenge (Battle-Scarred)',
}

def request_from_server(item_info):

    # Send request to the server
    item_info_json = json.dumps(item_info).encode()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    client_socket.sendall(item_info_json)

    # Receive the response from the server
    response_data = client_socket.recv(1024).decode()
    response = json.loads(response_data)

    # Close the connection with the server
    client_socket.close()
    
    return response

def list_weapons():
    print("List of weapons:\n" +
          "AK-47\n" +
          "AWP\n" +
          "M4A4\n" +
          "M4A1-S\n" +
          "and more...")
    
def list_exterior_wear():
        print("List of exterior wear:\n" +
          "Factory New\n" +
          "Minimal Wear\n" +
          "Field-Tested\n" +
          "Battle-Scarred\n" +
          "Well-Worn")
    
print("<- CSGO Steam market price checker ->\n")
print("<- check available weapons -> weapons ->")
print("<- check price -> price ->")
print("<- check wear -> wear ->")
print("<- exit ->")

while(True):
    action = input('Enter what you want to do:').lower()
    if(action == 'wear'): list_exterior_wear()
    elif(action == 'weapons'): list_weapons()
    elif(action == 'price'):
        info_chart = []  
        weapon = input('Enter your weapon type:')
        skin = input('Enter your desired skin finish:')
        for wear in wears:
            item_info['name'] = weapon.upper() + ' | ' + skin + " (" + wear + ")"
            response = request_from_server(item_info)
            data = response['item_info']
            if(data['name'] == 'error'):
                print(item_info['name'] + "\t\t - " + "No data")
            else:
                print(item_info['name'] + "\t\t - " + str(data['average_price_30_days']) + " PLN")
        for wear in wears:
            item_info['name'] ='StatTrak\u2122 ' + weapon.upper() + ' | ' + skin + " (" + wear + ")"
            response = request_from_server(item_info)
            data = response['item_info']
            if(data['name'] == 'error'):
                print(item_info['name'] + "\t\t - " + "No data")
            else:
                print(item_info['name'] + "\t\t - " + str(data['average_price_30_days']) + " PLN")
    elif(action == 'exit'): break
    else: print('Wrong input...')

