def sum(num):
 s=0
 for i in range(0,num+1):
        if i%2==0:
            print(i)
            s=i
            print("sum of all even numbers")
a=int(input("enter the number"))
sum(a)
