import random
number_2 = 0
number_1 = 0
for i in range(1000000):
    r = random.randint(0,1000000)
    x = 2 + (r*(6/1000000))
    fx = 9-(x-5)**2
    y = r*10/1000000
    if y < fx :
        number_2 += 1
    else :
        number_1 += 1


u = (number_1/number_2) *60

print(u)
