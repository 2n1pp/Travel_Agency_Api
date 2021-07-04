import requests
import json
from requests_oauth2 import OAuth2BearerToken


def get_token():
    urloi = "https://test.api.amadeus.com/v1/security/oauth2/token"
    api_key = "5ThsBs5GbFyWhKqf1LTgmpHvXziehHw1"
    api_secret = "TYPsoO9JOCMsmYCq"
    data = {'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': api_secret}

    r = requests.post(url = urloi, data = data)
    json_data = json.loads(r.text)
    return json_data['access_token']


def prove():
    access_token = get_token()
    url2 = "https://test.api.amadeus.com/v1/shopping/flight-offers"
    query = {'origin': 'NYC',
            'destination': 'MAD',
            'departureDate':'2020-10-01',
            'max':'8'}

    with requests.Session() as s:
        s.auth = OAuth2BearerToken(access_token)
        s.params = query 
        r = s.get(url2)
        r.raise_for_status()
        data = r.json()
    return data