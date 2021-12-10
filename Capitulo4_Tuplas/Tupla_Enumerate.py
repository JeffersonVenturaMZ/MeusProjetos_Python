usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()
tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome"), input("Digite o nível")]    
for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])    
    
# Na primeira linha do código acima, estamos enumerando (função enumerate()) cada item encontrado na lista “e-mails” e gerando uma tupla com cada elemento (função: list()), formados pelo número e pelo e-mail. Em seguida, utilizamos um laço “for” atrelado ao tamanho da nossa tupla, ou seja, à quantidade de e-mails que foram armazenados.Se foram armazenados três e-mails, teremos que solicitar três nomes e três níveis e assim sucessivamente. Por isso, utilizamos a função range(), que controlará o laço “for” de zero até a quantidade de elementos encontrados na “tupla”