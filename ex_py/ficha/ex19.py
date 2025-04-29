a = 1
b = 1

print("serie de Fibonacci :")
print(a, b, end=' ')

for _ in range(58): 
    c = a + b
    print(c, end=' ')
    a = b
    b = c
