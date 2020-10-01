import psycopg2
import array as arr
import random
import string

pg_host = 'localhost'
pg_db = 'travel_agency'
pg_user = 'postgres'
pg_pasword = 'A123456b'

def randomString(stringLength=65):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def authenticate(username, password):
    conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
    cur = conn.cursor()
    cur.execute("select username, password from users where username = %s;", (username, ))

    rows = cur.fetchall()
    cur.close()
    conn.close()
    for x in rows:
        ret_pass = x[1]
    if(ret_pass == password):
        response = randomString()
        try:
            conn = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pasword)
            cur = conn.cursor()
            cur.execute("UPDATE users SET token = %s where username = %s", (response, username))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(e)
    else:
        response = '3003'

    return response