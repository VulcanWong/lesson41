n = input('enter the number:')
a = 0
b= 1
count = 1
while count <= int(n):
    print(b, end=' ')
    count +=1
    a,b = b, a+b
print()