import sqlite3
db="student.sqlite3"

def query_db(q, data=None,a=0):
    con = sqlite3.connect(db)
    cur = con.cursor()

    if data is None:
        cur.execute(q)
    else: cur.execute(q,data)
    result=None
    if a==1:
        result=cur.fetchone()
    elif a==2:
        result = cur.fetchall()
    con.commit()
    con.close()
    return result