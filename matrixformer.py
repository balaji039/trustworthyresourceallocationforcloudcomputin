import mysql.connector as mys
import sys

class matrixcomputation:
    def __init__(self):
        self.db=mys.connect(host='localhost',database='cloud',user='system',password='system123')
        self.cursor=self.db.cursor()

    def cloud2(self):
        try:
            #for i in range(0,4):
            arr=[]
            for i in range(0,10):
                arr.append([])
                que2="select * from rerources where hostid=%d" % (i);
                self.cursor.execute(que2)
                res=self.cursor.fetchall()
                for row in res:
                    #print row[j]
                    arr[-1].append(int(row[0]))
                    arr[-1].append(int(row[1]))
                    arr[-1].append(int(row[2]))
                    arr[-1].append(int(row[3]))
                    arr[-1].append(int(row[4]))
                    arr[-1].append(int(row[5]))
                    arr[-1].append(int(row[6]))
                    arr[-1].append(int(row[7]))
            #print arr
        except:
            print 'error'
        return arr

