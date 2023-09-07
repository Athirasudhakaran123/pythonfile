def oddeven(*n):
 l1=[]
 l2=[]
for i in n:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
     print("even:",l1)
     print("odd:",l2)
oddeven(*n 1,2,3,4,5,6,7,8,9)

