import requests

def count_words_starting_with_a(app_id, app_key):
    """
    Counts the number of words starting with the letter 'A' in the Oxford Dictionaries API.
    
    Args:
    app_id (str): Oxford Dictionaries API app ID.
    app_key (str): Oxford Dictionaries API app key.
    
    Returns:
    int: The number of words starting with 'A'.
    """
    language_code = "en-gb"
    url = f"https://od-api-sandbox.oxforddictionaries.com/api/v2/words/{language_code}"
    params = {
        "q": "a",  # Search for words containing 'A'
        "limit": 500  # Maximize the number of results (up to sandbox limits)
    }

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}, params=params)

    if r.status_code == 200:
        data = r.json()
        return len(data.get('results', []))
    else:
        print(f"Failed to fetch word data: {r.status_code}")
        print(f"Error response: {r.text}")
        return 0

# Replace with your actual app_id and app_key
app_id = "cebcae56"
app_key = "c1c1cd03a8e159bfe344ab6c5ece31b9"

word_count = count_words_starting_with_a(app_id, app_key)
print(f"Number of words starting with 'A': {word_count}")