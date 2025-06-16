# dicionario
usuario = {
        'nome': "Mano zoi",
        'Idade': "25",
        'Peso': "1,75",
        'profissão': "programador"
}
# usuario escolhe a chave que deseja alterar
chave = input("Informe o nome da chave que deseja alterar:").lower().strip()

# tratamento de exeção
try:
    if chave in usuario:
        usuario[chave] = input("Informe o nome valor: ").strip()
        print(F"chave {chave} alterada com sucesso!")
    else:
        print("Não foi posssivel encontrar a chave requisitada.")
except Exception as e:
    print(F"Não foi possivel alterar. {e}.")
finally:
    #exibe os novo valores no dicionario
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}.")