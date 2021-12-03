from Capitulo3_Funcoes import IdentificacaoDeFuncoes as Ident

minhaLista=[]
print("Preenchendo")
Ident.preencherInventario(minhaLista)
print("Exibindo")
Ident.exibirInventario(minhaLista)

print("Pesquisando")
Ident.localizarPorNome(minhaLista)
print("Alterando")
Ident.depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(Ident.excluirPorSerial(minhaLista))
Ident.exibirInventario(minhaLista)

print("Resumindo")
Ident.resumirValores(minhaLista)