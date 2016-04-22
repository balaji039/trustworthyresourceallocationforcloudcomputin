class attribute:
    def harddiskutilisation(self,n,array):

        sum=0
        for i in range(0,n):

            sum=sum+array[i]

        res=sum/n
        return res

    def memoryutilisation(self,n,array):

        sum=0

        for i in range(0,n):

            sum=sum+array[i]

        res=sum/n
        return res

    def cpuutilisation(self,n,array):
        sum=0
        for i in range(0,n):

            sum=sum+array[i]

        res=sum/n
        return res

    def bandwidthutilisation(self,n,array):
        sum=0
        for i in range(0,n):

            sum=sum+array[i]

        res=sum/n
        return res


class multiattribute:

    def matrix(self,array1,array2):

        self.ap=attribute()

        m1=len(array1)
        n=len(array1[0])
        m2=len(array2)

        n2=len(array2[0])


        hs=array1[2]
        ms=array1[3]

        #bs=array1[6]

        hs2=array2[2]
        ms2=array2[3]

        #bs2=array1[6]

        #hs3=array1[3]
        #ms3=array1[4]

        #bs3=array1[6]

        hr=self.ap.harddiskutilisation(n,hs)
        mr=self.ap.memoryutilisation(n,ms)
        #cr=self.ap.cpuutilisation(n,cs)
        #br=self.ap.bandwidthutilisation(n,bs)

        hr2=self.ap.harddiskutilisation(n2,hs2)
        mr2=self.ap.memoryutilisation(n2,ms2)
        #cr2=self.ap.cpuutilisation(n2,cs2)
        #br2=self.ap.bandwidthutilisation(n2,bs2)

        #hr3=self.ap.harddiskutilisation(n3,hs3)
        #mr3=self.ap.memoryutilisation(n3,ms3)
        #cr3=self.ap.cpuutilisation(n3,cs3)
        #br3=self.ap.bandwidthutilisation(n3,bs3)

        mat=[]
        mat.append([])

        mat[-1].append(array1[0][n-1])
        mat[-1].append(array1[1][n-1])
        #mat[-1].append(array1[2][n-1])
        mat[-1].append(hr)
        mat[-1].append(mr)
        #mat[-1].append(cr)
        #mat[-1].append(br)

        mat.append([])

        mat[-1].append(array2[0][n2-1])
        mat[-1].append(array2[1][n2-1])
        #mat[-1].append(array2[2][n2-1])
        mat[-1].append(hr2)
        mat[-1].append(mr2)
        #mat[-1].append(cr2)
        #mat[-1].append(br2)


        return mat



