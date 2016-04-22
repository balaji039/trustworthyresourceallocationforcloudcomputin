import mysql.connector as mys
from collisionattack import attack
import matplotlib.pyplot as plt
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
          
db=mys.connect(host='localhost',database='cloud',user='system',password='system123')
cursor=db.cursor()
pi=attack()
t=pi.action()
sum=[]
for k in range(0,10):
  temp=0
  ct=0
  for ts in t:
     query="select rating from usersfeedback where cloudserviceid='%d' and userid='%d'" % (k,ts)
     cursor.execute(query)
     rs=int(cursor.fetchone()[0])
     temp=temp+rs
     ct=ct+1
  res2=float(temp)/float(ct)
  sum.append(res2)
sum2=[]
for k in range(0,10):
     temp=0
     ct=0
     query="select rating from usersfeedback where cloudserviceid='%d'" % (k)
     cursor.execute(query)
     rs=cursor.fetchall()
     for row in rs:
          temp=temp+int(row[0])
          ct=ct+1
     res2=float(temp)/float(ct)
     sum2.append(res2)
tl=minweight()
ret=tl.minmax(sum)
ret2=tl.minmax(sum2)
s = [0,1,2,3,4,5,6,7,8,9]
plt.plot(s,ret,color='r',marker='o',label='filtered feedback')
plt.plot(s,ret2,color='y',marker='*',label='selfpromotingattack')
#plt.plot(s,t2,color='b',marker='D',label='collisionfilter')
#plt.plot(s,t3,color='g',marker='o',label='allfilter')
plt.legend()
plt.axis([0,9,0,1])
# plt.axis([0, 6, 0, 1])
plt.ylabel('trustvalue')
plt.xlabel('csp')
plt.show()
