# declaração de lista
carrinho = [""]

while True:
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

# ordenar a lista em ordem afabética
carrinho.sort()

#exibe os intem da lista
for item in carrinho:
  print(item)
  