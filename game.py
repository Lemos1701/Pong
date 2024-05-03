from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import pygame
import time

def startGameIA():
    clock = pygame.time.Clock()
    timer = time.time()
    #CRIANDO VARIÁVEIS NECESSÁRIAS
    iD = 0
    iE = 0
    jan = Window(600, 600)
    ball = Sprite("./Sprites./game/p503.png")
    BarraE = Sprite("./Sprites./game/barraE.png")
    BarraD = Sprite("./Sprites./game/barraD.png")
    fundo = GameImage("./Sprites./main/fundo.png") 
    teclado = Window.get_keyboard()

    #DEFININDO VELOCIDADES
    velx = 220
    vely = 205
    velBOT = 155
    velBarraE = 250
    
    #SONS
    bolaBate = pygame.mixer.Sound("./sons./menu/colide.mp3")
    bolaBate.set_volume(0.15)

    #DEFININDO POSIÇÕES
    BXe = BarraE.width
    BYe = jan.height/2 - BarraE.height/2

    BXd = jan.width - (2*BarraD.width)
    BYd = jan.height/2 - BarraE.height/2

    px = jan.width/2 - ball.width/2
    py = jan.height/2 - ball.height/2

    jan.set_title("Pong by LeMoS")
    ball.set_position(px, py)
    BarraE.set_position(BXe,BYe)
    BarraD.set_position(BXd,BYd)

    while True: 

        #VELOCIDADE DA BOLA
        timePass = time.time() - timer
        if timePass>=0.1:
            ball.x = ball.x + velx*jan.delta_time()
            ball.y = ball.y + vely*jan.delta_time()

        #CRIAR A IA
        if velx > 0 and ball.x > jan.width/2 and ball.x < jan.width:
            if BarraD.y >= 0 and ball.y < BarraD.y + BarraD.height/2:
                    BarraD.y -= velBOT*jan.delta_time()
            if BarraD.y <= jan.height - BarraD.height and ball.y > BarraD.y + BarraD.height/2:
                    BarraD.y += velBOT*jan.delta_time()

        #BOLA BATENDO NAS PAREDES
        if ball.y >= jan.height - ball.height:
            bolaBate.play()
            ball.y = jan.height - ball.height
            vely *= -1
        elif ball.y <= 0:
            bolaBate.play()
            ball.y = 0
            vely *= -1
        if ball.x >= jan.height - ball.height:
            bolaBate.play()
            ball.x = jan.height - ball.height
            velx *= -1
        elif ball.x <= 0:
            bolaBate.play()
            ball.x = 0
            velx *= -1

        #MOVIEMNTAÇÃO DAS BARRAS
        if(teclado.key_pressed("w")):
            BarraE.y = BarraE.y - velBarraE*jan.delta_time()
        if(teclado.key_pressed("s")):
            BarraE.y = BarraE.y + velBarraE*jan.delta_time()

        #COLISÃO COM AS BARRAS
        if(BarraE.collided(ball)) and velx < 0:
            if velx > 0:
                bolaBate.play()
                velx += 10
                velx *= -1
            else:
                bolaBate.play()
                velx -= 10
                velx *= -1

        if(BarraD.collided(ball)) and velx > 0:
            if velx > 0:
                bolaBate.play()
                velx += 10
                velx *= -1
            else:
                bolaBate.play()
                velx -= 10
                velx *= -1

        #PATINAÇÃO DA BOLA
        if ball.x == BXe:
            ball.x = BXe
        if ball.x == BXd:
            ball.x = BXe

        #PONTUAÇÃO
        if ball.x >= jan.width - ball.width:
            iD += 1
            ball.set_position(px, py)
            BarraE.set_position(BXe,BYe)
            BarraD.set_position(BXd,BYd)
            velx = 220
        elif ball.x <= 0:
            iE += 1
            ball.set_position(px, py)
            BarraE.set_position(BXe,BYe)
            BarraD.set_position(BXd,BYd)
            velx = 220
        
        #COLISÃO COM A BORDA
        if BarraE.y >= jan.height - BarraE.height:
            BarraE.set_position(BXe,jan.height - BarraE.height)
        elif BarraE.y <= 0:
            BarraE.set_position(BXe, 0)
        
        if BarraD.y >= jan.height - BarraE.height:
            BarraD.set_position(BXd,jan.height - BarraE.height)
        elif BarraD.y <= 0:
            BarraD.set_position(BXd, 0)
        
        jan.set_background_color((255,0,0)) 

        #TEXTO

        fundo.draw()
        jan.draw_text("{} - {}".format(iD, iE),100, 50 , 45, (0,0,0), "Arial", False, False)
        ball.draw()
        BarraE.draw()
        BarraD.draw()
        jan.update()

