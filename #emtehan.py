#emtehan

#soal dict
# import random
# dict1 = {}
# dict2 = {}
# dict3 = {}
# for i in range(15):
#     m = random.randint(1,20)
#     n = random.randint(25,30)
#     dict1[m] = n
# for i in range(15):
#     m = random.randint(1,20)
#     n = random.randint(25,30)
#     dict2[m] = n
# print(dict1)
# print(dict2)
# for i in dict1.keys() :
#     for j in dict2.keys() :
#         if i == j :
#             dict3[i] = dict1[i] + dict2[i]
# print(dict3)
import random
import time
a = []
for i in range(20):
    a.append(random.randint(1,200))



def merge2(l1,l2):
    i = 0
    j  = 0
    l3 = []
    while (i <= len(l1)-1) and (j <= len(l2)-1):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else :
            l3.append(l2[j])
            j += 1
        if i <= len(l1)-1:
            l3.extend(l1[i:])
        if j <= len(l2)-1:
            l3.extend(l2[j:])
    return l3

def merge_sort2(l):
    if len(l) < 2:
        return l
    r = len(l)//2
    l1 = l[:r]
    l2 = l[r:]
    l3 = merge_sort2(l1)
    l4 = merge_sort2(l2)
    l5 = merge2(l3,l4)
    return(l5)
    
def merge(l1,l2,l3):
    i = 0
    j = 0
    k = 0
    l4 = []
    while (i <= (len(l1)-1)) and (j <= (len(l2)-1)) and (k <= (len(l3)-1)) :
        if l1[i] <= l2[j] and l1[i] <= l3[k]:
            l4.append(l1[i])
            i += 1
        elif l2[j] <= l1[i] and l2[j] <= l3[k]:
            l4.append(l2[j])
            j += 1
        elif l3[k] <= l1[i] and l3[k] <= l2[j]:
            l4.append(l3[k])
            k += 1
        else :
            l4.append(l3[k])
            k += 1
    if i <= len(l1)-1:
        l4.extend(l1[i:])
    if j <= len(l2)-1:
        l4.extend(l2[j:])
    if k <= len(l3)-1:
        l4.extend(l3[k:])
    return l4

def merge_sort(l):
    if len(l) < 3:
        return l
    r = len(l)//3
    l1 = l[:r]
    l2 = l[r:2*r]
    l3 = l[2*r:]
    l4 = merge_sort(l1)
    l5 = merge_sort(l2)
    l6 = merge_sort(l3)
    l7 = merge(l4,l5,l6)
    return l7

t1 = time.time()
for i in range(2000):
    merge_sort2(a)
t2 = time.time()
tm2 = t2 - t1

t3 = time.time()
for i in range(2000):
    merge_sort(a)
t4 = time.time()
tm3 = t4 - t3

print(tm2/tm3)