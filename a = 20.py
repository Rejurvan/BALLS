import random
n = int(input("put a number here : "))
l = []
for i in range(n):
    l.append(random.randint(0,20))
print(l)
for i in range(n):
    temp = l[i]
    for j in range(1,i+1):
        if l[i-j] > temp :
         l[i-j+1] = l[i-j]
        else :
           l[i-j+1] = temp
           break
        if i == j :
           l[0] = temp
print(l)                   
x = int(input("what are you searching for?  "))
left = 0
right = n-1
flag = 0
while left <= right :
   m = (left+right)//2
   if l[m] == x :
      flag = 1
      #formated (in f)
      print(f"your key is {m+1}")
      break
   elif l[m] > x :
      right = m-1
   else :
      left = m+1
if  flag == 0    :
    print("key is not in there")
