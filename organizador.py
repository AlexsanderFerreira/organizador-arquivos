import os

# Aqui você pode colocar o caminho para a pasta que estão os arquivos que deseja organizar
os.chdir(r"C:\Users\seu.usuario\Downloads") 

# Aqui criamos uma lista para separar os arquivos de pastas e uma lista dos tipos de extensões
lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)]
# Usado o .split(".")[-1] para separar o nome do arquivo da extensão e também pegar o valor de trás pra frente da lista.
lista_tipos = {tipo.split(".")[-1] for tipo in lista_arquivos}  

# Aqui estamos validando se já existe a pasta daquele tipo, então não cria uma nova, mas caso nao exista ai sim é criado.
for tipo in lista_tipos:
    if os.path.exists(tipo):
        pass
    else:
        os.mkdir(tipo)

# Aqui é onde transferimos o arquivo para a pasta respectiva da sua extensão.
for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1]
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.replace(de, para)