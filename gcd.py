  def GCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
  
a=int(input( "Please enter the a : "))

b=int(input( "Please enter the b : "))

print (GCD(a,b))
