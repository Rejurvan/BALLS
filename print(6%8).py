def main():
    print("a",end = "")
    do1()
def do1():
    do3()
    print("B", end = "")
    do2()
def do2():
    print("B",end = "")
def do3():
    do2()
    print("D",end = "")
main()