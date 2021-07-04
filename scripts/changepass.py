import psycopg2
import string

pg_host = 'localhost'
pg_db = 'travel_agency'
pg_user = 'postgres'
pg_pasword = 'A123456b'

def changePass(oldpass, newpass, token):
    try:
        conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
        cur = conn.cursor()
        cur.execute("select password from users where token = '" + token + "'")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        print(rows[0][0])
    except Exception as e:
        print(e)
        
    if(oldpass == rows[0][0]):
        try:
            conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
            cur = conn.cursor()
            cur.execute("UPDATE users SET password = %s where token = %s", (newpass, token))
            conn.commit()
            cur.close()
            conn.close()
            response = "200"
        except Exception as e:
            print(e)
    else:
        response = "500"
    
    return response
