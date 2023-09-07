def oddeven(*n):
    l1=[]
    l2=[]
    for i in n:
     if i%2==0:
        l1.append(i)
        print(l1)
     else:
        l2.append(i)
        print(l2)
oddeven( 1,2,3,4,5,6,7)
