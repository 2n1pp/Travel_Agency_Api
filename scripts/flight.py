import psycopg2
import requests
import json
from requests_oauth2 import OAuth2BearerToken

pg_host = 'localhost'
pg_db = 'travel_agency'
pg_user = 'postgres'
pg_pasword = 'A123456b'

def get_token():
    urloi = "https://test.api.amadeus.com/v1/security/oauth2/token"
    api_key = ""
    api_secret = ""
    data = {'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': api_secret}

    r = requests.post(url = urloi, data = data)
    json_data = json.loads(r.text)
    return json_data['access_token']

def flight(origin, destination, departureDate, returnDate, adults, children, infants, token):

    conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
    cur = conn.cursor()
    cur.execute("select token from users where token = %s;", (token, ))

    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    if(rows == []):
        data = '3003'
    else:
        access_token = get_token()
        url2 = "https://test.api.amadeus.com/v1/shopping/flight-offers"
        query = {}
        if(origin != None or origin == ""):
            query["origin"] = origin
        
        if(destination != None or destination == ""):
            query["destination"] = destination
        
        if(departureDate != None or departureDate == ""):
            query["departureDate"] = departureDate
        
        if(returnDate != None or returnDate == ""):
            query["returnDate"] = returnDate
        
        if(adults != None or adults == ""):
            query["adults"] = adults
        
        if(children != None or children == ""):
            query["children"] = children
        
        if(infants != None or infants == ""):
            query["infants"] = infants

        query['max'] = '50'

        with requests.Session() as s:
            s.auth = OAuth2BearerToken(access_token)
            s.params = query 
            r = s.get(url2)
            r.raise_for_status()
            data = r.json()
    return data
