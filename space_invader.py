import pygame
import time
pygame.init()

wwid = 800
whei = 600

screen = pygame.display.set_mode((wwid, whei))
pygame.display.set_caption("LEVEL DESIGNING")

White = (255, 255, 255)
Black = (0, 0, 0)

def ShowText(text,x,y,color):
    font = pygame.font.SysFont("Arial", 40)
    TextSurface = font.render(text,True,color)
    screen.blit(TextSurface, (x,y))

def makegrid():
    for loop in range(1,17):
        pygame.draw.line(screen,White,(loop*Cellsize,0),(loop*Cellsize,800))
        pygame.draw.line(screen,White,(0,loop*Cellsize),(800,loop*Cellsize))



class Game ():
    def __init__(self):
        self.LevelObj = True
    @staticmethod
    def LevelInit(self):
        global CurrLevel,Levels
        if CurrLevel<3:
            screen.fill(Black)
            ShowText("Level "+str(CurrLevel+1),300,whei/2,White)
            pygame.display.update()
            time.sleep(2)
            createStruct(Levels[CurrLevel])

            CurrLevel+=1
            return
        
        ##for the winner slide 
        CurrLevel = min(len(Levels)+1,CurrLevel+1)

    def NextLevel(self):
        global EnvObj,CurrLevel
        if self.LevelObj == True:
            EnvObj = []
            self.LevelObj = False
            Game.LevelInit(self)

class Alien():
    AlienObj = []
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        self.HP=1
##this is basically speed
        self.counter=0
        self.direction = 1
    def move(self):
        self.x += self.direction
        self.counter +=1
        if abs(self.counter)>220:
            self.direction = -self.direction
            self.counter *= self.direction
            self.y+=30
    def show(self):
        screen.blit(self.image, (self.x,self.y))


class HenchLien(Alien):
    def __init__ (self,image,xCoord,yCoord):
        super().__init__(xCoord,yCoord)
        self.HP = 1
        self.image = image

Cellsize = 50

HenchAlien = pygame.image.load(""
"vaderb2.png")

HenchAlien = pygame.transform.scale(HenchAlien,(50,40))



BossAlien = pygame.image.load(""
"vaderb2.png")
BossAlien = pygame.transform.scale(BossAlien,(50,40))

Player = pygame.image.load(""
"vaderb2.png")
Player = pygame.transform.scale(Player,(50,49))
global DictRes
DictRes = {
    '0':HenchAlien,
    '1':BossAlien
}

LevelOneList = [
    ['0','0','0','-1','0','0','0'],
    ['0','-1','0','-1','0','-1','0'],
    ['0','0','0','-1','0','0','0']
]

Levels = [LevelOneList]

SpaceInvaders = Game()

# AlienObj = []

def createStruct(level):
    for i,row in enumerate(level):
        for j,column in enumerate(row):
            print(column)
            if column in DictRes:
                Alien.AlienObj.append(
                    HenchLien(DictRes[column],Cellsize*-j+500,Cellsize*i))

createStruct(LevelOneList)

#gameloop
while True:
    pygame.time.delay(10)
    screen.fill(Black)
    for loop in Alien.AlienObj:
        loop.show()
        loop.move()
   
       

    makegrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
