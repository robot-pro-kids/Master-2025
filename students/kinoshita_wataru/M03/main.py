import pyxel
import random

class Pixelman:
    FS = -30
    GA = 3
    def __init__(self,anime):
        self.anime = anime
        self.bn_x = 1
        self.bn_y = Anime.SCREEN_HIGHT - 16
        self.bn_vx = 1
        self.bn_vy = Pixelman.FS
        self.bn_ptn = 1
        self.anime.pixelman = self
        self.action = 0

    def update(self,anime):
        if self.bn_ptn == 0:
            self.bn_y += self.bn_vy
            self.bn_vy += Pixelman.GA
            if self.bn_y > Anime.SCREEN_HIGHT:
                self.bn_y = Anime.SCREEN_HIGHT - 16
                self.bn_ptn = 1
                self.bn_vy = Pixelman.FS
            if self.bn_y < 0:
                self.bn_vy *= -1
        else:

            if pyxel.btn(pyxel.KEY_RIGHT):
                self.bn_x += self.bn_vx
                self.action = 1
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.bn_x -= self.bn_vx
                self. action = -1
            else:
                self.action = 0

            if self.bn_x > Anime.SCREEN_WIDTH:
                self.bn_x = 0
            elif self.bn_x < -16:
                self.bn_x = Anime.SCREEN_WIDTH - 16

            if self.bn_x % 5 == 0:
                self.bn_ptn *= -1
            
        if self.bn_ptn == 2:
            self.bn_vx += 2

        if pyxel.btnp(pyxel.KEY_SPACE) == True:
            self.bn_ptn = 0

        if pyxel.btn(pyxel.KEY_RETURN):
            Hanabi(self.anime,self.bn_x,self.bn_y)

        self.anime.haikei.update(self.anime,self.bn_x,self.bn_y)
        self.anime.haikei2.update(self.anime,self.bn_x,self.bn_y)
            
    def draw(self):
        if self.bn_ptn == 1:
            pyxel.blt(self.bn_x,self.bn_y,0,0,0,16,16,0)
        elif self.bn_ptn == -1:
            pyxel.blt(self.bn_x,self.bn_y,0,16,0,16,16,0)
        elif self.bn_ptn == 0:
            pyxel.blt(self.bn_x,self.bn_y,0,32,0,16,16,0)

class Hanabi:
    def __init__(self,anime,x,y):
        self.anime = anime
        self.anime.hanabis.append(self)
        self.hana_x = x + 8
        self.hana_y = y
        self.hana_cnt = 0
        self.hana_tim = random.randint(0,150)
        self.a = random.randint(0,16)
        self.b = random.randint(0,16)
        self.c = random.randint(0,16)
        self.d = random.randint(0,8)
        self.e = random.randint(8,15)
        self.f = random.randint(15,23)
        self.g = random.randint(23,30)

    def update(self,s=0, a=0):
        if a==1:
            self.hana_x -= s
        elif a==-1:
            self.hana_x += s
        self.hana_cnt += 1
        if self.hana_cnt < self.hana_tim:
            self.hana_y -= 1
            self.hana_ptn = 0
        elif self.hana_cnt < self.hana_tim + 15:
            self.hana_ptn = 1
        elif self.hana_cnt < self.hana_tim + 30:
            self.hana_ptn = 2
        elif self.hana_cnt < self.hana_tim + 45:
            self.hana_ptn = 3
        else:
            if self.anime.hanabis:
                self.anime.hanabis.remove(self)

    def draw(self):
        if self.hana_ptn == 0:
            pyxel.circ(self.hana_x,self.hana_y,self.d,self.a)
        elif self.hana_ptn == 1:
            pyxel.circb(self.hana_x,self.hana_y,self.e,self.b)
        elif self.hana_ptn == 2:
            pyxel.circb(self.hana_x,self.hana_y,self.e,self.b)
            pyxel.circb(self.hana_x,self.hana_y,self.f,self.c)
        elif self.hana_ptn == 3:
            pyxel.circb(self.hana_x,self.hana_y,self.f,self.c)
            pyxel.circb(self.hana_x,self.hana_y,self.g,self.a)

class Haikei:
    def __init__(self,anime):
        self.anime = anime
        self.anime.haikei = self
        self.pos_start = 0

    def update(self,anime,x,y):
        self.pos_start = x//8 % 32
    def draw(self):
        for i in range (-self.pos_start,Anime.SCREEN_WIDTH,32):
            pyxel.blt( i , 0 ,
                      1 ,
                      0 , 0 ,
                      31 , 175 ,
                      0)

class Haikei2:
    def __init__(self,anime):
        self.anime = anime
        self.anime.haikei2 = self
        self.pos_start = 0

    def update(self,anime,x,y):
        self.pos_start = x % 32
    def draw(self):
        for i in range (-self.pos_start,Anime.SCREEN_WIDTH,32):
            pyxel.blt( i , 175 ,
                      1 ,
                      0 , 175 ,
                      31 , 16 ,
                      0)

class Anime:
    SCREEN_WIDTH = 256
    SCREEN_HIGHT = 196
    def __init__(self):
        pyxel.init(Anime.SCREEN_WIDTH,Anime.SCREEN_HIGHT,title="Pixelman")
        pyxel.load("my_resource.pyxres")
        self.hanabis = []
        self.sosuu = 100
        self.cnt = 1
        Pixelman(self)
        Haikei(self)
        Haikei2(self)
        pyxel.run(self.update,self.draw)

    def update(self):
        self.pixelman.update(Anime)
        for hanabi in self.hanabis.copy():
            hanabi.update(self.pixelman.bn_vx,self.pixelman.action)

    def draw(self):
        pyxel.cls(1)
        self.haikei.draw()
        self.haikei2.draw()
        self.pixelman.draw()
        for hanabi in self.hanabis.copy():
            hanabi.draw()
Anime()