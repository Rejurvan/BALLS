#  #charkh random
# import random
# a = float((input("put the chance that a will come out")))
# b = float((input("put the chance that b will come out"))) + a*1000000
# c = float((input("put the chance that c will come out"))) + b*1000000
# d = float((input("put the chance that d will come out"))) + c*1000000
# e = float((input("put the chance that e will come out"))) + d*1000000
# n = random.randint(0,1000000)
# if n == [0 , a*1000000]:
#     print("a came out")
# elif n in [a*1000000 , b*1000000]:
#     print("b came out")
# elif n in [b*1000000 , c*1000000]:
#     print("c came out")
# elif n in [c*1000000 , d*1000000]:
#     print("d came out")
# elif n in [d*1000000 , e*1000000]:
#     print("e came out")
  

# import random
# l = {}
# dict_chance = {}
# mojodi = "mojodi"
# while not(mojodi == 0):
#     name = str(input("put a name in here : "))
#     mojodi = int(input("put a mojodi in here : "))
#     l[name] = mojodi
#     s = 0
#     for key in l:
#         s += l[key]
#     dict_chance[name] = l[key]/s
# print(l)
# print(dict_chance)
# interval = {}
# end = 0
# r = random.randint(0,10000)
# for key in dict_chance:
#     interval[key] = (end , end+100*dict_chance[key])
#     end = end+100*dict_chance[key]
# for key in interval:
#     if r > interval[key][0] and r < interval[key][1]:
#         print(key)





# import random
# l = {}
# dict_chance = {}
# mojodi = "mojodi"
# while not(mojodi == 0):
#     name = str(input("put a name in here : "))
#     mojodi = int(input("put a mojodi in here : "))
#     l[name] = mojodi
#     s = 0
#     for key in l:
#         s += l[key]
#     dict_chance[name] = l[key]
# print(s)
# print(l)
# print(dict_chance)
# interval = {}
# end = 0
# r = random.randint(0,s*100)
# print(r)
# for key in dict_chance:
#     interval[key] = (end , end+100*dict_chance[key])
#     end = end+100*dict_chance[key]
# print(interval)
# for key in interval:
#         if r > interval[key][0] and r < interval[key][1]:
#             print(key)





# import random
# l = {}
# dict_chance = {}
# mojodi = "mojodi"
# while not(mojodi == 0):
#     name = str(input("put a name in here : "))
#     mojodi = int(input("put a mojodi in here : "))
#     l[name] = mojodi
#     s = 0
# interval = {}
# end = 0
# r = random.randint(0,s*100)
# for key in l:
#     interval[key] = (end , end+100*l[key])
#     end = end+100*l[key]
# for key in interval:
#         if r > interval[key][0] and r < interval[key][1]:
#             print(key)





import random
l = {}
dict_chance = {}
mojodi = "mojodi"
while not(mojodi == 0):
    name = str(input("put a name in here : "))
    mojodi = int(input("put a mojodi in here : "))
    l[name] = mojodi
    s = 0
    for key in l:
        s += l[key]
    dict_chance[name] = l[key]


interval = {}
end = 0
r = random.randint(0,s*100)
for key in dict_chance:
    interval[key] = (end , end+100*dict_chance[key])
    end = end+100*dict_chance[key]
for key in interval:
        if r > interval[key][0] and r < interval[key][1]:
            print(f"the winner is {key}")
            break
        elif r > interval[key][0] and r < interval[key][1]:
            print("AW sowwy we ran into a problem")