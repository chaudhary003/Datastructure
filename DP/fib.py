#fibonacci nth term without DP
def fib(n):
    result=0
    if n ==1 or n==2:
        result= 1
        return result
    else:
        result=fib(n-1)+fib(n-2)
        return result
#fibonacci nth term using DP
def fib_memo(n):
    if not (n<=0):
        memo=[None]*(n+1)
        if memo[n] is not None:
            return memo[n]
        if n==1 or n==2:
            return 1
        else:
            result=fib_memo(n-1)+fib_memo(n-2)
            memo[n]=result
            return result
    else:
        return "invalid input"
#bottom_up approach
def fib_bottom(n):
    if not(n<=0):
        if n==1 or n==2:
            return 1
        else:
            arr=[1]*(n+1)
        #arr[0],arr[1]=1,1
            for i in range(3,n+1):
                arr[i]=arr[i-1]+arr[i-2]
            return arr[n]
    else:
        return "invalid input"
#finding fectorial without  DP
def fact(n):
    if not(n<0):
        if n==1 or n==0:
            return 1
        else:
            return n*fact(n-1)
    else:
        return "invalid input"
#fact using dp
def fact_memo(n):
    if not(n<0):
        memo=[None]*(n+1)
        if memo[n] is not None:
            return memo[n]
        if n==0 or n==1:
            return 1
        else:
            result=n*fact_memo(n-1)
            memo[n]=result
            return result
    else:
        return "invalid input"
def fact_bottom(n):
    if not(n<0):
        arr=[None]*(n+1)
        arr[0]=1
        arr[1]=1
        arr[2]=2
        for i in range(3,n+1):
            arr[i]=i*arr[i-1]
        return arr[n]
    else:
        return "invalid input"

'''knapsack problem'''
def knapsack(capacity, w, value,n):
    if not(capacity <=0 or n==0):
        if(w[n-1]>capacity):
            return knapsack(capacity,w, value ,n-1)
        else:
            return max(value[n-1]+knapsack(capacity-w[n-1],w,value, n-1),
            knapsack(capacity,value, w,n-1))


#testing
if __name__=="__main__":
    #fib_num=fib(10)
    #fib_memo=fib_memo(10)
    #fib_bottom=fib_bottom(-1)
    #print(fib_num)
    #print(fib_memo)
    #print(fib_bottom)
    #fact=fact_bottom(4)
    #print(fact)
    #fact=fact_memo(5)
    #print(fact)
    capacity=50
    w=[10,20,30]
    n=len(w)
    value=[60,100,120]
    total=knapsack(capacity,w,value, n)
    print(total)
