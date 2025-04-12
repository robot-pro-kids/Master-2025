import pyxel
class Pixelman:
  FS=-30
  GA=3
  def __init__(self,anime):
       self.anime = anime
       self.bn_x=0
       self.bn_y=Anime.screen_hight-16
       self.bn_vx=1
       self.bn_vy=Pixelman.FS
       self.bn_ptn=1
       self.anime.pixelman = self
  def update(self):
    if self.bn_ptn==0:
        self.bn_y+=self.bn_vy
        self.bn_vy+=Pixelman.GA
        if self.bn_y>Anime.screen_hight:
            self.bn_y=Anime.screen_hight-16
            self.bn_ptn=1
            self.bn_vy=Pixelman.FS

    else :
        self.bn_x +=self.bn_vx
        if self.bn_x>Anime.screen_width:
            self.bn_x=0
        if self.bn_x%5==0:
            self.bn_ptn *=-1
    if pyxel.btnp(pyxel.KEY_SPACE)==True:
        self.bn_ptn=0

  def draw(self):        
     if self.bn_ptn==1:
            pyxel.blt(self.bn_x,self.bn_y,0,  0,0, 16,16,0)
     elif self.bn_ptn==-1:
            pyxel.blt(self.bn_x,self.bn_y,0,  16,0, 16,16,0)
     else:
         pyxel.blt(self.bn_x,self.bn_y,0,   0,0,  16,16,0)

class Anime:
    screen_width=256
    screen_hight=196
    def __init__(self):
        pyxel.init(Anime.screen_width,Anime.screen_hight,title="piixelman")
        pyxel.load("my_resource.pyxres")
        Pixelman(self)
        pyxel.run(self.update,self.draw)

    def update(self):
        self.pixelman.update()

    def draw(self):
        pyxel.cls(1)
        self.pixelman.draw()       
        
    

Anime()    