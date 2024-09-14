#traning




# #fibb
# k = int(input())
# a = 0
# b = 1
# if k < 1 :
#     print(0)
# elif k < 2:
#     print(1)
# else :
#     for i in range(1,k):
#         c = a + b
#         a = b
#         b = c
# print(c)



#insertion sort
# a=[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 111 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 0]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         if a[i] > a[j]:
#             a[i] , a[j] = a[j] , a[i]
# print(a)



#tedad argham
# k = int(input())
# c = 1
# while not (k//10 == 0) :
#     k = k//10
#     c += 1
# print(c)



#zoj va fard
# import random
# for i in range(1 , 100):
#     a = random.randint(1,20000)
#     if a % 2 == 0 :
#         print(" it is even")
#         c = 1
#         while not(a//10 == 0):
#             a = a//10
#             c+=1
#         print(c)
#     else :
#         print("it is odd")




#bubble sort
# a=[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 111 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 0]
# def bubble_sort(l):
#     for i in range(len(l)):
#         for j in range(len(l)-i-1):
#             if l[j] > l[j+1]:
#                 temp = l[j]
#                 l[j] = l[j+1]
#                 l[j+1] = temp
#     return l


#merge
# def merge(l1,l2):
#     i = 0
#     j = 0
#     l3 = []
#     while (i <= len(l1) -1) and (j <= len(l2)-1):
#         if l1[i] <= l2[i]:
#             l3.append(l1[i])
#             i += 1
#         else :
#             l3.append(l2[j])
#             j += 1
#         if i <= len(l1) -1 :
#             l3.extend(l1[i:])
#         if j <= len(l2) - 1:
#             l3.extend(l2[j:])
#         return l3





#merge sort
# def merge_sort(l):
#     if len(l) < 1 :
#         return l
#     r = len(l)//2
#     l1 = l[r:]
#     l2 = l[:r]
#     l3 = merge_sort(l1)
#     l4 = merge_sort(l2)
#     l5 = merge(l3,l4)
#     return l5



# # # def binary_search(l,key):
# # #     left = 0
# # #     right = n-1
# # #     index = None
# # #     while left <= right :
# # #         m = (right+left)//2
# # #         if l[m] == key :
# # #             index = m
# # #             break 
# # #         elif l[m] > key :
# # #             right = m-1
# # #         else :
# # #             left = m+1


#matrix moment
# import random
# def make_matrix(n,m):
#     l = [[random.randint(1,100)for i in range(n)]for j in range(m)]
#     return l


# l1 = make_matrix(2,2)
# l2 = make_matrix(2,2)


# def zarb_matrix(l1,l2):
#     l3 = [[0 for i in range(len(l1))]for i in range(len(l2))]
#     for i in range(len(l1)):
#         for j in range(len(l1)):
#             for k in range(len(l1)):
#                 l3[i][j] += l1[i][k] * l2[k][j]
#     return l3

# print(zarb_matrix(l1,l2))
