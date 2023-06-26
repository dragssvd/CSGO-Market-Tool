import requests
import pymongo

client = pymongo.MongoClient("172.17.0.2:27017")
db = client["csgo_items"]
collection = db["items"]


def get_item_info(item_name):
    item_data = collection.find_one(item_name)
    if item_data:
        # Extract relevant information from item_data
        
        try:
            average_price = item_data['price']['30_days']['average']
        except:
            average_price = "No data"
        
        print(average_price)
        
        item_info = {
            'name': item_data['name'],
            'description': item_data['type'],
            'average_price_30_days': average_price
        }
        
        return (item_info)
    else:
        return ({'name': 'error'})


import socket
import json

# Server configuration
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = (str)(s.getsockname()[0])
s.close()
PORT = 7777

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Client connected from {client_address}")

    # Receive data from the client
    received_data = client_socket.recv(1024)
    item_info = json.loads(received_data.decode())
    
    # Construct a response
    response = {
        'message': 'Item info received successfully',
        'item_info': get_item_info(item_info)
    }
    response_data = json.dumps(response).encode()

    # Send the response back to the client
    client_socket.sendall(response_data)

    # Close the connection with the client
    client_socket.close()