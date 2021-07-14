from TrabalhoFinalPOO import TocaFita
import subprocess
toca = TocaFita()

toca.dir = r'C:\Users\Senketsv\Downloads'

#toca.Tocar('Protoman.mp4', "C:\Program Files (x86)\Windows Media Player\wmplayer.exe")

#lista = [r'C:\Users\Senketsv\Downloads\Protoman.mp4', r'C:\Users\Senketsv\Downloads\Poze.mp4']
#lista = [r'C:\Users\Val\Desktop\Musicas\Konai-Brown-Cidade-Lunar.mp3', r'C:\Users\Val\Desktop\Musicas\Hozier-Take-Me-To-Church.mp3']
lista = open('playlist.txt')
toca.TocarLista(lista)

#subprocess.call(["C:\Program Files (x86)\Windows Media Player\wmplayer.exe", "-nodisp", "-autoexit", r"C:\Users\Senketsv\Downloads\Protoman.mp4"])
#subprocess . run ( ["C:\Program Files (x86)\Windows Media Player\wmplayer.exe", r"C:\Users\Senketsv\Downloads\Protoman.mp4", r"C:\Users\Senketsv\Downloads\Poze.mp4"])
#player = subprocess . run ( ["C:\Program Files (x86)\Windows Media Player\wmplayer.exe", r"C:\Users\Senketsv\Downloads\Poze.mp4" ] )

#subprocess.call(['C:\Program Files (x86)\Windows Media Player\wmplayer.exe',"-nodisp","-autoexit", r'C:\Users\Val\Desktop\Musicas\Hozier-Take-Me-To-Church.mp3'])
#subprocess . run ( [r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe', r'C:\Users\Val\Desktop\Musicas\Hozier-Take-Me-To-Church.mp3',r'C:\Users\Val\Desktop\Musicas\Konai-Brown-Cidade-Lunar.mp3'])

#player = subprocess . run ( ["C:\Program Files (x86)\Windows Media Player\wmplayer.exe",lista[0]])
for i in lista:
    musica = i.split()
    for j in range(0,2):
        subprocess.call(['C:\Program Files (x86)\Windows Media Player\wmplayer.exe',"-nodisp","-autoexit", musica[j]])
        subprocess.run(musica[j])
        #player = subprocess.run(["C:\Program Files (x86)\Windows Media Player\wmplayer.exe",musica[i]])
lista.close()