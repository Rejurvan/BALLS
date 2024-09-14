#adad kamel
n = int(input())
l = []
for i in range(1,n):
    if n % i == 0:
        l.append(i)
if n == sum(l):
    print("Yes")
else:
    print("No")