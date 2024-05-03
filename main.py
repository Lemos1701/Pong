
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import game
import pygame
import time

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
timer = time.time()

#CHAMANDO A JANELA
menuJan = Window(600,600)
menuJan.set_title("Pong")
mouse = menuJan.get_mouse()

#SPRITES
playIA = Sprite("./Sprites./main/vsBot.png")
playSolo = Sprite("./Sprites./main/vsPlayer.png")
sair = Sprite("./Sprites./main/sair.png")
fundo = GameImage("./Sprites./main/fundo.png")
titulo = Sprite("./Sprites./main/titulo.png")

#SONS
click = pygame.mixer.Sound("./sons./main/click.mp3")
click.set_volume(0.5)
fundoM = pygame.mixer.Sound("./sons./main/fundo.mp3")
fundoM.set_volume(0.05)
fundoM.play(-1)

#DEFINIR POSIÇÃO DOS BOTÕES
titulo.x = menuJan.width/2 - titulo.width/2
titulo.y = menuJan.height/2 - (1.5 * titulo.height)

playSolo.x = menuJan.width/2 - playSolo.width/2
playSolo.y = menuJan.height/2 + playSolo.height/2

playIA.x = menuJan.width/2 - playIA.width/2
playIA.y = playSolo.y + (1.5 * playIA.height)

sair.x = menuJan.width/2 - sair.width/2
sair.y = playIA.y + (1.5 * sair.height)

while(True):
    if mouse.is_over_area([playSolo.x, playSolo.y], [playSolo.x + playSolo.width, playSolo.y + playSolo.height]) and mouse.is_button_pressed(1):
        click.play()
        timePass= time.time() - timer
        if timePass >=0.1:
            game.startGameSolo()
    
    if mouse.is_over_area([playIA.x, playIA.y], [playIA.x + playIA.width, playIA.y + playIA.height]) and mouse.is_button_pressed(1):
        click.play()
        timePass= time.time() - timer
        if timePass >=0.1:
            game.startGameIA()

    if mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        menuJan.close()

    fundo.draw()

    playIA.draw()
    playSolo.draw()
    sair.draw()
    titulo.draw()
    menuJan.update()