# A forma de utilizar o comando “if”, ou seja, sua sintaxe, é bem simples:
# if <condição>:
#     <o que você quer que aconteça caso a condição seja verdadeira>
# Repare em dois detalhes importantes:
# A linha do if deve ser encerrada com dois pontos (:).
# A(s) linha(s) a ser executada(s), caso a condição seja verdadeira, deverá(ão) estar com um recuo da margem esquerda. 
# Este recuo deve ser realizado através da tecla <TAB>. Tudo que estiver recuado, abaixo do if, será executado somente se a condição for verdadeira.

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)