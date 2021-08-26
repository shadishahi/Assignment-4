def gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

n=int(input())
m=int(input())

print("lcm: ", lcm(n, m))
