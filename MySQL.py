import bottle
from bottle import route, run
import MySQLdb as db

def GetAllAuthors():
    connect = db.connect('localhost', 'root', 'pass', 'test')
    with connect:
        curs = connect.cursor()
        curs.execute("Select * from authors")
        rows = curs.fetchall()
        desc = curs.description
        print desc
        print "%s %s %s %s" % (desc[0][0], desc[1][0], desc[2][0], desc[3][0])
        for row in rows:
            print "%d %s %s %s" % row
    curs.close()
GetAllAuthors()
