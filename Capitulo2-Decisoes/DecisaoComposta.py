nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# função chamada “upper()”. Esta função tem a finalidade de converter o conteúdo de uma string para letras maiúsculas, ou seja, o que for digitado no “input()”    
# comando chamado “elif:”, que é uma sigla para “else”+”if”, ou seja, existe uma segunda condição que deve ser também avaliada. Podemos acrescentar quantos “elifs” forem necessários.