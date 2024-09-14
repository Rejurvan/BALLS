# # soal 1
# def fun():
#     global set
#     for i in range(5):
#         set = {i}
#         set.add(input("put the age here : "))
#     return set

# for i in range(len(set)):
#     l = {}
#     l.append({set[i]:  int(input()),})
# print(l)


# import random
# import time
# n = int(input("the length of your list : "))
# l = []
# for i in range(n):
#     l.append(random.randint(1,10000000000))
# for i in range(n):
#     for j in range(i,n):
#         if l[i] >= l[j]:
#             l[i] , l[j] = l[j] , l[i]

# #binary search
# def binary(l,key):
#     key = int(input("the number you are searching for : "))
#     left = 0
#     right = n-1
#     index = None
#     while left <= right :
#         m = (left + right)//2
#         if l[m] == key :
#             index = m
#             break
#         elif key < l[m] :
#             right = m-1
#         elif key > l[m] :
#             left = m+1
# def seq(l , key):
#     key = int(input("the number you are searching for : "))
#     for i in range(n):
#         if l[i] == key:
#             return i
# t1 = time.time()
# binary(l,5)
# t2 = time.time()
# tbin = t2 - t1
# print(tbin)
# t3 = time.time()
# seq(l,5)
# t4 = time.time()
# tseq = t4 - t3
# print(tseq)



#hanoy
def printit(from_a,to_a):
    print(f"move top ring of {from_a} to {to_a}")
def tower(n,A,B,C):
    if n == 1:
        printit(A,C)
    else :
        tower(n-1,A,C,B)
        printit(A,C)
        tower(n-1,B,A,C)
tower(5,'A','B','C')


#soal 6
l = [2,1,23,45,56,67,89,0,234]
max = ""
min = ""
for i in range(len(l)):
    for j in range(len(l)):
       if l[i] > l[j] :
           max = l[i]
       if l[i] < l[j] :
           min = l[i]
print(max)
print(min)
left = 0
right = len(l)
p = (left + right)//2
l[p] = min
l[p-1] = max

