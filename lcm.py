def lcm(a, b):
   if a > b:
       largest = a
   else:
       largest = b

   while(True):
       if((largest % a == 0) and (largest % b == 0)):
           val = largest
           break
       largest += 1

   return val
