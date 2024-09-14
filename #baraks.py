#baraks
l = []
n = ""
while not(n == 0):
    n = int(input())
    l.append(n)
for j in range(len(l)):
    for i in range(j,len(l)):
        l[i] , l[i+(len(l)-i-1)] = l[i+(len(l)-i-1)] , l[i]
for i in range(1,len(l)):
    print(l[i])