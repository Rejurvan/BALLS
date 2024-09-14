#last jalase

dictD = { 40213144341212 : {"debt" : 31 ,"credit" : 501},
         40213144341213 : {"debt" : 32 ,"credit" : 502},
         40213144341214 : {"debt" : 33 ,"credit" : 503}}
for i in range(1):
            k = int(input("shomare daneshjoii ha : "))
            f = int(input("debt ha : "))
            r = int(input("credit ha : "))
            dictD[k] = {"debt" : f , "credit" : r }
print(dictD)
n = int(input("shomare daneshjoii ro vared kon : "))
m = input("debt ro mikhaii ya credit : ")
print(dictD[40213144341212]["debt"])
def debt(n,m):
    dictD[n][m] = input("debt jadid to vared kon : ")
    return dictD[n]
def credit(n,m):
    dictD[n][m] = input("credit jadid to vared kon : ")
    return dictD[n]
if m == "debt" :
    print(debt(n,m))
elif m == "credit" :
    print(credit(n,m))
