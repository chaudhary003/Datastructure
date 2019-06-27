def selection_sort(lis):
    n=len(lis)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if lis[j]<lis[min]:
                min=j
        temp=lis[i]
        lis[i]=lis[min]
        lis[min]=temp
def bubble_sort(lis):
    n=len(lis)
    #flag=False
    count=0
    for i in range(n):
        for j in range(n-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
                flag=True
        count +=1
        #if flag==False:
            #break
    print(count)
def insertion_sort(lis):
    n=len(lis)
    for i in range(1,n):
        current=lis[i]
        j=i
        while j>0 and lis[j-1]>current:
             lis[j]=lis[j-1]
             j-=1
             lis[j]=current

def merge(lis1,lis2,lis):
    i=j=0
    while i+j < len(lis):
        if j==len(lis2) or (i<len(lis1) and lis1[i]<lis2[j]):
            lis[i+j]=lis1[i]
            i+=1
        else:
            lis[i+j]=lis2[j]
            j+=1

def merge_sort(lis):
    n=len(lis)
    if n<2:
        return
    mid=n//2
    lis1=lis[0:mid]
    lis2=lis[mid:n]
    #print(lis1)
    #print(lis2)
    merge_sort(lis1)
    merge_sort(lis2)
    merge(lis1,lis2,lis)






if __name__=="__main__":
    lis=[2,7,4,1,5,3,90,19,6,78,91,43,23]
    #print(lis)
    #selection_sort(lis)
    #print(lis)
    #bubble_sort(lis)
    #print(lis)
    lis1=[1,3,4,5,6,8,9,20]
    bubble_sort(lis1)
    print(lis1)
    #insertion_sort(lis)
    #merge_sort(lis)
    #print(lis)
