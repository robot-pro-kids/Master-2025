import random
import pyxel

class Hanabi:
    def __init__(self,anime,x,y):
        self.anime=anime
        self.anime.hanabis.append(self)
        self.hana_x=x+8
        self.hana_y=y
        self.hana_cnt=0
        self.hana_tim=random.randint(130,150)
        self.random = random.randint(0,1)
    def update(self):
        self.hana_cnt +=1
        if self.hana_cnt<self.hana_tim:
            self.hana_y-=1
            self.hana_ptn=0
        elif self.hana_cnt<self.hana_tim+30:
            self.hana_ptn=1
        elif self.hana_cnt<self.hana_tim+60:
            self.hana_ptn=2
        elif self.hana_cnt<self.hana_tim+90:
            self.hana_ptn=3
        else:
            if self.anime.hanabis:
                self.anime.hanabis.remove(self)
    def draw(self):
        if self.random==0:#円の花火
            if self.hana_ptn ==0:
                pyxel.circ(self.hana_x,self.hana_y,2,8)
            elif self.hana_ptn ==1:
                pyxel.circb(self.hana_x,self.hana_y,4,15)
            elif self.hana_ptn ==2:
                pyxel.circb(self.hana_x,self.hana_y,4,15)
                pyxel.circb(self.hana_x,self.hana_y,8,5)              
            elif self.hana_ptn ==3:
                pyxel.circb(self.hana_x,self.hana_y,8,5)
                pyxel.circb(self.hana_x,self.hana_y,16,8)
        else:#四角の花火
            if self.hana_ptn ==0:
                pyxel.rect(self.hana_x-2,self.hana_y-2,4,4,8)
            elif self.hana_ptn ==1:
                pyxel.rectb(self.hana_x-4,self.hana_y-4,8,8,15)
            elif self.hana_ptn ==2:
                pyxel.rectb(self.hana_x-4,self.hana_y-4,8,8,15)
                pyxel.rectb(self.hana_x-8,self.hana_y-8,16,16,5)    
            elif self.hana_ptn ==3:
                pyxel.rectb(self.hana_x-8,self.hana_y-8,16,16,5)
                pyxel.rectb(self.hana_x-16,self.hana_y-16,32,32,8)


class Pixelman:
  FS=-30
  GA=3
  def __init__(self,anime):
       self.anime = anime
       self.bn_x=0
       self.bn_y=Anime.SCREEN_HEIGHT-16
       self.bn_vx=1
       self.bn_vy=Pixelman.FS
       self.bn_ptn=1
       self.anime.pixelman = self
  def update(self,anime):
    if self.bn_ptn==0:
        self.bn_y+=self.bn_vy
        self.bn_vy+=Pixelman.GA
        if self.bn_y>Anime.SCREEN_HEIGHT:
            self.bn_y=Anime.SCREEN_HEIGHT-16
            self.bn_ptn=1
            self.bn_vy=Pixelman.FS

    else :
        if pyxel.btn(pyxel.KEY_RIGHT)==True:
            self.bn_x +=self.bn_vx
        elif pyxel.btn(pyxel.KEY_LEFT)==True:
            self.bn_x -=self.bn_vx
        if self.bn_x>Anime.SCREEN_WIDTH:
            self.bn_x=0
        elif self.bn_x <-16:
            self.bn_x=Anime.SCREEN_WIDTH-16
            
        if self.bn_x%5==0:
            self.bn_ptn *=-1
    if pyxel.btnp(pyxel.KEY_SPACE)==True:
        self.bn_ptn=0
    if pyxel.btnp(pyxel.KEY_RETURN):
        Hanabi(self.anime,self.bn_x,self.bn_y)
    self.anime.haikei.update(self.anime,self.bn_x,self.bn_y)

  def draw(self):        
     if self.bn_ptn==1:
            pyxel.blt(self.bn_x,self.bn_y,0,  0,0, 16,16,0)
     elif self.bn_ptn==-1:
            pyxel.blt(self.bn_x,self.bn_y,0,  16,0, 16,16,0)
     else:
         pyxel.blt(self.bn_x,self.bn_y,0,   0,0,  16,16,0)

class Haikei:
    def __init__(self,anime):
        self.anime=anime
        self.anime.haikei =self
        self.pos_start =0

    def update(self,anime,x,y):
        self.pos_start =x%32

    def draw(self):
        for i in range(-self.pos_start,Anime.SCREEN_WIDTH,32):
            pyxel.blt(i,0,1,0,0,31,191,0)



class Anime:
    SCREEN_WIDTH=256
    SCREEN_HEIGHT=196
    def __init__(self):
        pyxel.init(Anime.SCREEN_WIDTH,Anime.SCREEN_HEIGHT,title="piixelman")
        pyxel.load("my_resource.pyxres")
        self.hanabis=[]
        Pixelman(self)
        Haikei(self)
        pyxel.run(self.update,self.draw)

    def update(self):
        self.pixelman.update(Anime)
        for hanabi in self.hanabis.copy():
            hanabi.update()

    def draw(self):
        pyxel.cls(1)
        self.haikei.draw()
        self.pixelman.draw()
        for hanabi in self.hanabis.copy():
            hanabi.draw()       
        
    

Anime()    