#Al: abra e reproduza um arquivo MP3
#autor: Lucas Borguezam
#data:18032022

#Import
import pygame #utilizado em jogos (jogos tem musica)
#Inicio
# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('desafio21-music-giveon.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
#fim