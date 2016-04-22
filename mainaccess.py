import mysql.connector as mys
import getpass
import sys
from mainframe import mainframe
from collisionattack import attack
from inputgathere import result
class minweight:
    def maximum(self,a,b):
        if(a>b):
            return 1
        else:
            return 2
    def minmax(self,array):
        #for i in range(0,self.row):
            mini = min(array)
            maxi = max(array)
            #self.y.append([])
            result=[]
            for ele in array:
                temp = ele - mini
                temp2 = maxi - mini
                temp3 = temp * (0.99 - 0.01)
                res = float(temp3) / float(temp2)
                #print res
                res2 = 0.01 + float(res)
                #print res2
                result.append(res2)
            return result
class MainAccess:
    def create(self):
        db=mys.connect(host='localhost',database='cloud',user='system',password='system123')
        cursor=db.cursor()
        mf=mainframe()
        mt=mf.T                    
        #print mt
        tru=[]
        tru1=[]
        for i in range(0,10):
        #tru.append([]
            sum=0
            usum=0
            for j in range(0,4):
               sum=sum+mt[i][j]
            for k in range(4,8):
                usum=usum+mt[i][k]
            tru.append(sum*2)
            tru1.append(usum*2)
        #print tru,tru1
        pi=attack()
        t=pi.action()
        sum=[]
        sec=[]
        for p in range(0,10):
            que="select sec from security where cloudid='%d'" %(p)
            cursor.execute(que)
            res=int(cursor.fetchone()[0])
            sec.append(res)
        for k in range(0,10):
            temp=0
            ct=0
            for ts in t:
                query="select rating from userfeedback where cloudserviceid='%d' and userid='%d'" % (k,ts)
                cursor.execute(query)
                rs=int(cursor.fetchone()[0])
                temp=temp+rs
                ct=ct+1
            res2=float(temp)/float(ct)
            sum.append(res2)
        #print sum
        #print sum
        #sum2=[1,1.5,2,2.5,3,3.5,4,4.5,5]
        #print sum2
        tl=minweight()
        ret=tl.minmax(sum)
        sec1=tl.minmax(sec)
        #print sec1
        #print ret
        #tru=[0.3223603221798172, 0.99, 0.3450511449365403, 0.3192616712523298, 0.11932801544333009, 0.21607115913730365, 0.17092327150084316, 0.01, 0.02322091062394603, 0.47714609035235644]
        #tru1=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        #tru=[0.5647694979969955, 0.99, 0.40789496745117676, 0.37726996745117675, 0.13983420443164749, 0.25472396094141214, 0.2011072076865298, 0.01, 0.025703555332999495, 0.5647694979969955]
        #tru1=[0.01, 0.99, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        atp=result()
        favail=[]
        futil=[]
        ffeed=[]
        fsec=[]
        for i in range(0,10):
            tp=atp.rangecalculator("D:\\cloud\\availability.txt",tru[i])
            favail.append(tp)
        for i in range(0,10):
            tp1=atp.rangecalculator("D:\\cloud\\utilisation.txt",tru1[i])
            futil.append(tp1)
        for i in range(0,10):
            tp2=atp.rangecalculator("D:\\cloud\\feedback.txt",ret[i])
            ffeed.append(tp2)
        for i in range(0,10):
            tp3=atp.rangecalculator("D:\\cloud\\security.txt",sec1[i])
            fsec.append(tp3)
        
        fsum=[]
        #print favail,futil,ffeed,fsec
        for i in range(0,10):
            tp4=atp.computeresult(ffeed[i],favail[i],futil[i],fsec[i])
            #print tp4
            fsum.append(tp4)
        #if fsum[0]=='HIGH':
            #print fsum[0]
        #print fsum
        
        #maxi=max(fsum)
        
        #print fsum
        for i in range(0,10):
            bl="insert into trustcloud values('%d','%s')" % (int(i),fsum[i])
            cursor.execute(bl)
            db.commit()
        #print 'commited'
        #System.out.println("commited");'''
        '''mi=minweight()
        pi=attack()
        ts=pi.action()
        c1=tru[0]+ts[0]
        c2=tru[1]+ts[1]
        maxi=mi.maximum(c1,c2)'''           
m=MainAccess()
m.create()

                      
       
                     

