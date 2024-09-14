#bmm va kmm
m, n = input().split()
m = int(m)
n = int(n)
if m == 1:
    bmm = 1
    kmm = n
elif n == 1:
    bmm = 1
    kmm = m
else:
    if m > n:
        bmm = n
    elif m < n:
        bmm = m
    while bmm > 1:
        if m % bmm == 0 and n % bmm == 0 :
            break
        else :
            bmm -= 1
            if m % bmm == 0 and n % bmm == 0 :
                break
# kmm = zarb adad ha taqsim bae bmm
kmm = m*n//bmm
print(bmm, kmm)