import requests
import json

app_id = "cebcae56"  # Your app ID
app_key = "c1c1cd03a8e159bfe344ab6c5ece31b9"  # Your app key
language = "en-gb"
word_id = "apple"  # A word starting with "A"
url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/{language}/{word_id.lower()}"

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

if r.status_code == 200:
    print("API request successful!")
    print(json.dumps(r.json(), indent=2))  # Pretty print the JSON response
else:
    print(f"Failed to fetch word data: {r.status_code}")
    print(r.text)