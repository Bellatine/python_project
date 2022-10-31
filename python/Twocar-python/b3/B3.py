import pygame
import random

pygame.init()

screen=pygame.display.set_mode((400,800))
pygame.display.set_caption('Two car -- GN version ')
running = True
BLUE = (99,233,247)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (49,196,12)
font = pygame.font.SysFont('sans',25)
font1 = pygame.font.SysFont('sans',50)
text_1 = font.render('Score',True,GREEN)
text_3 = font1.render('GAME OVER',True,GREEN)
point =0

clock = pygame.time.Clock()
pygame.mixer.init()
car1 = pygame.image.load('Redcar.png')
car2 = pygame.image.load('Bluecar.png')
circle_x = 0
circle_y = 0
rect_x = 0
rect_y = 0
circle1_x = 0
circle1_y = 0
rect1_x = 0
rect1_y = 0
circle3_x = 0
circle3_y = 0
rect3_x = 0
rect3_y = 0
circle4_x = 0
circle4_y = 0
rect4_x = 0
rect4_y = 0

car1_x = 5
car1_y = 650
car2_x = 205
car2_y = 650
speed_car=5
speed_v = 5
ok=0
ok1=0
n = random.randint(1,4)
m = random.randint(1,4)
n1 = random.randint(1,4)
m1 = random.randint(1,4)
count = 0
ktra = 0
t=1
t1=1
oke=1
while running:
    clock.tick(60)
    pygame.draw.rect(screen,BLUE,(0,0,200,800))
    pygame.draw.rect(screen,RED,(200,0,200,800))
    #pygame.draw.rect(screen,WHITE,(0,645,400,2))
    text_2 = font.render(str(point),True,GREEN)
    if n==1 :
        if circle_x == 0:
            circle_x = 50
            circle_y = 50
        circle_y+=speed_v
        count += 1
        pygame.draw.circle(screen,RED,(circle_x,circle_y),40,15)
    if n==2 :
        if circle_x == 0:
            circle_x = 150
            circle_y = 50
        circle_y+=speed_v
        count += 1
        pygame.draw.circle(screen,RED,(circle_x,circle_y),40,15)
    if n==3 :
        if rect_x == 0:
            rect_x = 10
            rect_y = 2
        rect_y+=speed_v
        count += 1
        pygame.draw.rect(screen,RED,(rect_x,rect_y,80,80),15)
    if n==4 :
        if rect_x == 0:
            rect_x = 110
            rect_y = 2
        rect_y+=speed_v
        count += 1
        pygame.draw.rect(screen,RED,(rect_x,rect_y,80,80),15)
    if m==1 :
        if circle1_x == 0:
            circle1_x = 50
            circle1_y = 50
        if ktra == 0:
            circle1_x = 50
            circle1_y = 300
        circle1_y+=speed_v
        pygame.draw.circle(screen,RED,(circle1_x,circle1_y),40,15)
    if m==2 :
        if circle1_x == 0:
            circle1_x = 150
            circle1_y = 50
        if ktra == 0:
            circle1_x = 150
            circle1_y = 300
        circle1_y+=speed_v
        pygame.draw.circle(screen,RED,(circle1_x,circle1_y),40,15)
    if m==3 :
        if rect1_x == 0:
            rect1_x = 10
            rect1_y = 2
        if ktra == 0:
            rect1_x = 10
            rect1_y = 330
        rect1_y+=speed_v
        pygame.draw.rect(screen,RED,(rect1_x,rect1_y,80,80),15)
    if m==4 :
        if rect1_x == 0:
            rect1_x = 110
            rect1_y = 2
        if ktra == 0:
            rect1_x = 110
            rect1_y = 330
        rect1_y+=speed_v
        pygame.draw.rect(screen,RED,(rect1_x,rect1_y,80,80),15)
    if n1==1 :
        if circle3_x == 0:
            circle3_x = 250
            circle3_y = 50
        circle3_y+=speed_v
        pygame.draw.circle(screen,BLUE,(circle3_x,circle3_y),40,15)
    if n1==2 :
        if circle3_x == 0:
            circle3_x = 350
            circle3_y = 50
        circle3_y+=speed_v
        pygame.draw.circle(screen,BLUE,(circle3_x,circle3_y),40,15)
    if n1==3 :
        if rect3_x == 0:
            rect3_x = 210
            rect3_y = 2
        rect3_y+=speed_v
        pygame.draw.rect(screen,BLUE,(rect3_x,rect3_y,80,80),15)
    if n1==4 :
        if rect3_x == 0:
            rect3_x = 310
            rect3_y = 2
        rect3_y+=speed_v
        pygame.draw.rect(screen,BLUE,(rect3_x,rect3_y,80,80),15)
    if m1==1 :
        if circle4_x == 0:
            circle4_x = 250
            circle4_y = 50
        if ktra == 0:
            circle4_x = 250
            circle4_y = 300
        circle4_y+=speed_v
        pygame.draw.circle(screen,BLUE,(circle4_x,circle4_y),40,15)
    if m1==2 :
        if circle4_x == 0:
            circle4_x = 350
            circle4_y = 50
        if ktra == 0:
            circle4_x = 350
            circle4_y = 300
        circle4_y+=speed_v
        pygame.draw.circle(screen,BLUE,(circle4_x,circle4_y),40,15)
    if m1==3 :
        if rect4_x == 0:
            rect4_x = 210
            rect4_y = 2
        if ktra == 0:
            rect4_x = 210
            rect4_y = 330
        rect4_y+=speed_v
        pygame.draw.rect(screen,BLUE,(rect4_x,rect4_y,80,80),15)
    if m1==4 :
        if rect4_x == 0:
            rect4_x = 310
            rect4_y = 2
        if ktra == 0:
            rect4_x = 310
            rect4_y = 330
        rect4_y+=speed_v
        pygame.draw.rect(screen,BLUE,(rect4_x,rect4_y,80,80),15)
    if oke == 1 :
        if count == 660/speed_v:
            rect_y = 0
            rect_x = 0
            circle_x = 0
            circle_y = 0
            rect3_y = 0
            rect3_x = 0
            circle3_x = 0
            circle3_y = 0
            count = 0
            n = random.randint(1,4)
            n1 = random.randint(1,4)
            t=1
            t1=1
            if point % 20 == 0:
                speed_v += 1
        else:
            if count == 330/speed_v:
                rect1_y = 0
                rect1_x = 0
                circle1_x = 0
                circle1_y = 0
                m = random.randint(1,4)
                rect4_y = 0
                rect4_x = 0
                circle4_x = 0
                circle4_y = 0
                m1 = random.randint(1,4)
                t=1
                t1=1
                if point % 20 == 0:
                    speed_v += 1
        ktra = 1


        screen.blit(car1,(car1_x,car1_y))
        screen.blit(car2,(car2_x,car2_y))
        screen.blit(text_1,(3,50))
        screen.blit(text_2,(3,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1 and car1_x==105:
                    ok=-1
                else:
                    if event.key == pygame.K_2 and car1_x==5:
                        ok=+1
                if event.key == pygame.K_LEFT and car2_x==305:
                    ok1=-1
                else:
                    if event.key == pygame.K_RIGHT and car2_x==205:
                        ok1=+1
        if ok==-1 and car1_x>5:
            car1_x+=ok*speed_car
        else:
            if ok==1 and car1_x<105:
                car1_x+=ok*speed_car
        if ok1==-1 and car2_x>205:
            car2_x+=ok1*speed_car
        else:
            if ok1==1 and car2_x<305:
                car2_x+=ok1*speed_car
        if circle_x-40<=car1_x<=circle_x+40 and circle_y-40<=car1_y<=circle_y+40 :
            point += t
            t=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle1_x-40<=car1_x<=circle1_x+40 and circle1_y-40<=car1_y<=circle1_y+40 :
            point += t
            t=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle1_x-40<=car1_x+80<=circle1_x+40 and circle1_y-40<=car1_y<=circle1_y+40:
            point += t
            t=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle_x-40<=car1_x+80<=circle_x+40 and circle_y-40<=car1_y<=circle_y+40:
            point += t
            t=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle3_x-40<=car2_x<=circle3_x+40 and circle3_y-40<=car2_y<=circle3_y+40 :
            point += t1
            t1=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle4_x-40<=car2_x<=circle4_x+40 and circle4_y-40<=car2_y<=circle4_y+40 :
            point += t1
            t1=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle4_x-40<=car2_x+80<=circle4_x+40 and circle4_y-40<=car2_y<=circle4_y+40:
            point += t1
            t1=0
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()
        if circle3_x-40<=car2_x+80<=circle3_x+40 and circle3_y-40<=car2_y<=circle3_y+40:
            point += t1
            t1=0 
            pygame.mixer.music.load("quac.mp3")
            pygame.mixer.music.play()   
        if rect_x-10<=car1_x<=rect_x+90 and rect_y<=car1_y<=rect_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect_x-10<=car1_x+80<=rect_x+90 and rect_y<=car1_y<=rect_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect1_x-10<=car1_x<=rect1_x+90 and rect1_y<=car1_y<=rect1_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect1_x-10<=car1_x+80<=rect1_x+90 and rect1_y<=car1_y<=rect1_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect3_x-10<=car2_x<=rect3_x+90 and rect3_y<=car2_y<=rect3_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect3_x-10<=car2_x+80<=rect3_x+90 and rect3_y<=car2_y<=rect3_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect4_x-10<=car2_x<=rect4_x+90 and rect4_y<=car2_y<=rect4_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
        if rect4_x-10<=car2_x+80<=rect4_x+90 and rect4_y<=car2_y<=rect4_y+100:
            oke = 0
            pygame.mixer.music.load('over.mp3')
            pygame.mixer.music.play()
    else:
        screen.blit(text_3,(50,350))
        speed_v=0
        if count == 300:     
            running = False       
    pygame.display.flip()
pygame.quit()
