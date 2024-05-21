import pygame
import cores


cor = cores.cores()

def escolher_musica():

    while True:
        print(f'{cor["fundo_preto"]}{cor["amarelo"]}Escolha uma musica: {cor["limpa"]}')
        musica = str(input(f'{cor["fundo_preto"]}{cor["amarelo"]}[1]\n[2]\n[3]\n[4]\n> {cor["limpa"]}'))
        if musica.isnumeric():
            numero = int(musica)
            if 0 < numero < 5:
                return musica
            else:
                print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')
        else:
            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')


def set_volum():

    while True:
        print(f'{cor["fundo_preto"]}{cor["amarelo"]}Volume: ')
        volume = str(input('[1] - Alto\n[2] - Medio\n[3] - Baixo\n[4] - Parar musica\n> '))
        if volume.isnumeric():
            numero = int(volume)
            if 0 < numero < 5:
                if numero == 1:
                    return 0.7
                if numero == 2:
                    return 0.5
                if numero == 3:
                    return 0.3
                if numero == 4:
                    return 0
            else:
                print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')
        else:
            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')


def set_music(num,volume):

    music = {'1':"Patch3.0/Music/music_1.mp3",'2':"Patch3.0/MusicMusic/music_2.mp3",'3':"Patch3.0/MusicMusic/music_3.mp3",
             '4':"Patch3.0/Music/music_4.mp3"}
    music_choice = ' '
    for number in music.keys():
        if num in number:
            music_choice = music[number]

    pygame.mixer.init()
    pygame.mixer_music.load(music_choice)
    pygame.mixer_music.set_volume(volume)
    pygame.mixer_music.play()


def musica():
    musica = escolher_musica()
    volume = set_volum()
    set_music(musica,volume)




