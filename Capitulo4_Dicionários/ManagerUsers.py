import Funcoes.Funcoes_Dicionarios as fun

usuarios = {}
opcao = fun.perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        fun.inserir(usuarios)
    opcao = fun.perguntar()
    if opcao=="P":
        fun.pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        fun.excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        fun.listar(usuarios)
    opcao = fun.perguntar()
    