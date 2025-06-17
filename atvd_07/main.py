# dicionario
pessoa = {}

# inserindo a dados da pessoa
try:
    pessoa['Nome'] = (input("Informe a nome: "))
    pessoa['idade'] = int(input("Informe a idade: "))
    pessoa['E-mail'] = (input("Informe a E-mail: "))
    pessoa['CPF'] = int(input("Informe a CPF: "))
    pessoa['Data de Nascimento'] = int(input("Informe a Data de Nascimento: "))
    pessoa['Gênero'] = (input("Informe o Gênero: "))
    pessoa['Telefone'] = int(input("Informe o Telefone: "))

except Exception as e:
    print(f"Não foi possivel inserir o novo valor. {e},")
finally:
    print(f"Nome: {pessoa.get('nome')}")
    print(f"Idade: {pessoa.get('Idade')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"CPF: {pessoa.get('CPF')}")
    print(f"Data de Nascimento: {pessoa.get('Data de Nascimento')}")
    print(f"Gênero: {pessoa.get('Gênero')}")
    print(f"Telefone: {pessoa.get('Telefone')}")

while True:
    print(f" {'_'*20} MENU pessoas {'_'*20}/20")
    print("1 - Cadastrar nova chave")
    print("2 - Exibir dados do usuário")
    print("3 - Alterar valor de uma chave")
    print("4 - Excluir uma chave")
    print("5 - Sair do programa")
    opcao = input('Escolha uma opção (1-5):').strip ()
    os.system("cls")
    match opcao:
        case "1":
            chave = input("Informe o nome da chave que deseja inserir: ").lower().strip()
            pessoa[chave] = input("Informe o valor da chave: ")
               
            os.system("cls")
            print('Chave cadastrada com sucesso!')

            continue
        case "2":
           for chave in pesssoa: # type: ignore
            print(f"{chave.capitalize()}: {pesssoa.get(chave)}") # type: ignore
            print("\n")
            continue
              
        case "3":
            chave = input("Informe o nome da chave que deseja alterar: ").lower().strip()

            if chave in pessoa:
                pessoa[chave] = input(f"Informe o valor da chave: ").strip()
                os.system("cls")
                print("Valor da chave alterado com sucesso!")
            else:
                os.system("cls")
                print("Chave não encontrada.")
            continue

        case "4":
            chave = input("Informe o nome da chave que deseja deletar: ").strip().lower()
            confirmacao = input(f"Tem certeza de que deseja excluir {chave}?(s/n)").lower().strip()
            os.system("cls")
    
            if confirmacao is "s":
                del pessoa[chave]
                print(f"Chave excluida com sucesso!")
            else:
                print("chave não foi exluida.")
            continue
        case "5":
            print("Programa encerrado...")
            break