import pygame
import random
from playsound import playsound

pygame.init()

screen = pygame.display.set_mode((400,700))

COLOR = (210,252,252)
WHITE = (2,90,92)
RED = (255,0,0)
VIOLET = (242,184,236)
RED1 = (250,190,190)
GRAY = (186,182,182)
running = True
rect_x=30
rect_y=40
width=150
longs=50
ok=0
font = pygame.font.SysFont('arial',20)
text_1 = font.render('Honggg iuuu',True,COLOR)
text_2 = font.render('Em iu anhhhh!!',True,RED)
text_3 = font.render('Em co iu anh honggg?',True,RED)
text_4 = font.render('Nhap de tra loi!',True,RED)
text_5 = font.render('Anh cung iu em <3<3',True,COLOR)
text_6 = font.render('Nhap de tiep tuc!',True,COLOR)
text_7 = font.render('Thoat!',True,COLOR)
run1 = True
while running:
    screen.fill(COLOR)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if ok == 0:
        pygame.draw.rect(screen,RED1,(100,325,200,50))
        screen.blit(text_3, (100,325))
        screen.blit(text_4, (150,350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_x > 100 and mouse_x < 300 and mouse_y > 325 and mouse_y < 375:
                        ok=1
    if ok == 1:
        pygame.draw.rect(screen,WHITE,(rect_x,rect_y,width,longs))
        pygame.draw.rect(screen,VIOLET,(100,400,width,longs))
        screen.blit(text_2, (100,400))
        screen.blit(text_1, (rect_x,rect_y))
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_x > rect_x and mouse_x < (rect_x+width) and mouse_y > rect_y and mouse_y < rect_y + longs:
                        pygame.draw.rect(screen,COLOR,(rect_x,rect_y,width,longs))
                        rect_x=random.randint(1,200)
                        rect_y=random.randint(1,600)
                        while rect_y > 350 and rect_y <450 :
                            rect_y=random.randint(1,600)
                    if mouse_x > 100 and mouse_x <250 and mouse_y > 400 and mouse_y <450: 
                        ok = 2
    if ok == 2:
        pygame.draw.polygon(screen,RED,((200,250),(300,350),(200,450),(100,350)))
        pygame.draw.circle(screen,RED,(145,295),71)
        pygame.draw.circle(screen,RED,(255,295),71)
        screen.blit(text_5,(129,279))
        screen.blit(text_6,(141,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_x > 100 and mouse_x <300 and mouse_y > 250 and mouse_y < 400: 
                        ok = 3
    if ok == 3:
        pygame.draw.circle(screen,GRAY,(200,350),100,1)
        pygame.draw.rect(screen,GRAY,(150,300,25,100))
        pygame.draw.rect(screen,GRAY,(225,300,25,100))
        pygame.draw.polygon(screen,RED,((380,5),(395,20),(380,20),(365,20)))
        pygame.draw.rect(screen,RED,(370,20,20,20))
        screen.blit(text_7,(330,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_x > 100 and mouse_x <300 and mouse_y > 250 and mouse_y < 400:
                        pygame.mixer.init()
                        pygame.mixer.music.load("HPBD.mp3")
                        pygame.mixer.music.play()
    pygame.display.flip()

pygame.quit()