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

    def verificar_categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas):
    if quantidade_rodas < 4:
        return 'Categoria A'
    elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
        return 'Categoria B'
    elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
        return 'Categoria D'
    elif quantidade_rodas >= 4 and peso_bruto > 6000:
        return 'Categoria E'
    elif quantidade_rodas >= 4 and 3500 < peso_bruto <= 6000:
        return 'Categoria C'
    else:
        return 'Categoria não determinada'

        