#lista de cidades 
cidades = [
    "Brasília",
    "Rio de Janeiro",
    "São Paulo",
    "Goiânia",
    "Palmas",
    "São Luis",
    "Belém",
    "Fortaleza",
    "Salvador",
    "Porto Alegre",
    "Florianópolis",
    "Belo Horizonte"
    "Maceió",
    "Brasília",
    "Florianópolis",
    "Maceió",
    "Goiânia",
    "Brasília",
]   

# usúario faz a pesquisa
pesquisa = input("informe o nome da cidade a ser pesquisada: ").title().strip()
quantidade = cidades.count(pesquisa)

print(f"{pesquisa} foi encontrado {quantidade} vezes na lista!")
