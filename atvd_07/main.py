# bibliotecas
import os

#lista
usuarios = []

# loop
while True:
    # menu
    print(f" {'_'*20} MENU pessoas {'_'*20}\n")
    print("1 - Inserir dados do novo usuário")
    print("2 - Exibir lista de usuário")
    print("3 - Alterar dados de um usuário já cadastrado")
    print("4 - Excluir usuário da lista")
    print("5 - Sair do programa")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            # inicializa o dicionário
            usuario = {}

            # input do usuario
            usuarios['Nome'] = input("Informe a nome: ").title().strip
            usuarios['data de nascimento'] = input("data de nascimento: ").strip
            usuarios['E-mail'] = input("Informe a E-mail: ").strip()
            usuarios['CPF'] = input("Informe a CPF: ").strip()
            usuarios['Telefone'] = input("Informe o Telefone: ")
            usuarios['Profissão'] = input("Profissão: ")
            usuarios['Gênero'] = input("Informe o Gênero: ")

            os.system("cls" if os.name == "nt" else "clear")
            try:
                # inserir os dados do dicionário na lista
                usuarios.append(usuario) # type:ignore
                print('Usuário cadastrado com sucesso!')
            except Exception as e:
                print(f"Não foi possivel inserir o novo valor. {e},")
            finally:
                continue
        case "2":
           print("\nLista de usuários:")
           for i in range(Len(usuarios)): # type: ignore
            print(f"{'_'*40}\n")
            print(f"Índice: {i}.")
            for chave in usuarios[i]: # type: ignore
                print(f"{chave.capitalize()}: {usuarios[i].get(chave)}.") # type: ignore
            continue
        case "3":
            try:
                i = int(input("Informe o índice desejado:"))
                if i >= 0 and i < Len(usuarios): # type: ignore
                    for chave in usuarios[i]: # Type:ignore
                        print(f"{chave.capitalize()}. {usuarios[i].get(chave)} ")# Type:ignore
                    chave_escolhida = input("Informe a chave que deseja alterar:" ).lower().strip()
                    usuarios[i][chave_escolhida] = input("Informe o novo valor: ").strip() 
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Chave alterada com sucesso.")
                else:
                    print("Indice inválido.")
            except Exception as e:
                print(f"Não foi possivel alterar os dados. {e}.")
            finally:
                continue
        case "4":
            try:
                i = int(input("Informe o índice:"))
                if i >= 0 and i < Len(usuarios): # type: ignore
                    for chave in usuarios[i]: # Type:ignore
                        print(f"{chave.capitalize()}. {usuarios[i].get(chave)} ")# Type:ignore
                    confirma = input("Tem certeza de que deseja exluir esse usuário? (s/n) ").lower().strip()
                    match confirma: # type: ignore
                        case "s":
                            del(usuarios[i])
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário deletado com sucesso.")
                        case "n":
                            os.system("cls" if os.name == "nt" else "clear")
                        case _:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("opção inválida. Operação cancelada.")
                else:
                    print("Indice inválido.")
            except Exception as e:
                print(f"Não foi possivel excluir usuário. {e}.")
            finally:
                continue
        case "5":
            print("Programa encerrado...")
            break
        case _:
            print("Opção Inválida.")