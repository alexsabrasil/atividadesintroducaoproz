quantidade_rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso_bruto = float(input("Digite o peso bruto do veículo (em kg): "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

if quantidade_rodas == 2 or quantidade_rodas == 3:
    print("Categoria de habilitação: A")
elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
    print("Categoria de habilitação: B")
elif quantidade_rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
    print("Categoria de habilitação: C")
elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
    print("Categoria de habilitação: D")
elif quantidade_rodas >= 4 and peso_bruto > 6000:
    print("Categoria de habilitação: E")
else:
    print("Não foi possível determinar a categoria de habilitação para o veículo.")
