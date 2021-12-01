nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))
# Função str() para converter o conteúdo da variável “float” para string.
# Vamos utilizar a função input(), assim como a função print() exibe. A função input() permitirá que o usuário final possa digitar um conteúdo em tempo de execução.
# Utilizaremos mais uma função, chamada type(). Esta função retorna o tipo do dado do que estiver dentro dos seus parênteses.