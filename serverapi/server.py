import requests
import pymongo

# Establish connection to MongoDB
client = pymongo.MongoClient("172.17.0.2:27017")
db = client["csgo_items"]
collection = db["items"]

# API endpoint
url = "http://csgobackpack.net/api/GetItemsList/v2/?currency=PLN"

# Send request to the API
response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200 and data["success"]:
    print('API Connected!')
    # Extract item list from the JSON response
    items_list = data["items_list"]

    # Iterate over each item and insert it into MongoDB
    for item_name, item_data in items_list.items():
        collection.insert_one(item_data)
    
    print("Data inserted successfully!")
else:
    print("Request failed or API returned unsuccessful response.")

# Close the MongoDB connection
client.close()
