def prime(num):
 l=num/2
 i=2
 while i<=l:
     if num%2==0:
         print("it is not a prime number")
         break
     i=i+i
 else:
        print("it is  a prime number")
a=int(input("enter the number"))
prime(a)


