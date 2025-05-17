import pyxel
import random

class Pixelman:
    FS = -30  
    GA = 2.8
    def __init__(self,anime):
        self.anime = anime
        self.bn_x = 0
        self.bn_y = Anime.SCREEN_HIGHT - 16
        self.bn_vx = 1
        self.bn_vy = Pixelman.FS
        self.bn_ptn = 1
        self.anime.pixelman = self

    def update(self,anime):
        if self.bn_ptn == 0:
            self.bn_y += self.bn_vy
            self.bn_vy += Pixelman.GA
            if self.bn_y > Anime.SCREEN_HIGHT:
                self.bn_y = Anime.SCREEN_HIGHT - 16
                self.bn_ptn = 1
                self.bn_vy = Pixelman.FS

        else:
            if pyxel.btn(pyxel.KEY_D) == True :
                self.bn_x += self.bn_vx
            elif pyxel.btn(pyxel.KEY_A) == True :
                self.bn_x -= self.bn_vx
            if self.bn_x > Anime.SCREEN_WIDTH:
                self.bn_x = 0
            elif self.bn_x < -16 :
                self.bn_x = Anime.SCREEN_WIDTH - 16

        if pyxel.btnp(pyxel.KEY_SPACE) == True:
            self.bn_ptn = 0

        if pyxel.btnp(pyxel.KEY_W):
            Hanabi(self.anime,self.bn_x,self.bn_y)
        self.anime.haikei.update(self.anime,self.bn_x,self.bn_y)

    def draw(self):
        if self.bn_ptn == 1:
            pyxel.blt(self.bn_x,self.bn_y, 0,  0,0, 16,16, 0)
        elif self.bn_ptn == -1:
            pyxel.blt(self.bn_x,self.bn_y, 0, 16,0, 16,16, 0)
        else:
            pyxel.blt(self.bn_x,self.bn_y, 0,  32,0, 16,16, 0)

class Hanabi :
    def __init__(self,anime,x,y):
        self.anime = anime
        self.anime.hanabis.append(self)
        self.hana_x = x + 8
        self.hana_y = y
        self.hana_cnt = 0
        self.hana_tim = 150
        self.a = random.randint(0,16)
        self.b = random.randint(0,16)
        self.c = random.randint(0,16)
        self.d = random.randint(0,16)
        self.e = random.randint(0,16)
        self.f = random.randint(0,16)

        self.r_a = random.randint(0,16)
        self.r_b = random.randint(16,20)
        self.r_c = random.randint(20,25)
        self.r_d = random.randint(25,30)
        self.r_e = random.randint(30,35)


    def update(self):
        self.hana_cnt += 1
        if self.hana_cnt < self.hana_tim :
            self.hana_y -= 1
            self.hana_ptn =0
        elif self.hana_cnt < self.hana_tim+30:
            self.hana_ptn = 1
        elif self.hana_cnt < self.hana_tim+60:
            self.hana_ptn =2
        elif self.hana_cnt < self.hana_tim+90:
            self.hana_ptn =3
        elif self.hana_cnt < self.hana_tim+120:
            self.hana_ptn =4
        elif self.hana_cnt < self.hana_tim+150:
            self.hana_ptn =5
        else :
            if self.anime.hanabis :
                self.anime.hanabis.remove(self)


    
    def draw(self):
        if self.hana_ptn == 0 :
            pyxel.circ(self.hana_x,self.hana_y,2,self.a)
        elif self.hana_ptn == 1 :
            pyxel.circb(self.hana_x,self.hana_y,self.r_a,self.b)
        elif self.hana_ptn == 2 :
            pyxel.circb(self.hana_x,self.hana_y,self.r_a,self.b)
            pyxel.circb(self.hana_x,self.hana_y,self.r_b,self.c)
        elif self.hana_ptn == 3 :
            pyxel.circb(self.hana_x,self.hana_y,self.r_b,self.c)
            pyxel.circb(self.hana_x,self.hana_y,self.r_c,self.d)
        elif self.hana_ptn == 4 :
            pyxel.circb(self.hana_x,self.hana_y,self.r_c,self.d)
            pyxel.circb(self.hana_x,self.hana_y,self.r_d,self.e)
        elif self.hana_ptn == 5 :
            pyxel.circb(self.hana_x,self.hana_y,self.r_d,self.e)
            pyxel.circb(self.hana_x,self.hana_y,self.r_e,self.f)

class Haikei:
    def __init__(self,anime):
        self.anime = anime
        self.anime.haikei = self
        self.pos_start = 0

    def update(self,anime,x,y):
        self.pos_start = x % 16

    def draw(self):
        for i in range(-self.pos_start,Anime.SCREEN_WIDTH,16):
            pyxel.blt(i, 0,
                      1,
                      0, 0,
                     15, 191,
                      0)

class Anime:
    SCREEN_WIDTH = 256
    SCREEN_HIGHT = 196
    def __init__(self):
        pyxel.init(Anime.SCREEN_HIGHT,Anime.SCREEN_HIGHT,title="Pixelman")
        pyxel.load("my_resource.pyxres")
        self.hanabis=[]
        Pixelman(self)
        Haikei(self)
        pyxel.run(self.update,self.draw)

    def update(self):
 #       self.pixelman.update()
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
