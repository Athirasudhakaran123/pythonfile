def oddeven(o,e):
   o=[1,3,5,7,9]
   e=[2,4,6,8,10]
   o.extend(e)
   e.clear()
   for i in o:
      if i%2==0:
        o.append(i)
      else:
          e.append(i)
          o.remove(i)
          print(o)
          print(e)
oddeven(o,e)
