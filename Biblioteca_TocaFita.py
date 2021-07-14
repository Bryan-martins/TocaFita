import os
import subprocess 

class TocaFita:
    def __init__(self):
        self.player = ''        #Player padrão que o usuário irá utilizar.
    
    def Tocar(self, Music):
        try:
            subprocess.run([self.player, Music])        #Chamada de subprocesso, que abre o reprodutor e toca uma música.

        except:
            print('Erro ao tocar a musica!')    #Tratamento de erro.
            print('Recomenda-se abrir arquivos de áudio e vídeo por reprodutores como o VLC Media Player')
            print('Link para Download: https://www.videolan.org')
    
    def TocarLista(self, lista):
        try:
            lista.insert(0, self.player) #Recebe uma lista de nomes de música, contidos no diretório. A primeira posição da lista é adicionada o reprodutor que irá toca-lás. (self.player)
            subprocess.run(lista)        #Chamada de subprocesso, que abre o reprodutor e toca a playlist.
        
        except:
            print('Erro ao tocar a musica!') #Tratamento de erro.
            print('Recomenda-se abrir arquivos de áudio e vídeo por reprodutores como o VLC Media Player')
            print('Link para Download: https://www.videolan.org')