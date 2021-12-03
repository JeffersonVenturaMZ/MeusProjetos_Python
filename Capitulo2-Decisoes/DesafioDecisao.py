# O seu módulo solicitará o nível de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e o gênero dessa pessoa, 
# caso o nível seja ADM, ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres. 
# Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres. 
# Se o nível for GUEST, a mensagem deverá ser “Olá visitante”. E se o nível digitado for diferente de ADM, USR ou GUEST deverá exibir a mensagem “Olá desconhecido(a)”. 
# Considere apenas os gêneros masculino e feminino
nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
# cuidado com as tabulações, elas são decisivas em Python.    