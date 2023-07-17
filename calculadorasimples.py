numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

resultado = calculadora(numero1, numero2, operacao)
print("Resultado: ", resultado)

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Evita a divisão por zero
            return num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return 0

            def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Digite o número da operação desejada: "))

        if operacao == 0:
        print("Saindo...")
        break
    elif operacao < 1 or operacao > 4:
        print("Essa opção não existe.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == 1:
            resultado = num1 + num2
            print("Resultado: ", resultado)
        elif operacao == 2:
            resultado = num1 - num2
            print("Resultado: ", resultado)
        elif operacao == 3:
            resultado = num1 * num2
            print("Resultado: ", resultado)
        elif operacao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado: ", resultado)
            else:
                print("Erro: Divisão por zero!")
        print()