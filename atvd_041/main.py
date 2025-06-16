# importe biblioteca
import os

# lista
nomes = []

while True:
    print(f"{'-'*30} MENU {'-'*30}")
    print("1 - Inserir novo nome na lista")
    print("2 - Exibir lista")
    print("3 - Pesquisar nome na lista")
    print("4 - Sair do programa")

    opcao = input("Opção desejada: ").strip()

    os.system("cls")
    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser cadastrado: ").sy
            os.system("cls")   
