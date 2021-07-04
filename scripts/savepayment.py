import psycopg2

pg_host = 'localhost'
pg_db = 'travel_agency'
pg_user = 'postgres'
pg_pasword = 'A123456b'
id = 1

def savePayment(holdername, cardnumber, cvv, expiration, token):
    conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
    cur = conn.cursor()
    cur.execute("select token from users where token = %s;", (token, ))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    if(rows == []):
        response = 'token s eshte ok'
    else:
        try:
            conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
            cur = conn.cursor()
            cur.execute("UPDATE payment SET holder_name = %s, card_number = %s, cvv = %s, expiration_date = %s where id = %s", (holdername, cardnumber, cvv, expiration, id))
            conn.commit()
            cur.close()
            conn.close()
            response = "200"
        except Exception as e:
            response = "update futja kot"
            
    return response
