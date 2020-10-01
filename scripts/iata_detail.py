import psycopg2
import array as arr

pg_host = 'localhost'
pg_db = 'travel_agency'
pg_user = 'postgres'
pg_pasword = 'A123456b'

def getDetails(code, token):

    conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
    cur = conn.cursor()
    cur.execute("select token from users where token = %s;", (token, ))

    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    if(rows == []):
        response = '3003'
    else:
        conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
        cur = conn.cursor()
        cur.execute("select airport, type, city, country, iata from iata_codes where iata = '"+ code +"';")

        rows = cur.fetchall()
        cur.close()
        conn.close()
        for x in rows:
            res = "["+x[0]+","+x[2]+","+x[3]+","+x[4]+"]"

        response = {}
        response.update({"0" : res})
    
    return response
