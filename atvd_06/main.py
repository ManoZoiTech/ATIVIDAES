import os
usuario = {}
    

while True:
    print(f" {'_'*20} MENU USUÁRIO {'_'*20}/20")
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
            usuario[chave] = input("Informe o valor da chave: ")
               
            os.system("cls")
            print('Chave cadastrada com sucesso!')

            continue
        case "2":
           for chave in usuario: # type: ignore
            print(f"{chave.capitalize()}: {usuario.get(chave)}") # type: ignore
            print("\n")
            continue
              
        case "3":
            chave = input("Informe o nome da chave que deseja alterar: ").lower().strip()

            if chave in usuario:
                usuario[chave] = input(f"Informe o valor da chave: ").strip()
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
                del usuario[chave]
                print(f"Chave excluida com sucesso!")
            else:
                print("chave não foi exluida.")
            continue
        case "5":
            print("Programa encerrado...")
            break
        case _:
             print("Oção invalida.Tente novamente.")
   









"""
# todo - atividade: Crie um programa com um dicionario chamado 'usuario',
com o seguinte menu:
- Cadastrar nova chave
-Exibir dados do usuario
-Aletar valor da chave
-Excluir chave
-Sair do programa
# NOTE - os dados a serem inseridos precisam ter a ver com os dados de usuario
"""


