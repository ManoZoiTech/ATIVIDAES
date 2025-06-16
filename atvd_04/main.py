# TODO  - Ativade
"""
Crie um programa em que o usuário pode escolher entre:
-inserir um nome em uma lista
-Exibir a lista de nomes
-Pesquisar por um nome na lista
-Sair do programa
"""
# NOTE - DIVIRTAM-SE!!! =D

carrinho = [""]

while True:
    print("\n=== Menu ===")
    print("1. Inserir um nome na lista")
    print("2. Exibir a lista de nomes")
    print("3. Pesquisar por nome na lista")
    print("4. Sair do programa")
    item = input ("informe o intem: ").capitalize().strip()
    carrinho.append(item)
    print(f"{item} inserido no carrinho com sucesso!")
    confirmar = input("Deseja inserir outro intem? (s/n)").lower().strip()
    match confirmar:
        case "S":
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            continue

opcao = input("Escolha uma opção (1-4): ").strip()

if opcao == "1":
    intem = input("informe o nome: ").capitalize().strip()
    carrinho.append(item)
    print(f"{item} inserido no carrinho com sucesso!")

elif opcao == "2":
    if carrinho:
        print("\nLista de nomes em ordem alfabética:")
        for nome in sorted(carrinho):
            print(f" - {nome}")

    else:
        print("A lista está vazia.")

elif opcao == "3":
    nome_busca = input("Digite o nome que deseja pesquisar: ").capitalize().strip()
    if nome_busca in carrinho:
        print(f"{nome_busca} está na lista.")
    else:
        print(f"{nome_busca} não foi encontrado na lista.")

elif opcao == "4":
    print("Saindo do programa. Até logo!")
    "break"

else:
    print("Opção inválida. Tente novamente.")
    




