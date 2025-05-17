import pyxel

class Pixelman :
    def __init__(self,anime) :
        self.anime = anime
        self.bn_x = 0
        self.bn_y = Anime.SCREEN_HIGHT - 16
        self.bn_vx = 1
        self.bn_vy = 0
        self.bn_ptn = 1
        self.anime.pixelman = self          #クラス「Pixelman」をクラス「Anime」に登録する

    def update(self) :
        self.bn_x += self.bn_vx
        if self.bn_x > Anime.SCREEN_WIDTH :
            self.bn_x = 0
        if self.bn_x % 5 == 0 : 
            self.bn_ptn *= -1

    def draw(self) :
        if self.bn_ptn == 1 :
            pyxel.blt(self.bn_x,self.bn_y ,0,   0,0 , 16,16 ,0 )
        elif self.bn_ptn == -1 :
            pyxel.blt(self.bn_x,self.bn_y ,0,  16,0 , 16,16 ,0 )    

class Anime :
    SCREEN_WIDTH = 256
    SCREEN_HIGHT = 196 

    def __init__(self) :
        pyxel.init(Anime.SCREEN_WIDTH,Anime.SCREEN_HIGHT,title="Pixelman")
        pyxel.load("my_resource.pyxres")
        Pixelman(self)                      #クラス「Pixelman」の実体化
        pyxel.run(self.update,self.draw)

    def update(self) :
        self.pixelman.update()

    def draw(self) :
        pyxel.cls(1)
        self.pixelman.draw()

Anime()

