import os
import subprocess 

class TocaFita:
    def __init__(self):
        self.dir = ''
    
    def Tocar(self, Music, Player):
        try:
            dirr = self.dir+'\\'
            #r'C:\Users\Senketsv\Downloads\Protoman.mp4'
            subprocess.run([Player, dirr + Music])

        except:
            print('Erro ao tocar a musica!')
            print('Recomenda-se abrir arquivos de áudio e vídeo por reprodutores como o VLC Media Player')
            print('Link para Download: https://www.videolan.org')
    
    def TocarLista(self, lista, Player):
        try:
            dirr = self.dir+'\\'
            #r'C:\Users\Senketsv\Downloads\Protoman.mp4'
            tam = len(lista)
            
            #subprocess.run([Player, dirr + Music])
        
        except:
            print('Erro ao tocar a musica!')
            print('Recomenda-se abrir arquivos de áudio e vídeo por reprodutores como o VLC Media Player')
            print('Link para Download: https://www.videolan.org')