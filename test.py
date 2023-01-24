n = int(input("Enter the Number: "))
sym = input("Enter the symbol: ")

for i in range(n):
    print(sym, end="")
print()
for i in range(n):
    print(sym)

x = 4
y = 5

def myfunc(x , y):
    return x + y

k = myfunc(x , y)
print(k)

def myfunc2(x,y):
    return x+y-2

k = myfunc2(x,y)
print(k)