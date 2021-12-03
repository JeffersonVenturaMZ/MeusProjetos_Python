#lista preenchida estaticamente
lista_estatica = ["xpto", True]

#lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]

#lista vazia
lista_vazia=[]

# Na “lista_dinamica”, o segundo item está passando por duas conversões. Isso ocorreu porque desejamos um dado do tipo “boolean”, ou seja, um dado booleano que pode possuir apenas os valores “True” ou “False”. Esse tipo de dado é utilizado normalmente para perguntas que possam ter como resposta somente os valores “sim” ou “não”, como é o caso do nosso exemplo, a pergunta “Está logado?” somente pode ter as respostas “sim” ou ”não”.Como o input retorna uma string, devemos converter o dado para int (inteiro), para, então, posteriormente, convertê-lo para bool (booleano). Não podemos fazer a conversão diretamente de string para bool. O valor retornado será “False” somente se o número informado for igual a zero, qualquer outro valor trará o retorno “True”.