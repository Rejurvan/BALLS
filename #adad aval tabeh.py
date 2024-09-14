#adad aval tabeh
z = int(input())
y = int(input())
def adad_aval(a):
    f = True
    for i in range (2,a):
            if a % i == 0:
                f = False
    return f
for i in range(z , y+1):
    if i != 1:
        if adad_aval(i):
             print(i)

          