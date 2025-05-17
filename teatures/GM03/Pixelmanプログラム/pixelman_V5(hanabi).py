import pyxel

class Pixelman :
    FS = -30
    GA = 3
    def __init__(self,anime) :
        self.anime = anime
        self.bn_x = 0
        self.bn_y = Anime.SCREEN_HIGHT - 16
        self.bn_vx = 1
        self.bn_vy = Pixelman.FS
        self.bn_ptn = 1
        self.anime.pixelman = self

    def update(self,anime) :
        if self.bn_ptn == 0 :
            self.bn_y += self.bn_vy
            self.bn_vy += Pixelman.GA
            if self.bn_y > Anime.SCREEN_HIGHT :
                self.bn_y = Anime.SCREEN_HIGHT - 16
                self.bn_ptn = 1
                self.bn_vy = Pixelman.FS
 
        else :
            if pyxel.btn(pyxel.KEY_RIGHT) == True :
                self.bn_x += self.bn_vx    
            elif pyxel.btn(pyxel.KEY_LEFT) == True :
                self.bn_x -= self.bn_vx

            if self.bn_x > Anime.SCREEN_WIDTH :
                self.bn_x = 0
            elif self.bn_x < -16 :
                self.bn_x = Anime.SCREEN_WIDTH - 16

            if self.bn_x % 5 == 0 : 
                self.bn_ptn *= -1

        if pyxel.btnp(pyxel.KEY_SPACE) == True :
            self.bn_ptn = 0

        if pyxel.btnp(pyxel.KEY_RETURN) :
            Hanabi(self.anime,self.bn_x,self.bn_y)

    def draw(self) :
        if self.bn_ptn == 1 :
            pyxel.blt(self.bn_x,self.bn_y ,0,   0,0 , 16,16 ,0 )
        elif self.bn_ptn == -1 :
            pyxel.blt(self.bn_x,self.bn_y ,0,  16,0 , 16,16 ,0 )
        else :
            pyxel.blt(self.bn_x,self.bn_y ,0,   0,0 , 16,16 ,0 )

class Hanabi :
    def __init__(self,anime,x,y) :
        self.anime = anime
        self.anime.hanabis.append(self) 
        self.hana_x = x + 8 
        self.hana_y = y
        self.hana_cnt = 0
        self.hana_tim = 150

    def update(self) :
        self.hana_cnt += 1
        if self.hana_cnt < self.hana_tim :
            self.hana_y -= 1
            self.hana_ptn = 0
        elif self.hana_cnt < self.hana_tim+30 :
            self.hana_ptn = 1
        elif self.hana_cnt < self.hana_tim+60 :
            self.hana_ptn = 2
        elif self.hana_cnt < self.hana_tim+90 :
            self.hana_ptn = 3
        else :
            if self.anime.hanabis :
                self.anime.hanabis.remove(self)

    def draw(self) :
        if self.hana_ptn == 0 :
            pyxel.circ(self.hana_x,self.hana_y,2,8)    
        elif self.hana_ptn == 1 :
            pyxel.circb(self.hana_x,self.hana_y,4,15)    
        elif self.hana_ptn == 2 :
            pyxel.circb(self.hana_x,self.hana_y,4,15)    
            pyxel.circb(self.hana_x,self.hana_y,8, 5)    
        elif self.hana_ptn == 3 :
            pyxel.circb(self.hana_x,self.hana_y,8, 5)    
            pyxel.circb(self.hana_x,self.hana_y,16,8)    

class Anime :
    SCREEN_WIDTH = 256
    SCREEN_HIGHT = 196 

    def __init__(self) :
        pyxel.init(Anime.SCREEN_WIDTH,Anime.SCREEN_HIGHT,title="Pixelman")
        pyxel.load("my_resource.pyxres")
        self.hanabis=[]
        Pixelman(self)
        pyxel.run(self.update,self.draw)

    def update(self) :
#        self.pixelman.update()
        self.pixelman.update(Anime)
        for hanabi in self.hanabis.copy() :
            hanabi.update()

    def draw(self) :
        pyxel.cls(1)
        self.pixelman.draw()
        for hanabi in self.hanabis.copy() :
            hanabi.draw()

Anime()

