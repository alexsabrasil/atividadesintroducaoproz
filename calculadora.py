import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1970 e 2023): "))
            if 1970 <= ano <= 2023:
                return ano
            else:
                print("Ano de nascimento inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"\nNome: {nome}")
    print(f"Idade: {idade} anos")

if __name__ == '__main__':
    main()

    