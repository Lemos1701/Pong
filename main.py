
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import game
import pygame
import time

#CHAMANDO A JANELA
menuJan = Window(600,600)
menuJan.set_title("Pong")
mouse = menuJan.get_mouse()

#SPRITES
playIA = Sprite("./Sprites./main/botao_1.png")
playSolo = Sprite("./Sprites./main/botao_1.png")
sair = Sprite("./Sprites./main/botao_1.png")
fundo = GameImage("./Sprites./main/fundo.png") 

#DEFINIR POSIÇÃO DOS BOTÕES
playSolo.x = menuJan.width/2 - playSolo.width/2
playSolo.y = menuJan.height/2 + playSolo.height/2

playIA.x = menuJan.width/2 - playIA.width/2
playIA.y = menuJan.height/2 + (2 * playIA.height)

sair.x = menuJan.width/2 - sair.width/2
sair.y = menuJan.height/2 + (3.5 * sair.height)

while(True):
    if mouse.is_over_area([playSolo.x, playSolo.y], [playSolo.x + playSolo.width, playSolo.y + playSolo.height]) and mouse.is_button_pressed(1):
        game.startGameSolo()
    
    if mouse.is_over_area([playIA.x, playIA.y], [playIA.x + playIA.width, playIA.y + playIA.height]) and mouse.is_button_pressed(1):
        game.startGameIA()

    if mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        menuJan.close()

    fundo.draw()
    playIA.draw()
    playSolo.draw()
    sair.draw()
    menuJan.update()