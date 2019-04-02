import pickle
import os
import pathlib
#Picklexandria
#Modulo para salvar e carregar arquivos pickle dinamicamente sem gastar muita memoria
#Versao 1.0.1
#04/03/2019
def pos(name): #funcao para ordernar os arquivos de cada parte na hora de ler
    return int(name.split(".")[0])
def addpart(lista,foldername): #funcao para adicionar dados na tua estrutura em disco
    if foldername not in os.listdir(): #se nao existir a estrutura ainda, cria sua pasta
        pathlib.Path(foldername).mkdir(parents=True, exist_ok=True) #cria o diretorio com o nome definido
    os.chdir(foldername) #vai pra ela
    size = len(os.listdir()) #ve quantos arquivos ja existem
    idnum = "0"*(8-len(str(size)))+str(size) #calcula o id da parte
    filename = idnum+".iypt" #nome do arquivo da parte
    pickle.dump(lista,open(filename,"wb")) #deposita a parte
    os.chdir("..") #volta
def loadall(foldername): #carregar o arquivo inteiro
    os.chdir(foldername)#vai pra pasta
    files = sorted(os.listdir(),key=pos) #pega os arquivos e ordena por id
    os.chdir("..") #volta uma pasta
    files = [os.path.join(foldername,i) for i in files] #cria os caminhos de cada uma
    for arquivo in files: #abre cada parte
        openfile = open(arquivo,"rb")
        data = pickle.load(openfile)
        openfile.close()
        for item in data:
            yield item #manda o item daquela parte
            #para o usuario o efeito e de ler a lista inteira continuamente sem interrupcoes
        data = []