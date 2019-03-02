def countTriplets(arr, r):
    hm1={}
    sum=0
    for k,i in enumerate(arr):
        if i not in hm1 :
            tempList={k}
            hm1[i]=tempList
        else:
            tempList=hm1[i]
            tempList.add(k)
            hm1[i]=tempList
        num=i/r
        num2=i/(r*r)
        if(num in hm1 and num2 in hm1):
            numList=hm1[num]
            num2List=hm1[num2]
            for elem in num2List:
                for elem2 in numList:
                    if(elem<elem2):
                        sum+=1
    print (sum)

if __name__ == "__main__":
    countTriplets([1,5,5,25,125],5)