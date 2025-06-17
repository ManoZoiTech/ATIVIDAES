chaves = ('nome', 'Idade', 'E-mail', 'Profissão')
pessoas = [ # type: ignore
    {
            chaves[0]: "Mano Zoi",
            chaves[1]: 25,
            chaves[2]:"manozoi@gmail.",
            chaves[3]: "gerente"
    },
    {
            chaves[0]: "Mano Japa",
            chaves[1]: 23,
            chaves[2]:"manojapa@gmail.",
            chaves[3]: "fucionario"
    }
]
# inserindo novo dicionario
pessoa = {}

#inserindo dados no novo dicionario 

try:
    for chave in chaves:
        if chave == "Idade":
            pessoa[chave] = int(input("informe Idade:"))
        else:
            pessoa[chave] = input(f"Informe {chave}: ")
        pessoas.append(pessoa) # type: ignore  
        print(f"{pessoa.get(chaves[0])} inserida com sucesso.") # type:ignore
except Exception as e:
        print(f"Não foi possivel cadastrar nova pessoa. {e}.")
finally:
    for pessoa in pessoas: # type: ignore
        for chave in pessoa:
            print(f"{chave}: {pessoa.get(chave)}.") # type: ignore
        print(f"\n{'-'*40}\n")                                         