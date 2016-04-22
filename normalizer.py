import math

class minmax:
    def minim(self,array,c):
        length=len(array)
        minimum=array[0][c]
        for i in range(0,length):
            if(array[i][c]<minimum):
                minimum=array[i][c]
        return minimum
    def maxim(self,array,c):
        length=len(array)
        #print '############'
        #print length,c
        maximum=array[0][c]
        for i in range(0,length):
            if(array[i][c]>maximum):
                maximum=array[i][c]
        return maximum
class countinteger:
    def count(self,no):
        count=0
        while(no>=10):
            count=count+1
            no=no/10
        count=count+1
        return count
    def firstdigit(self,n):
        while(n>=10):
            n=n/10
        return n

class normaliser:
    def __init__(self,arr):

        self.ce=minmax()
        self.array=arr
        #arr=[[1,2],[3,4]]
        self.row=len(arr)
        self.col=len(arr[0])
        self.y=[]
        #self.A=arr[0][0]

    def minmax(self):
        for i in range(0,self.row):
            self.y.append([])
            for j in range(0, self.col):
                mini=self.ce.minim(self.array,j)
                maxi=self.ce.maxim(self.array,j)
                #print mini,maxi
                temp = self.array[i][j] - mini
                temp2 = maxi - mini
                temp3 = temp * (0.99 - 0.01)
                if(temp3==0 and temp2==0):
                    res=0
                else:
                    res = float(temp3) / float(temp2)
                #print res
                res2 = 0.01 + float(res)
                #res2=0
                #print res2
                self.y[-1].append(res2)
        return self.y

    #normalization procedure calculation
    def normalizematrix(self):
        for i in range(0,self.row):
            self.y.append([])
            for j in range(0,self.col):
                n=self.ce.count(self.array[i][j])
                x=self.array[i][j]
                A=self.ce.firstdigit(x)
                temp=n-1
                te=math.pow(10,temp)
                res=((x)-(te*A))/te
                self.y[-1].append(res)

        return self.y
