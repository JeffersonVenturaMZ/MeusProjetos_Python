from Funcoes.Funcoes_Arquivos import *
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
for linha in resultado:
        separacao=linha[linha.find(";")+1:-1]
        data=separacao[0:separacao.find(";")]
        separacao = separacao[separacao.find(";")+1:-1]
        descricao=separacao[0:separacao.find(";")]
        departamento=linha[linha.rfind(";")+1:-1]
        print("Data.........: ", data)
        print("Descrição....: ", descricao)
        print("Departamento.: ", departamento)
opcao = chamarMenu()
for linha in resultado:
        lista=linha.split(";")
        print("Data.........: ", lista[1])
        print("Descrição....: ", lista[2])
        print("Departamento.: ", lista[3])
opcao = chamarMenu()
# O método find(), também utilizado por Strings, permite que você encontre um caractere e/ou uma parte da string (conjunto de caracteres), retornando a posição da primeira incidência encontrada. Por exemplo: caso tenhamos a string “AmoPython” e executarmos um comando como: “AmoPython”.find(“o”), ele irá retornar o valor 2, pois a primeira vogal “o” se encontra na posição 2.
# O método find(), também utilizado por Strings, permite que você encontre um caractere e/ou uma parte da string (conjunto de caracteres), retornando a posição da primeira incidência encontrada. Por exemplo: caso tenhamos a string “AmoPython” e executarmos um comando como: “AmoPython”.find(“o”), ele irá retornar o valor 2, pois a primeira vogal “o” se encontra na posição 2.