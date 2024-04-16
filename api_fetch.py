import requests
from constants import BASE_URL

def fetch_data(endpoint, topic_id = None, country_code = None, indicator_id = None):
    url = BASE_URL + endpoint
    if topic_id:
        url += "/" + topic_id + "/indicator"
    elif country_code:
        url += "/" + country_code + "/indicators/" + indicator_id
    url += "?format=json"
    print(url)
    response = requests.get(url)
    return response.json() if response.status_code == 200 else print("Failed to fetch data from the API:", response.status_code)