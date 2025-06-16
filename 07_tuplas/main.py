# tupla 
estados= (
        "Distrito Federal",
        "Goiás",
        "Minas Gerais",
        "Tocantins",
        "Rio de Janeiro",
        "Ceará"
)

# listar a tupla
for estado in estados:
    print(estados)

# pesquisar estados
estado_pesquisado = input("informa um estado que deseja pesquisar: ").title().strip()
qtde_estados = estados.count(estados_pesquisados)

print(f"{estados_pesquisa} foi encontrado {qtde_estados} vezes na tupla.")

# tentando organizar a tupla em ordem alfabética
try:
    estados.sort()
    for estado in estados:
        print(estados)
except Exception as e:
    print(f"Não foi possivel ordena a tupla. {e}.")

