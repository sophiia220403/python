
# forLoop()
anz = int(input("gimme number \n"))
for durchgang in range(1, anz + 1):
    print(f"{durchgang}: ", end='')

    for i in range(durchgang):
        print("*", end=" ")
    print()


"""
#forLoop()
anz = int(input("gimme number"))
#                [1, 2, 3, 4, 5]
for durchgang in range(1,anz + 1):
    print(f"{durchgang}: ", end='')
    # dg = 1: range(1) : [0]
    # dg = 2: range(2) : [0, 1]
    # dg = 3: range(3) : [0, 1, 2]
    
    for e in range(durchgang):
      print("*", end='')
    print()
"""