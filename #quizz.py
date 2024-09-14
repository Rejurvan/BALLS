#quizz
def adad_aval(a):
    flag = True
    for i in range (2,a):
        if a % i == 0:
            flag = False
    return flag
def tedad_aval(a):
    l = []
    for i in range(2,a):
        if adad_aval(i):
            l.append(i)
    return(len(l))
def aval(a):
    l = []
    for i in range(2,a):
        if adad_aval(i):
            l.append(i)
    return(l)
def tedad_maqsoom(a):
    l = []
    for i in aval(a):
        if a % i == 0:
            l.append(i)
    return(len(l))
n = int(input())
l = []
for i in range(n):
    n = int(input())
    if adad_aval(n):
        price1 = tedad_aval(n)
        l.append(price1)
    else :
        price2 = tedad_maqsoom(n)
        l.append(price2)
price = sum(l)
if adad_aval(price):
    takhfif = tedad_aval(price)
else :
    takhfif = tedad_maqsoom(price)
print(price - takhfif)
