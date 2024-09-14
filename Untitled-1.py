name = "name"
l = {}
dict_chance = {}
s = 0
def dict_acc():
    global s
    global dict_chance
    mojodi = "mojodi"
    while not(mojodi == 0):
        name = str(input("put a name in here : "))
        mojodi = int(input("put a mojodi in here : "))
        l[name] = mojodi
        for key in l:
            s += l[key]
        dict_chance[name] = l[key]
    return dict_acc


def answer():
    import random
    interval = {}
    end = 0
    r = random.randint(0,2400)
    for key in dict_chance:
        interval[key] = (end , end+100*dict_chance[key])
        end = end+100*dict_chance[key]
    for key in interval:
            if r > interval[key][0] and r < interval[key][1]:
                print(f"the winner is {key}")
                break
            elif r > interval[key][0] and r < interval[key][1]:
                print("AW sowwy we ran into a problem")
    return answer
dict_acc()
print(answer())






# name = "name"
# l = {}
# def dict_acc():
#     dict_chance = {}
#     mojodi = "mojodi"
#     while not(mojodi == 0):
#         name = str(input("put a name in here : "))
#         mojodi = int(input("put a mojodi in here : "))
#         l[name] = mojodi
#         s = 0
#         for key in l:
#             s += l[key]
#         dict_chance[name] = l[key]
#     return dict_acc


# def answer():
#     global dict_acc
#     global s
#     global dict_chance
#     import random
#     interval = {}
#     end = 0
#     ra = 10000
#     r = random.randint(0,1000)
#     for key in dict_chance:
#         interval[key] = (end , end+100*dict_chance[key])
#         end = end+100*dict_chance[key]
#     for key in interval:
#             if r > interval[key][0] and r < interval[key][1]:
#                 print(f"the winner is {key}")
#                 break
#             elif r > interval[key][0] and r < interval[key][1]:
#                 print("AW sowwy we ran into a problem")
#     return answer
# dict_acc()
# answer()