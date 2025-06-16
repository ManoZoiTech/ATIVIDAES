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
    pessoa['Endereço'] = (input("Informe o Endereço: "))
    pessoa['Altura em metros'] = float(input("Informe a Altura em metros: "))
    pessoa['Peso em kg'] = float(input("Informe Peso em kg: "))
    pessoa['Tipo Sanguíneo'] = (input("Informe Tipo Sanguíneo: "))

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
    print(f"Endereço: {pessoa.get('Endereço')}")
    print(f"Altura em metros: {pessoa.get('Altura em metros')}")
    print(f"Tipo Sanguíneo: {pessoa.get('Tipo Sanguíneo')}")
    
#exibe os dados do dicionário
for dado in pessoa:
    print(f"{dado.capitalize()}: {pessoa.get(dado)}")       
    print(f"Nome: {pessoa['nome']}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"E-mail: {pessoa.get('email')}")
