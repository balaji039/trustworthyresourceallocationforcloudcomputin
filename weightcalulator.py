import math

#probability distribution calculation function
class prober:
    def probability(self,array,n,k,z):

        sum=0.0

        for i in range(0,n):

            sum=sum+array[i][k]
            #print sum
        #print array[z][k],float(sum)
        if(array[z][k]==0.0 and sum==0.0):
            pro=0.0
        else:
            pro=(array[z][k])/float(sum)
        return pro

#entrophy calculator for m attribute
class weightcalc:
    def __init__(self):
        self.pr=prober()

    def attributecalc(self,arr):
        hmat=[]
        no=len(arr)
        m=len(arr[0])
    #arr=[[1,2,3,4],[5,6,7,8]]
        ki=1/(math.log10(m))
        for i in range(0,m):

            sum=0

            for j in range(0,no):

                pe=self.pr.probability(arr,no,i,j)
                lnp=math.log10(pe)
                temp=pe*lnp
                sum=sum+temp

            temp2=(-ki)*sum
            hmat.append(temp2)

#y weight calculation

        yi=[]
        for i in range(0,m):

            sum1=0

            for g in range(0,m):

                temp=hmat[g]+1-(2*hmat[g])
                sum1=sum1+temp

            sum2=0

            for j in range(0,m):

                sum3=0

                for l in range(0,m):

                    temp=hmat[l]+1-(2*hmat[j])
                    sum3=sum3+temp

                sum2=sum2+sum3

            temp2=sum1/sum2
            yi.append(temp2)


# to calculate the entrophy weight

        summ=0
        for kj in range(0,m):

            summ=summ+yi[kj]

        w=[]

        for ki in range(0,m):

            temp=yi[ki]/summ
            w.append(temp)


        return w