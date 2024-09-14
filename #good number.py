#good number
k = int(input())
for j in range(1,20*(k+1)):
    l = []
    lst = []
    for i in range(1,j+1):
        l.append(i)
        lst.append(sum(l))
for i in range(len(lst)):
    l1 = set()
    if lst[i] > k :
        for j in range(1,lst[i]):
                    if lst[i] % j == 0 :
                        l1.add(j)
    if (len(l1)+1) >= k:
        print(lst[i])
        break