def startGameSolo():
    clock = pygame.time.Clock()
    timer = time.time()
    #CRIANDO VARIÁVEIS NECESSÁRIAS
    iD = 0
    iE = 0
    jan = Window(600, 600)
    ball = Sprite("./Sprites./game/p503.png")
    BarraE = Sprite("./Sprites./game/barraE.png")
    BarraD = Sprite("./Sprites./game/barraD.png")
    fundo = GameImage("./Sprites./main/fundo.png") 
    teclado = Window.get_keyboard()

    #SONS
    bolaBate = pygame.mixer.Sound("./sons./menu/colide.mp3")
    bolaBate.set_volume(0.15)

    #DEFININDO VELOCIDADES
    velx = 220
    vely = 205
    velBarra = 250


    #DEFININDO POSIÇÕES
    BXe = BarraE.width
    BYe = jan.height/2 - BarraE.height/2

    BXd = jan.width - (2*BarraD.width)
    BYd = jan.height/2 - BarraE.height/2

    px = jan.width/2 - ball.width/2
    py = jan.height/2 - ball.height/2

    jan.set_title("Pong by LeMoS")
    ball.set_position(px, py)
    BarraE.set_position(BXe,BYe)
    BarraD.set_position(BXd,BYd)


    while True:

        #VELOCIDADE DA BOLA
        timePass = time.time() - timer
        if timePass >= 0.1:
            ball.x = ball.x + velx*jan.delta_time()
            ball.y = ball.y + vely*jan.delta_time()

        #BOLA BATENDO NAS PAREDES
        if ball.y >= jan.height - ball.height:
            ball.y = jan.height - ball.height
            bolaBate.play()
            vely *= -1
        elif ball.y <= 0:
            ball.y = 0
            bolaBate.play()
            vely *= -1
        if ball.x >= jan.height - ball.height:
            ball.x = jan.height - ball.height
            bolaBate.play()
            velx *= -1
        elif ball.x <= 0:
            ball.x = 0
            bolaBate.play()
            velx *= -1

        #MOVIEMNTAÇÃO DAS BARRAS PLAYER 1
        if(teclado.key_pressed("w")):
            BarraE.y = BarraE.y - velBarra*jan.delta_time()
        if(teclado.key_pressed("s")):
            BarraE.y = BarraE.y + velBarra*jan.delta_time()
        
        #MOVIEMNTAÇÃO DAS BARRAS PLAYER 1
        if(teclado.key_pressed("UP")):
            BarraD.y = BarraD.y - velBarra*jan.delta_time()
        if(teclado.key_pressed("DOWN")):
            BarraD.y = BarraD.y + velBarra*jan.delta_time()

        #COLISÃO COM AS BARRAS
        if(BarraE.collided(ball)) and velx < 0:
            if velx > 0:
                bolaBate.play()
                velx += 10
                velx *= -1
            else:
                bolaBate.play()
                velx -= 10
                velx *= -1

        if(BarraD.collided(ball)) and velx > 0:
            if velx > 0:
                bolaBate.play()
                velx *= -1
                velx += 10
            else:
                bolaBate.play()
                velx -= 10
                velx *= -1

        #PATINAÇÃO DA BOLA
        if ball.x == BXe:
            ball.x = BXe
        if ball.x == BXd:
            ball.x = BXe

        #PONTUAÇÃO
        if ball.x >= jan.width - ball.width:
            iD += 1
            ball.set_position(px, py)
            BarraE.set_position(BXe,BYe)
            BarraD.set_position(BXd,BYd)
            velx = 220
        elif ball.x <= 0:
            iE += 1
            ball.set_position(px, py)
            BarraE.set_position(BXe,BYe)
            BarraD.set_position(BXd,BYd)
            velx = 220
        
        #COLISÃO COM A BORDA
        if BarraE.y >= jan.height - BarraE.height:
            BarraE.set_position(BXe,jan.height - BarraE.height)
        elif BarraE.y <= 0:
            BarraE.set_position(BXe, 0)
        
        if BarraD.y >= jan.height - BarraE.height:
            BarraD.set_position(BXd,jan.height - BarraE.height)
        elif BarraD.y <= 0:
            BarraD.set_position(BXd, 0)
        
        jan.set_background_color((255,0,0)) 

        #TEXTO

        fundo.draw()
        jan.draw_text("{} - {}".format(iD, iE),100, 50 , 45, (0,0,0), "Arial", False, False)
        ball.draw()
        BarraE.draw()
        BarraD.draw()
        jan.update()