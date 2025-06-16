# importe biblioteca
import os

# lista
nomes = [
    "Maria",
    "Ana",
    "Júlia",
    "Clara",
    "Laura",
    "Sofia",
    "Helena",
    "Isabela",
    "Luísa",
    "Beatriz"
] 

# exibe a lista original
for i in range(len(nomes)):
    print(f"Índice (i) {nomes[i]}.")

# usuário informa a posição da lista que deseja excluir
try:
    i = int(input("informe o Índice que deseja excluir: "))
    os.system("cls")
    if i >= 0 and 1 < len(nomes):
        print(f"Intem a ser excluído: {nomes[i]}")
        confirma = input(f"Deseja excluir {nomes[i]}? (s/n)").lower().strip
        os.system("cls")
        match confirma:
            case "s":
                intem_excluido = nomes[i]
                del(nomes[i]) 
                print(f"Intem {intem_excluido} excluido com sucesso.")
            case "n":
                print(f"{nomes[i]} não será excluído.")
            case _:
                print("Opção inválida")
    else:
        print("Índice inválido.")
except Exception as e:
 print(f"Não foi possivel excluir item. {e}.")