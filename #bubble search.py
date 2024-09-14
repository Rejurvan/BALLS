# # # # bubble search merge
# # # def bubble_search(l):
# # #     for i in range(len(l)):
# # #         for j in range(len(l)-i-1):
# # #             if l[j] > l[j+1]:
# # #                 temp = l[j]
# # #                 l[j] = l[j+1]
# # #                 l[j+1] = temp
# # #     return l
# # # import random
# # # n = int(input("put the legth of your list : "))
# # # l1 = []
# # # l2 = []
# # # for i in range(n):
# # #     l1.append(random.randint(1,100))
# # #     l2.append(random.randint(1,100))
# # # print(f"l1 = {l1}")
# # # print(f"l2 = {l2}")
# # # print(f"l1 sorted = {bubble_search(l1)}")
# # # print(f"l2 sorted = {bubble_search(l2)}")
# # # def merge(l1,l2,):
# # #     l3 = []
# # #     i = 0
# # #     j = 0
# # #     while i < len(l1)-1 and j < len(l2)-1 :
# # #         if l1[i] <= l2[j]:
# # #             l3.append(l1[i])
# # #             i += 1
# # #         else :
# # #             l3.append(l2[j])
# # #             j += 1
# # #     if i < len(l1) :
# # #         for i in range(i,len(l1)):
# # #             l3.append(l1[i])
# # #     if j < len(l2) :
# # #         for j in range(j,len(l2)):
# # #             l3.append(l2[j])
# # #     return l3
# # # print(merge(l1,l2))

# rah dovom




# # # # bubble search
# # # def bubble_search(l):
# # #     for i in range(len(l)):
# # #         for j in range(len(l)-i-1):
# # #             if l[j] > l[j+1]:
# # #                 temp = l[j]
# # #                 l[j] = l[j+1]
# # #                 l[j+1] = temp
# # #     return l
# # # import random
# # # n = int(input("put the legth of your list : "))
# # # l1 = []
# # # l2 = []
# # # for i in range(n):
# # #     l1.append(random.randint(1,100))
# # #     l2.append(random.randint(1,100))
# # # print(f"l1 = {l1}")
# # # print(f"l2 = {l2}")
# # # print(f"l1 sorted = {bubble_search(l1)}")
# # # print(f"l2 sorted = {bubble_search(l2)}")
# # # def merge(l1,l2,):
# # #     l3 = []
# # #     i = 0
# # #     j = 0
# # #     while i <= len(l1)-1 and j <= len(l2)-1 :
# # #         if l1[i] <= l2[j]:
# # #             l3.append(l1[i])
# # #             i += 1
# # #         else :
# # #             l3.append(l2[j])
# # #             j += 1
# # #     if i > len(l1)-1 :
# # #         l3.extend(l2[j:])
# # #     if j > len(l2)-1 :
# # #         l3.extend(l1[i:])
# # #     return l3
# # # print(merge(l1,l2))


# # # import random
# # # l = [random.randint(1,1000) for i in range(10)]
# # # print(l)
# # # print(l[3:6])