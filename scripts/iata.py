import psycopg2
import array as arr

pg_host = 'localhost'
pg_db = 'travel_agency'
pg_user = 'postgres'
pg_pasword = 'A123456b'

def getCodes(token):
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
        cur.execute("select airport, type, city, country, iata from iata_codes;")

        rows = cur.fetchall()
        cur.close()
        conn.close()

        formatted_list = []
        for x in rows:
            if(x[2] == '' or x[2] == None):
                row = x[0] +  ", " + x[3] + " [" + x[4] + "]"
            else:
                row = x[0] + " - " + x[2] + ", " + x[3] + " [" + x[4] + "]"
            formatted_list.append(row)

        response = {}
        response.update({"0" : formatted_list})

    return response