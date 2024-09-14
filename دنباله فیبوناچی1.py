# so lets try to write this down
# ...
# ...
# ...
# I couldn't do it
# lets try somthing else



# # # a = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229]
# # # n = int(input("put a number here : "))
# # # print(a[n-1])



#fibunacci
# # # # # now for my last try
# # # # k = int(input("put a nimber here : "))
# # # # a = 0
# # # # b = 1
# # # # if k < 0 :
# # # #     print("mano maskhare mikoni?")
# # # # elif k < 2 :
# # # #     print(1)    
# # # # for x in range(1,(k)):
# # # #     c = a + b
# # # #     a  =  b
# # # #     b  =  c
# # # # print(c)



# dor gardoon  gar do roozi bar moraad ma naraft
# daeman yeksan nabashad haal doraan gham makhor


# alright now lets try for real

          
           
# # # # # alright I suppose I did it
# # # # a=[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 111 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20] 
# # # # for i in range(20):
# # # #     for j in range(i,20):
# # # #         if a[i] > a[j]:
# # # #             a[i], a[j] = a[j],a[i]   
# # # # print(a)

  


# # # # import random
# # # # inp = int(input("put a number here : "))
# # # # a = []
# # # # for l in range(inp):
# # # #     a.append(random.randint(10,10000))
# # # # print(a)    
# # # # for j in range(len(a)):
# # # #     for i in range(j,len(a)):
# # # #         if a[i] < a[j] :
# # # #             a[i], a[j] = a[j],a[i]
# # # # print(a)  


# # # # import random
# # # # inp = int(input("put a number here : "))
# # # # a = []
# # # # for i in range(inp):
# # # #     a.append(random.randint(10,100000))
# # # # print(a)    
# # # # for j in range(len(a)):
# # # #     min = a[j]
# # # #     min_index = j
# # # #     for i in range(j, len(a)):
# # # #         if a[i] < min :
# # # #             min = a[i]
# # # #             min_index = i
# # # #     temp = min
# # # #     a[min_index] = a[j]
# # # #     a[j] = temp
# # # # print(a)  





# # # # n = int(input("put your number here : "))
# # # # c = 1
# # # # while not(n//10 == 0):
# # # #     n = n//10
# # # #     c += 1
# # # # print(c)



# # # # for i in range(1,100):
# # # #     import random
# # # #     a = random.randint(5000,50000000)
# # # #     if a % 2 == 0 :
# # # #         print(str(a) + " is even")
# # # #         c = 1
# # # #         while not(a//10 == 0) :
# # # #             a = a//10
# # # #             c += 1 
# # # #         print("and has " + str(c) + " digits")
# # # #     else :
# # # #         print(str(a) + " is odd")   



# # # # import random
# # # # n = int(input("put a number here : "))
# # # # l = []
# # # # for i in range(n):
# # # #      l.append(random.randint(1000,5000))
# # # # print(l)
# # # # for i in range(n):
# # # #      temp = l[i]
# # # #      for j in range(1,i+1):
# # # #         if l[i-j] >  temp :
# # # #           l[i-j+1] = l[i-j]
# # # #         else :
# # # #             l[i-j+1] = temp
# # # #             break
# # # #         if j == i:
# # # #             l[0] = temp
# # # # print(l)
   
    

# # # # n = int(input("put a number here : "))
# # # # if n == 1 :
# # # #     print("aval nist")
    
# # # # elif n == 2 :
# # # #     print("aval ast")
# # # # flag = True
# # # # for i in range(2,n):
# # # #     if n % i == 0:
# # # #         print("aval nist")
# # # #         flag = False
# # # #         break
# # # # print(flag)






# # # # import random
# # # # n = int(input("put a number here : "))
# # # # l = []
# # # # for i in range(n):
# # # #     l.append(random.randint(100,1000))
# # # # print(l)
# # # # for i in range(n):
# # # #     temp = l[i]
# # # #     for j in range(i-1 , -1 , -1):
# # # #         if l[j] > temp :
# # # #             l[j+1] = l[j]
# # # #         else :
# # # #             l[j+1] = temp
# # # #             break
# # # #         if j == 0:
# # # #             l[0] = temp
# # # # print(l)
# # # # key = int(input("put the number you are searching for : "))
# # # # left = 0
# # # # right = n-1
# # # # index = None
# # # # while left <= right :
# # # #     m = (right+left)//2
# # # #     if l[m] == key :
# # # #         index = m
# # # #         break 
# # # #     elif l[m] > key :
# # # #         right = m-1
# # # #     else :
# # # #         left = m+1
# # # # print(f"{key} and  is in index {index}")



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
    

# # # def sequentioal_search(l,key):
# # #     for i in range(len(l)):
# # #         if l[i] == key:
# # #             return i
# # #     return None

# # # # import time
# # # # t1 = time.time()
# # # # for i in range(10):
# # # #     key = random.randint(100,1000)
# # # #     binary_search(l,key)
# # # # t2 = time.time() 
# # # # print("elapsed time : \t ", t2 - t1 )
# # # # t_seq = t2 - t1

# # # # import time
# # # # t1 = time.time()
# # # # for i in range(10):
# # # #     key = random.randint(100,1000)
# # # #     sequentioal_search(l,key)
# # # # t2 = time.time()
# # # # print("elapsed time : \t ", t2 - t1 )
# # # # t_bin = t2 - t1

# # # print(f"taqsume time ha mishe{t_bin/t_seq}")






# # # # import random
# # # # dict_chance = {
# # # #      'reza1' : 9000000,
# # # #      'reza2' : 1000000,
# # # #      'reza3' : 1000000,
# # # #      'reza4' : 10000,
     
# # # # }
# # # # mojodi = "mojodi"
# # # # while not(mojodi == 0):
# # # #     name = str(input("put a name in here : "))
# # # #     mojodi = int(input("put a mojodi in here : "))
# # # #     l[name] = mojodi
# # # #     s = 0
# # # #     for key in l:
# # # #         s += l[key]
# # # #     dict_chance[name] = l[key]
# # # # interval = {}
# # # # end = 0

# # # # r = random.randint(0,11010000)
# # # # for key in dict_chance:
# # # #     interval[key] = (end , end+100*dict_chance[key])
# # # #     end = end+100*dict_chance[key]
# # # # for key in interval:
# # # #         if r > interval[key][0] and r < interval[key][1]:
# # # #             print(f"the winner is {key}")




# # # # # # #slicing
# # # # # # import random
# # # # # # l = [random.randint(1,1000) for i in range(10)]
# # # # # # print(l)
# # # # # # print(l[3:6])
# # # # # # l1 = [random.randint(1,1000) for i in range(4)]
# # # # # # print(l1)
# # # # # # # l.extend(l1)
# # # # # # # l.extend(l1[1:])
# # # # # # # l.extend(l1[:1])
# # # # # # print(l)
# # # # # # l2 = l[5:8].extend(l1)
# # # # # # print(l2)



# # # # # # import random
# # # # # # list = [7,4,90,45,76,88]
# # # # # # while not(list == sorted(list)):
# # # # # #     random.shuffle(list)
# # # # # # print(list)

while True:
    print("and you dont seem to undrestand")