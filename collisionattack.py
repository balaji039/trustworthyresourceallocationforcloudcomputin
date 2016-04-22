import mysql.connector as mys
import sys
from sybilattack import Sybilattack

class attack:
  def action(self):
    mt=Sybilattack()
    mids=mt.sybildetector()
    #print mids
    #print mt.cans
    try:
        db=mys.connect(host='localhost',database='cloud',user='system',password='system123')
        cursor = db.cursor()
        query = "select * from usercredentials"
        cursor.execute(query)
        res = cursor.fetchall()
        j=0
        for row in res:
            #t=find(mids,mids[j])
            #print t
            if(mids[j]!=mt.cans):
           #print 'hi'
                qs="select COUNT(1) from blacklist where userid='%d'" % (int(row[0]))
                cursor.execute(qs)
                t=cursor.fetchone()[0]
                if(t==0):
                    que="insert into blacklist values('%d')" % (int(row[0]))
                    cursor.execute(que)
                    db.commit()
            j=j+1
        #print 'done'
        ev=3
        D=[]
        t=[]
        for k in range(0,10):
            M1= "select count(distinct userid) from userfeedback where cloudserviceid='%d' and userid not in (select userid from blacklist)" % (k)
            cursor.execute(M1)
            M=int(cursor.fetchone()[0])
            V1= "select count(rating) from userfeedback where cloudserviceid=%d and userid not in (select userid from blacklist)" % (k)
            cursor.execute(V1)
            V = int(cursor.fetchone()[0])
            sum = 0.0
            for i in range(0, V):
                que = "select distinct userid from userfeedback where userid not in (select userid from blacklist)"
                cursor.execute(que)
                res = cursor.fetchall()
                temp=0.0
                for row in res:
                    ct = "select count(rating) from userfeedback where cloudserviceid = '%d' and userid = '%d' " % (k, int(row[0]));
                    cursor.execute(ct)
                    ct1=int(cursor.fetchone()[0])
                    if (ct1 > ev):
                        qs5 = "select COUNT(1) from collisionblacklist where userid='%d'" % (int(row[0]))
                        cursor.execute(qs5)
                        t2 = cursor.fetchone()[0]
                        if (t2 == 0):

                            bl="insert into collisionblacklist values('%d')" % (int(row[0]))
                            cursor.execute(bl)
                            db.commit()
                        tp = float(ct1)/float(V)
                    else:
                        tp = 0.0
                    temp=temp+tp
                sum = sum + tp
                #print sum
            L=1+sum
            #print L
            #print M
            #print V
            result=float(M)/float((V*L))
            D.append(result)

        query="select u.userid,(c.userid is not null) as cbl,(p.userid is not null) as sbl from usercredentials u left outer join collisionblacklist c on u.userid=c.userid left outer join blacklist p on u.userid=p.userid";
        cursor.execute(query);
        resu=cursor.fetchall();
        t=[]
        for row in resu:
           if(row[1]==0 and row[2]==0):
              t.append(int(row[0]))
        #print t       
        #print D
        
              
        
        return t
    except:

        print "Error"


