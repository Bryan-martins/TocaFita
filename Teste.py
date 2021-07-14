from Biblioteca_TocaFita import TocaFita

toca = TocaFita()

toca.player = "C:\Program Files (x86)\Windows Media Player\wmplayer.exe"

#toca.Tocar(r'C:\Users\Senketsv\Downloads\Protoman.mp4')

lista = [r'C:\Users\Senketsv\Downloads\Protoman.mp4', r'C:\Users\Senketsv\Downloads\Poze.mp4', 
r'C:\Users\Senketsv\Downloads\Protoman.mp4', r'C:\Users\Senketsv\Videos\Digimon.mp4']

toca.TocarLista(lista)

