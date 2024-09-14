#matrix
import random
# a = int(input("put the number of rows : "))
# b = int(input("put the number of columns : "))
# l1 = []
# for i in range(a):
#     l1.append([])
# print("now for l1 valiues \n")
# for i in range(a):
#     for j in range(b):
#         print(f"l1[{i}][{j}] : " , end="")
#         x = int(input())
#         l1[i].append(x)
# c = int(input("put the number of rows : "))
# d = int(input("put the number of columns : "))
# l2 = []
# for i in range(c):
#     l2.append([])
# print("now for l2 valiues \n")
# for i in range(c):
#     for j in range(d):
#         print(f"l1[{i}][{j}] : " , end="")
#         x = int(input())
#         l2[i].append(x)
# print(l1)
# print(l2)
n = int(input("put the number of rows : "))
m = int(input("put the number of columns : "))
def makeM(n,m):
    l = [[random.randint(1,100) for i in range(n)] for j in range(m)]
    return l
l1 = makeM(n,m)
l2 = makeM(m,n)
print("the first matrix is : " , l1)
print("the second matrix is : " , l2)


e = len(l1)
f = len(l1[0])
g = len(l2)
h = len(l2[0])

# def jam_matrix(l1,l2):
#     l3 = [[0 for i in range(n)] for j in range(m)]
#     for i in range(n):
#         for j in range(n):
#            l3[i][j] = l1[i][j] + l2[i][j]
#     return l3
# print("jam matrix ha is : ", jam_matrix(l1,l2))


# def taf_matrix(l1,l2):
#     l3 = [[0 for i in range(n)] for j in range(m)]
#     for i in range(n):
#         for j in range(n):
#            l3[i][j] = l1[i][j] - l2[i][j]
#     return l3
# print("tfriq matrix ha is : ", taf_matrix(l1,l2))


# def zarb_matrix3x3(l1,l2):
#     l3 = [[0,0,0],[0,0,0],[0,0,0]]
#     l3[0][0] = l1[0][0]*l2[0][0] + l1[0][1]*l2[1][0] + l1[0][2]*l2[2][0]
#     l3[0][1] = l1[0][0]*l2[0][1] + l1[0][1]*l2[1][1] + l1[0][2]*l2[2][1]
#     l3[0][2] = l1[0][0]*l2[0][2] + l1[0][1]*l2[1][2] + l1[0][2]*l2[2][2]

#     l3[1][0] = l1[1][0]*l2[0][0] + l1[1][1]*l2[1][0] + l1[1][2]*l2[2][0]
#     l3[1][1] = l1[1][0]*l2[0][1] + l1[1][1]*l2[1][1] + l1[1][2]*l2[2][1]
#     l3[1][2] = l1[1][0]*l2[0][2] + l1[1][1]*l2[1][2] + l1[1][2]*l2[2][2]

#     l3[2][0] = l1[2][0]*l2[0][0] + l1[2][1]*l2[1][0] + l1[2][2]*l2[2][0]
#     l3[2][1] = l1[2][0]*l2[0][1] + l1[2][1]*l2[1][1] + l1[2][2]*l2[2][1]
#     l3[2][2] = l1[2][0]*l2[0][2] + l1[2][1]*l2[1][2] + l1[2][2]*l2[2][2]
#     return l3
# print(zarb_matrix3x3(l1,l2))


if f == g :
        def zarb_matrix(l1,l2):
            l3 = [[0 for i in range(m)] for j in range(m)]
            for i in range(m):
                for j in range(m):
                    for k in range(n):
                        l3[i][j] += l1[i][k]*l2[k][j] 
            return l3
        print("zarb matrix ha is : ", zarb_matrix(l1,l2))
else :
    print("nope")




def zarb_matrix(l1,l2):
    l3 = [[0 for i in range(m)] for j in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(n):
                l3[i][j] += l1[i][k]*l2[k][j] 
    return l3
print("zarb matrix ha is : ", zarb_matrix(l1,l2))

# def taranahade_matrix(l):
#     l3 = [[0 for i in range(n)]for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             l3[i][j] = l[j][i]
#     return l3
# print("taranahade matrix is : ", taranahade_matrix(l1))