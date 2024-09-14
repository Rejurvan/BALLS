#fithaghoreth
n = int(input("put a number here : "))
frag = True
for i in range(1,n):
    for j in range(i,n):
        c = n - i - j        
        if i**2 + j**2 == c**2 :
            print(str(i))
            print(str(j))
            print(str(c))
            frag = False
if frag:
    print("imposble")


# for a in range(1,n):
#     for b in range(a,n):
#         c = n - a - b
#         if a**2 + b**2 == c**2:
#             print(a,b,c)
    