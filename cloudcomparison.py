import MySQLdb as mys
import sys
import matplotlib.pyplot as plt

class Search:
    def search(self, array, n):
        for j in array:
            if (j == n):
                return 1
        return 0


class Comparer:

    def costloss(self):
        try:
            db = mys.connect('localhost', 'system', 'system', 'cloud')
            cursor = db.cursor()
            q="select count(userid) from userfeedback"
            cursor.execute(q)
            tc=int(cursor.fetchone()[0])
            que="select count(userid) from blacklist"
            cursor.execute(que)
            count1 = int(cursor.fetchone()[0])
            que2 = "select count(userid) from collisionblacklist"
            cursor.execute(que2)
            count2 = int(cursor.fetchone()[0])
            que3="select count(distinct userid) from userfeedback"
            cursor.execute(que3)
            totalcount=int(cursor.fetchone()[0])
            que8="select count(userid) from userfeedback where userid not in(select userid from blacklist)"
            cursor.execute(que8)
            tc2=int(cursor.fetchone()[0])
            que9 = "select count(userid) from userfeedback where userid not in(select userid from collisionblacklist)"
            cursor.execute(que9)
            tc3 = int(cursor.fetchone()[0])
            print 'wihtout trust'
            tque=count1+count2
            good=totalcount-tque
            percen=float(good)/float(tc)
            print percen
            percen2=float(good)/float(tc2)
            print percen2
            percen3=float(good)/float(tc3)
            print percen3
            print tc,tc2,tc3
            que4="select * from jobrequest"
            cursor.execute(que4)
            result=cursor.fetchall()
            count=0
            sum=0
            sum2=0
            sum3=0
            for row in result:
                cpu=int(row[1])
                mem=int(row[2])
                total=cpu+mem
                temp=total*percen
                temp2=total*percen2
                temp3=total*percen3
                rem=total-temp
                rem2=total-temp2
                rem3=total-temp3
                cost=rem*1
                cost2=rem2*1
                cost3=rem3*1
                sum=sum+cost
                sum2=sum2+cost2
                sum3=sum3+cost3
                #print sum,sum2,sum3
                count=count+1
                if(count==10):
                    break
            t=[]
            t1=[]
            t2=[]
            t.append(int(sum))
            t1.append(int(sum2))
            t2.append(int(sum3))
            #sum = 0
            #sum2 = 0
            #sum3 = 0
            for row in result:
                cpu = int(row[1])
                mem = int(row[2])
                total = cpu + mem
                temp = total * percen
                temp2 = total * percen2
                temp3 = total * percen3
                rem = total - temp
                rem2 = total - temp2
                rem3 = total - temp3
                cost = rem * 1
                cost2 = rem2 * 1
                cost3 = rem3 * 1
                sum = sum + cost
                sum2 = sum2 + cost2
                sum3 = sum3 + cost3
                #print sum,sum2,sum3
                count = count + 1
                if (count == 10):
                    break
            #t = []
            #t1 = []
            #t2 = []
            t.append(int(sum))
            t1.append(int(sum2))
            t2.append(int(sum3))
            #sum = 0
            #sum2 = 0
            #sum3 = 0
            for row in result:
                cpu = int(row[1])
                mem = int(row[2])
                total = cpu + mem
                temp = total * percen
                temp2 = total * percen2
                temp3 = total * percen3
                rem = total - temp
                rem2 = total - temp2
                rem3 = total - temp3
                cost = rem * 1
                cost2 = rem2 * 1
                cost3 = rem3 * 1
                sum = sum + cost
                sum2 = sum2 + cost2
                sum3 = sum3 + cost3
                count = count + 1
                if (count == 30):
                    break
            #t = []
            #t1 = []
            #t2 = []
            t3=[]
            t.append(int(sum))
            t1.append(int(sum2))
            t2.append(int(sum3))
            t3.append(0)
            t3.append(0)
            t3.append(0)
            s=[10,20,30]
            #print t,t1,t2

            plt.plot(s, t, color='r', marker='o', label='nofilter')
            plt.plot(s, t1, color='y', marker='*', label='sybilfilter')
            plt.plot(s, t2, color='b', marker='D', label='collisionfilter')
            plt.plot(s, t3, color='m', marker='D', label='allfilter')
            plt.legend()
            #plt.axis([0, 6, 0, 1])
            plt.ylabel('cost loss')
            plt.xlabel('jobsubmission')
            plt.show()
        except db.Error, e:

            print "Error %d: %s" % (e.args[0], e.args[1])

    def jobsucessrate(self):
        try:
            db = mys.connect('localhost', 'system', 'system', 'cloud')
            cursor = db.cursor()
            q = "select count(userid) from userfeedback"
            cursor.execute(q)
            tc = int(cursor.fetchone()[0])
            que = "select count(userid) from blacklist"
            cursor.execute(que)
            count1 = int(cursor.fetchone()[0])
            que2 = "select count(userid) from collisionblacklist"
            cursor.execute(que2)
            count2 = int(cursor.fetchone()[0])
            que3 = "select count(distinct userid) from userfeedback"
            cursor.execute(que3)
            totalcount = int(cursor.fetchone()[0])
            que8 = "select count(userid) from userfeedback where userid not in(select userid from blacklist)"
            cursor.execute(que8)
            tc2 = int(cursor.fetchone()[0])
            que9 = "select count(userid) from userfeedback where userid not in(select userid from collisionblacklist)"
            cursor.execute(que9)
            tc3 = int(cursor.fetchone()[0])
            print 'wihtout trust'
            tque = count1 + count2
            good = totalcount - tque
            percen = float(good) / float(tc)
            percen2 = float(good) / float(tc2)
            percen3 = float(good) / float(tc3)
            que4 = "select * from jobrequest"
            cursor.execute(que4)
            result = cursor.fetchall()
            count = 0
            sum = 0
            sum2=0
            sum3=0
            #print percen,percen2,percen3
            t=[]
            t1=[]
            t2=[]
            t3=[]
            res1=int(10*percen)
            print res1
            res2=int(10*percen2)
            print res2
            res3=int(10*percen3)
            print res3
            res4=int(10*1)
            temp=float(res1)/float(10)
            srate1=int(temp*100)
            print srate1
            temp = float(res2) / float(10)
            srate2 = int(temp * 100)
            print srate2
            temp = float(res3) / float(10)
            srate3 = int(temp * 100)
            print srate3
            temp=float(res4)/float(10)
            srate4=int(temp*100)
            print srate4
            t.append(srate1)
            t1.append(srate2)
            t2.append(srate3)
            t3.append(srate4)
            res1 = int(10 * percen)
            print res1
            res2 = int(10 * percen2)
            print res2
            res3 = int(10 * percen3)
            print res3
            res4 = int(10 * 1)
            temp = float(res1) / float(10)
            srate1 = int(temp * 100)
            print srate1
            temp = float(res2) / float(10)
            srate2 = int(temp * 100)
            print srate2
            temp = float(res3) / float(10)
            srate3 = int(temp * 100)
            print srate3
            temp = float(res4) / float(10)
            srate4 = int(temp * 100)
            print srate4
            t.append(srate1)
            t1.append(srate2)
            t2.append(srate3)
            t3.append(srate4)

            res1 = int(30 * percen)
            print res1
            res2 = int(30 * percen2)
            print res2
            res3 = int(30 * percen3)
            print res3
            res4 = int(30 * 1)
            temp = float(res1) / float(30)
            srate1 = int(temp * 100)
            print srate1
            temp = float(res2) / float(30)
            srate2 = int(temp * 100)
            print srate2
            temp = float(res3) / float(30)
            srate3 = int(temp * 100)
            print srate3
            temp = float(res4) / float(30)
            srate4 = int(temp * 100)
            print srate4
            t.append(srate1)
            t1.append(srate2)
            t2.append(srate3)
            t3.append(srate4)
            print t,t1,t2,t3

            s = [10, 20, 30]
            plt.plot(s,t,color='r',marker='o',label='nofilter')
            plt.plot(s,t1,color='y',marker='*',label='sybilfilter')
            plt.plot(s,t2,color='b',marker='D',label='collisionfilter')
            plt.plot(s,t3,color='g',marker='o',label='allfilter')
            plt.legend()
            plt.axis([10,30,0,110])
            # plt.axis([0, 6, 0, 1])
            plt.ylabel('jobsucessrate')
            plt.xlabel('jobsubmission')
            plt.show()
        except db.Error, e:

            print "Error %d: %s" % (e.args[0], e.args[1])

cs=Comparer()
cs.costloss()
cs.jobsucessrate()