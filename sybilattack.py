import mysql.connector as mys
import sys
class Sybilattack:
    def sybildetector(self):

        try:

                db=mys.connect(host='localhost',database='cloud',user='system',password='system123')
                cursor = db.cursor()
                quer="select count(userid) from usercredentials";
                cursor.execute(quer)
                at=int(cursor.fetchone()[0])
                query = "select * from usercredentials"
                cursor.execute(query)
                res = cursor.fetchall()
                mid = []
                self.ct=float(4)/float(at)
                self.cans=1-self.ct
                #print self.cans
                for row in res:
                    #print 'quwe'
                    qt = "select count(userid) from usercredentials where ipaddress='%s'" % (row[2])
                    cursor.execute(qt)
                    qtt=float(cursor.fetchone()[0])
                    #print qtt
                    t1 = float(qtt) /float (at)
                    #print t1
                    #print 'dfasdf'
                    qt2 = "select count(userid) from usercredentials where postaladdress='%s'" % (row[3])
                    cursor.execute(qt2)
                    qtt2 = float(cursor.fetchone()[0])
                    #print qtt2

                    t2 = float(qtt2) / float(at)
                    #print t2
                    #print 'sdfsd'
                    qt3 = "select count(userid) from usercredentials where hostname='%s'" % (row[4])
                    cursor.execute(qt3)
                    qtt3 = float(cursor.fetchone()[0])
                    #print qtt3
                    #print 'sdfsf'
                    t3 = float(qtt3) / float(at)
                    #print t3
                    qt4 = "select count(userid) from usercredentials where email='%s'" % (row[5])
                    cursor.execute(qt4)
                    qtt4 = float(cursor.fetchone()[0])
                    #print qtt4
                    t4 = float(qtt4) / float(at)
                    #print t4
                    #print "      "
                    res = t1 + t2 + t3 + t4
                    res2 = 1 - res
                    mid.append(res2)
                return mid

        except  mys.Error as err:

            print "Error:".format(err)
#me=Sybilattack()
#t=me.sybildetector()
#print t
