# ITEMS() Responsável por retornar em forma de lista os elementos do dicionário. Para isso, ele fará uso do recurso de tuplas, que será apresentado no tópico seguinte. Basicamente, cada tupla terá uma chave e um dado, conforme podemos perceber no exemplo abaixo. Considerando nosso exemplo, poderíamos ter este método retornando os dados da seguinte forma:[(“ologin”,[“nome”,”data”,”estacao”]),(“login2”,[“nome2”, “data2”,”est2”])]

# VALUES() Podemos retornar também somente os dados, descartando as chaves, ou seja, esse método retorna uma lista formada apenas pelos dados. Se pegarmos como exemplo o nosso caso do histórico dos usuários, teremos uma lista dentro de outra lista, e o exemplo ficaria como o que está apresentado abaixo:[ [“nome”,”data”,”estacao”],[“nome2”, “data2”,”est2”]]

# KEYS() Claro que se retornarmos somente os dados, podemos retornar também somente as chaves. E é isto o que este método faz, retornando todas as chaves do dicionário em forma de lista, conforme apresentado na linha abaixo:[“ologin”, “login2”]

# HAS_KEY() Este método permitirá que você tenha a resposta se a chave existe ou não dentro do dicionário, ele irá retornar True (1) ou False (0).

# CLEAR() Esvazia completamente o dicionário.

# POPITEM() Este é um método próprio para quem deseja montar algum dicionário que contenha elementos que serão executados, de maneira aleatória, individualmente e, na sequência, deverão ser eliminados do dicionário. Poderíamos pensar em um dicionário com dicas, e à medida que cada dica fosse exibida, automaticamente ela deveria ser retirada do dicionário.