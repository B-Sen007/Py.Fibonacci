limit = int(input("enter the limit "))
a = 0
b = 1
         
for i in range(2,limit):
         c = a + b
         print(c)
         a=b
         b=c
         
