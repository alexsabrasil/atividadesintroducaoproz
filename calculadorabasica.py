def calculadora (num1, num2, entrada):
    if entrada == 1:
       return num1 + num2
    elif entrada == 2:
        return num1 - num2
    elif entrada == 3:
        return num1 * num2
    elif entrada == 4:
        return num1 / num2
    else:
        return 0

num1 = int (input ("digite o primeiro número"))
num2 = int (input ("digite o segundo número"))
num3 = int (input ("Digite a operação, sendo 1 soma, 2 subtração, 3 multiplicação e 4 divisão"))

valor = calculadora (num1, num2, num3)

print ("O resultado é: " ,valor)