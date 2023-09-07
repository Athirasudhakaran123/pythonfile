def prime(num):
    l=int(num/2)
    for i in range(2,l+1):
            if num%i==0:
              print("it is not a prime number")
              break
            else:
              print("it is a prime number")
a=int(input("enter the number"))
prime(a)
