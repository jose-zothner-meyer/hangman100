import requests
import json

app_id = "MY_ID"  # Your app ID
app_key = "MY_KEY"  # Your app key
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