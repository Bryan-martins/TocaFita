from Biblioteca_TocaFita import TocaFita

#Comandos
toca = TocaFita()

toca.player = "C:\..."    #Diretório que contém o executavél do reprodutor.

toca.Tocar('Protoman.mp4') #Indique o nome do arquivo da música e sua extensão.

lista = [] #Uma lista contendo os diretórios das músicas

toca.TocarLista(lista) #Indique a lista para a função de playlist