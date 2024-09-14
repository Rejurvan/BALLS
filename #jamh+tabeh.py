#jamh+tabeh
# def math(a,b):
#     return a+b

# def multiply(a , b):
#     s = a
#     for i in range(1,b):
#         s = math(s,a)
#     return s
# print(multiply(4,2))

# def fib(n):
#     a = 1
#     b = 1
#     for i in range(3,n+1):
#         t = a
#         a = b
#         b = t + a
#     return b
    
# print(fib(5))

def printit(from_bar , to_bar):
    print(f"move top disc of {from_bar} to {to_bar}")
def tower(n,source,help,destination):
    if n == 1:
        printit(source,destination)
    else :
        tower(n-1,source,destination,help)
        printit(source,destination)
        tower(n-1,help,source,destination)

tower(20,"A","B","C")




