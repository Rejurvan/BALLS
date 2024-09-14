#quick sort
l = [2,4,1,91,50,21,343,5]

def quick_sort(l):
    left = []
    right = []
    mid = []
    if len(l) > 1:
        pvet = l[len(l)//2]
        for i in l:
            if i > pvet:
                right.append(i)
            if i < pvet:
                left.append(i)
            if i == pvet:
                mid.append(i)
            l = []
            for i in quick_sort(left):
                l.append(i)
            for i in quick_sort(mid):
                l.append(i)
            for i in quick_sort(right):
                l.append(i)
    return(l)

print(quick_sort(l))