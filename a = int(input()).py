c = int(input())
b = int(input())
def adad_aval(a):
    f = True
    for i in range (1,a):
            if a % i == 0:
                f = False
    return f
for i in range(c , b):
     if adad_aval(i):
          print(i)
            
    
