#Non Recursive Fib
def fib(n):
    if(n>0):
        a=0
        b=1
        print(a)
        print(b)
        for i in range(1,n):
            c=a+b
            print(c)
            a=b
            b=c
fib(8)
