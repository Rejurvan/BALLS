import random
import time
n = 6000
l = []
for i in range(n):
    l.append(random.randint(100,1000))

for i in range(len(l)):
    temp = l[i]
    for j in range(1,i+1):
        if l[i-j] > temp :
            l[i-j+1] = l[i-j]
        else :
            l[i-j] = temp
        if j == i :
            l[0] = temp
print(l)            
def binary_search(l,key): 
    left = 0
    right = n+1
    index = None
    while left <= right :
        m = (left+right)//2
        if l[m] == key:
            index = m
            break
        elif key > m :
            left = m+1
        elif key < m :
            right = m-1
        
def sequentioal_search(l,key):
    for i in range(len(l)):
        if l[i] == key:
            return i
    return None\
    
t1 = time.time()
for i in range(1000):
    key = random.randint(100,1000)
    binary_search(l,key)
t2 = time.time()
print("elapsed time : \t ", t2 - t1 )
t_seq = t2 - t1

t1 = time.time()
for i in range(1000):
    key = random.randint(100,1000)
    sequentioal_search(l,key)
t2 = time.time()
print("elapsed time : \t ", t2 - t1 )
t_bin = t2 - t1

print(f"taqsume time ha mishe{t_seq/t_bin}")