import pygame
import Colors


cor = Colors.cores()

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
        volume = str(input('[1] - Alto\n[2] - Medio\n[3] - Baixo\n> '))
        if volume.isnumeric():
            numero = int(volume)
            if 0 < numero < 4:
                if numero == 1:
                    return 0.7
                if numero == 2:
                    return 0.5
                if numero == 3:
                    return 0.3
            else:
                print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')
        else:
            print(f'{cor["fundo_preto"]}{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')


def set_music(num,volume):

    music = {'1':"music_1.mp3",'2':"music_2.mp3",'3':"music_3.mp3",'4':"music_4.mp3"}
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




