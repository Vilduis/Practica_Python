
import pygame,sys,time
from pygame.locals import *

pygame.init()

ANCHOVENTANA=400
ALTOVENTANA=400

superficieVentana=pygame.display.set_mode((ANCHOVENTANA,ALTOVENTANA),0,32)
pygame.display.set_caption('Animacion')

ABAJOIZQUIERDA=1
ABAJODERECHA=3
ARRIBAIZQUIERDA=7
ARRIBADERECHA=9

VELOCIDADMOVIMIENTO=4

NEGRO=(0,0,0)
RED=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)


b1={'rect':pygame.Rect(300,80,50,100),'color':RED,'dir':ARRIBADERECHA}
b2={'rect':pygame.Rect(200,200,20,20),'color':VERDE,'dir':ARRIBAIZQUIERDA}
b3={'rect':pygame.Rect(100,150,60,60),'color':AZUL,'dir':ABAJOIZQUIERDA}

bloques=[b1,b2,b3]

while True:
    for evento in pygame.event.get():
        if evento.type == quit:
            pygame.quit()
            sys.exit()

    superficieVentana.fill(NEGRO)
    for b in bloques:
       if b['dir']==ABAJOIZQUIERDA:
           b['rect'].left -= VELOCIDADMOVIMIENTO
           b['rect'].top += VELOCIDADMOVIMIENTO
       if b['dir']==ABAJODERECHA:
           b['rect'].left += VELOCIDADMOVIMIENTO
           b['rect'].top += VELOCIDADMOVIMIENTO
       if b['dir']==ARRIBAIZQUIERDA:
           b['rect'].left -= VELOCIDADMOVIMIENTO
           b['rect'].top -= VELOCIDADMOVIMIENTO
       if b['dir']==ARRIBADERECHA:
           b['rect'].left += VELOCIDADMOVIMIENTO
           b['rect'].top -= VELOCIDADMOVIMIENTO

       if b['rect'].top<0:
           if b['dir']==ARRIBAIZQUIERDA:
               b['dir']=ABAJOIZQUIERDA
           if b['dir']==ARRIBADERECHA:
               b['dir']=ABAJODERECHA
       if b['rect'].bottom>ALTOVENTANA:
             if b['dir']==ABAJOIZQUIERDA:
                 b['dir']=ARRIBAIZQUIERDA
             if b['dir']==ABAJODERECHA:
                 b['dir']=ARRIBADERECHA
       if b['rect'].left<0:
            if b['dir']==ABAJOIZQUIERDA:
                b['dir']=ABAJODERECHA
            if b['dir']==ARRIBAIZQUIERDA:
                b['dir']=ARRIBADERECHA
       if b['rect'].right>ANCHOVENTANA:
             if b['dir']==ABAJODERECHA:
                 b['dir']=ABAJOIZQUIERDA
             if b['dir']==ARRIBADERECHA:
                 b['dir']=ARRIBAIZQUIERDA
       pygame.draw.rect(superficieVentana,b['color'],b['rect'])
    pygame.display.update()
    time.sleep(0.02)




    



