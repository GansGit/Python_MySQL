import bottle
from bottle import route, run
import MySQLdb as myDB

conn = myDB.connect('localhost', 'root', 'pass', 'test')
cur = conn.cursor()
cur.execute ("Select version()")
result = cur.fetchone()
print "DataBase version : %s" %result
########################
cur.execute ("Select * from books")
rows = cur.fetchall()
for row in rows:
    print row
