# # bubble search
# def bubble_search(l):
#     for i in range(len(l)):
#         for j in range(len(l)-i-1):
#             if l[j] > l[j+1]:
#                 temp = l[j]
#                 l[j] = l[j+1]
#                 l[j+1] = temp
#     return l
# import random
# n = int(input("put the legth of your list : "))
# l1 = []
# l2 = []
# for i in range(n):
#     l1.append(random.randint(1,100))
#     l2.append(random.randint(1,100))
# print(f"l1 = {l1}")
# print(f"l2 = {l2}")
# print(f"l1 sorted = {bubble_search(l1)}")
# print(f"l2 sorted = {bubble_search(l2)}")





def merge(l1,l2):
    i = 0
    j = 0
    l3 = []
    while (i <= len(l1)-1) and j <= (len(l2) - 1):
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



# # # import random
# # # import time
# # # l = []
# # # for i in range(100000):
# # #     l.append(random.randint(1,2000))
def merge_sort(l):
    if len(l) == 1 :
        return l
    r = len(l)//2
    l1 = l[:r]
    l2 = l[r:]
    l3 = merge_sort(l1)
    l4 = merge_sort(l2)
    l5 = merge(l3,l4)
    return l5



# # # def bubble_search(l):
# # #     for i in range(len(l)):
# # #         for j in range(len(l)-i-1):
# # #             if l[j] > l[j+1]:
# # #                 temp = l[j]
# # #                 l[j] = l[j+1]
# # #                 l[j+1] = temp
# # #     return l


# # # t1 = time.time()

# # # sorted(l)
# # # t2 = time.time()
# # # tb = t2 - t1
# # # print(t2-t1)
# # # t3 = time.time()

# # # merge_sort(l)
# # # t4 = time.time()
# # # tm = t4 - t3
# # # print(t4-t3)
# # # print(tm/tb)
l = [1,3,4,5,2,4,12,34,56,134,547,876,234,546,765,34,234]
print(merge_sort(l))