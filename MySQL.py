import bottle
from bottle import route, run
import MySQLdb as myDB

conn = myDB.connect('localhost', 'root', 'pass', 'test')
cur = conn.cursor()
cur.execute ("Select version()")
result = cur.fetchone()
print "DataBase version : %s" %result
