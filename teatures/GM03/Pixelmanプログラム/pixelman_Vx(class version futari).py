import pyxel

class Pixelman :
    def __init__(self,anime,y) :
        self.anime = anime
        self.bn_x = 0
#        self.bn_y = Anime.SCREEN_HIGHT - 16
        self.bn_y = y
        self.bn_vx = 1
        self.bn_vy = 0
        self.bn_ptn = 1
        self.anime.pixelmans.append(self)  #####

    def draw_char(self,x,y,ptn) :
        if ptn == 1 :
            pyxel.blt(x,y ,0,   0,0 , 16,16 ,0 )
        elif ptn == -1 :
            pyxel.blt(x,y ,0,  16,0 , 16,16 ,0 )    

    def update(self) :
        self.bn_x += self.bn_vx
        if self.bn_x > Anime.SCREEN_WIDTH :
            self.bn_x = 0
        if self.bn_x % 5 == 0 : 
            self.bn_ptn *= -1

    def draw(self) :
        self.draw_char(self.bn_x,self.bn_y,self.bn_ptn)

class Anime :
    SCREEN_WIDTH = 256
    SCREEN_HIGHT = 196 

    def __init__(self) :
        pyxel.init(Anime.SCREEN_WIDTH,Anime.SCREEN_HIGHT,title="Pixelman")
        pyxel.load("my_resource.pyxres")
        self.pixelmans=[]
        Pixelman(self,100)
        Pixelman(self,150)
        pyxel.run(self.update,self.draw)

    def update(self) :
#        self.pixelman.update()
        for pixelman in self.pixelmans.copy() :
            pixelman.update()
    def draw(self) :
        pyxel.cls(1)
#        self.pixelman.draw()
        for pixelman in self.pixelmans.copy() :
            pixelman.draw()
 
Anime()

