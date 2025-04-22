num1 = 10
num2 = 0
num3 = 0

if num1>=num2 and num2>=num3:  
    print("Numero 1 e o maior,Numero 2 e do meio,Numero 3 e o menor")
elif num1>=num3 and num3>=num2:
    print("Numero 1 e o maior,Numero 3 e o do meio,Numero 2 e o menor")
elif num3>=num2 and num2>=num1:
    print("Numero 3 e o maior,Numero 2 e o do meio,Numero 1 e o menor")
elif num3>=num1 and num1>=num2:
    print("Numero 3 e o maior,Numero 1 e o do meio,Numero 2 e o menor")
elif num2>=num1 and num1>=num3:
    print("Numero 2 e o maior,Numero 1 e o do meio,Numero 3 e o menor")
elif num2>=num3 and num3>=num1:
    print("Numero 2 e o maior,Numero 3 e o do meio,Numero 1 e o menor")
else:
    print("Tem 2 numeros iguais")
