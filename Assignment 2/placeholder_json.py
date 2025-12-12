#fetch data from jsonfetch holder api and save to a file
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
with open("posts.json", "w") as f:
    json.dump(data, f, indent=4)

print("Fetched data from:", url)
print("Data saved to posts.json")
