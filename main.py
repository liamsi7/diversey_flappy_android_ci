from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.core.image import Image as CoreImage
from kivy.core.audio import SoundLoader
from math import sin
import os, random

WIDTH, HEIGHT = 480, 720
GRAVITY = 0.45
FLAP_VELOCITY = -8.5
BASE_PIPE_GAP = 170
BASE_PIPE_DISTANCE = 220
BASE_PIPE_SPEED = 3.2
GROUND_HEIGHT = 96
ASSETS_DIR = "assets"
SOUNDS_DIR = "sounds"

def clamp(v, lo, hi): return max(lo, min(hi, v))

def difficulty_params(score: int):
    pipe_speed = BASE_PIPE_SPEED + min(3.0, 0.12 * score)
    pipe_gap = int(max(110, BASE_PIPE_GAP - 2 * score))
    pipe_distance = int(max(150, BASE_PIPE_DISTANCE - 1.5 * score))
    return pipe_speed, pipe_gap, pipe_distance

class SpriteTex:
    def __init__(self, name):
        path = os.path.join(ASSETS_DIR, name)
        self.tex = CoreImage(path).texture if os.path.exists(path) else None

class ProductDef:
    def __init__(self, key, name, sprite, mini, radius=22):
        self.key = key; self.name = name; self.radius = radius
        self.sprite = SpriteTex(sprite); self.mini = SpriteTex(mini)

class PlayerObj:
    def __init__(self, product: ProductDef, x, y):
        self.product = product; self.x=float(x); self.y=float(y)
        self.vy=0.0; self.radius=product.radius
        self.shield_hits=0; self.small_timer=0.0; self.lowg_timer=0.0; self.dash_timer=0.0
    def flap(self): self.vy = FLAP_VELOCITY
    def update(self):
        g = GRAVITY * (0.6 if self.lowg_timer>0 else 1.0)
        self.vy += g; self.y += self.vy
        if self.dash_timer>0: self.x+=6.5; self.dash_timer-=1/60
        else: self.x += (120 - self.x) * 0.1
        self.y = clamp(self.y, self.effective_radius, HEIGHT - GROUND_HEIGHT - self.effective_radius)
        self.x = clamp(self.x, 90, 220)
        if self.small_timer>0: self.small_timer-=1/60
        if self.lowg_timer>0: self.lowg_timer-=1/60
    @property
    def effective_radius(self): return max(10, self.radius-6) if self.small_timer>0 else self.radius
    def rect(self):
        s=self.effective_radius*2
        return (self.x - s/2, self.y - s/2, s, s)

class PipeObj:
    def __init__(self, x, gap):
        self.x=x; self.width=70; self.gap=gap
        minc=80+gap//2; maxc=HEIGHT-GROUND_HEIGHT-80-gap//2
        self.gap_y = random.randint(minc, maxc); self.passed=False
    def update(self, dt, speed): self.x -= speed * dt
    def offscreen(self): return self.x + self.width < 0
    def collides(self, player: PlayerObj):
        px,py=player.x,player.y; r=player.effective_radius-1
        top=(self.x,0,self.width,self.gap_y - self.gap//2)
        bot=(self.x,self.gap_y + self.gap//2,self.width,HEIGHT-GROUND_HEIGHT-(self.gap_y + self.gap//2))
        def circle_rect(cx,cy,cr,rect):
            rx,ry,rw,rh=rect
            cx2=max(rx,min(cx,rx+rw)); cy2=max(ry,min(cy,ry+rh))
            dx=cx-cx2; dy=cy-cy2
            return dx*dx+dy*dy<=cr*cr
        return circle_rect(px,py,r,top) or circle_rect(px,py,r,bot)

class PickupObj:
    def __init__(self, kind, x, y, tex):
        self.kind=kind; self.x=float(x); self.y=float(y); self.tex=tex; self.taken=False
    def update(self, dt, speed):
        self.x -= speed * dt * 0.8
        self.y += sin(self.x/50.0) * 0.3
    def rect(self):
        w=30; return (self.x-w/2, self.y-w/2, w, w)

class GameWidget(Widget):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.size=(WIDTH,HEIGHT)
        self.products=[
            ProductDef("oxivir_five16","Oxivir Five 16","oxivir_five16.png","mini_oxivir_five16.png"),
            ProductDef("oxivir1_wipes","Oxivir 1 Wipes","oxivir1_wipes.png","mini_oxivir1_wipes.png"),
            ProductDef("suma_grill_d9","Suma Grill D9","suma_grill_d9.png","mini_suma_grill_d9.png"),
            ProductDef("taski_mymicro","TASKI MyMicro","taski_mymicro_green.png","mini_taski_mymicro_green.png"),
            ProductDef("water_only_bottle","Water Only Bottle","water_only_bottle.png","mini_water_only_bottle.png"),
        ]
        self.sel=0
        self.player=PlayerObj(self.products[self.sel],120,HEIGHT//2)
        self.pipes=[]; self.pickups=[]
        self.spawn_x=WIDTH+60; self.t=0.0; self.score=0; self.state="menu"
        self.sounds={k: SoundLoader.load(os.path.join(SOUNDS_DIR,f"{k}.wav")) for k in ["flap","point","powerup","gameover"]}
        Clock.schedule_interval(self.update_step, 1/60)

    def splay(self, key):
        s=self.sounds.get(key)
        if s:
            try: s.stop(); s.volume=0.65; s.play()
            except: pass

    def on_touch_down(self, touch):
        if self.state=="menu":
            self.sel=(self.sel+1)%len(self.products)
            self.reset(); self.state="playing"; return True
        if self.state=="playing":
            self.player.flap(); self.splay("flap"); return True
        if self.state=="gameover":
            self.reset(); self.state="playing"; return True
        return super().on_touch_down(touch)

    def reset(self):
        self.pipes=[]; self.pickups=[]; self.score=0
        self.player=PlayerObj(self.products[self.sel],120,HEIGHT//2)

    def update_step(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(135/255,206/255,235/255,1); Rectangle(pos=(0,0), size=(WIDTH,HEIGHT-GROUND_HEIGHT))
            Color(0.9,0.9,0.9,1); Rectangle(pos=(0,HEIGHT-GROUND_HEIGHT), size=(WIDTH,GROUND_HEIGHT))

        if self.state=="menu":
            self.draw_menu(); return

        speed,gap,dist = difficulty_params(self.score)

        if self.state=="playing":
            self.player.update()
            if (not self.pipes) or (self.spawn_x - (self.pipes[-1].x + self.pipes[-1].width) >= dist):
                p=PipeObj(self.spawn_x,gap); self.pipes.append(p)
                if random.random()<0.35:
                    pr=random.choice(self.products)
                    px=self.spawn_x+140; py=p.gap_y+random.randint(-int(gap*0.35), int(gap*0.35))
                    self.pickups.append(PickupObj(pr.key,px,py,pr.mini.tex))
            for p in self.pipes: p.update(1, speed)
            for pu in self.pickups: pu.update(1, speed)
            self.pipes=[p for p in self.pipes if not p.offscreen()]
            self.pickups=[pu for pu in self.pickups if (pu.x+20)>0 and not pu.taken]
            for p in self.pipes:
                if not p.passed and p.x + p.width < self.player.x:
                    p.passed=True; self.score+=1; self.splay("point")
            if any(p.collides(self.player) for p in self.pipes):
                if self.player.shield_hits>0: self.player.shield_hits-=1; self.player.vy=-4
                else: self.splay("gameover"); self.state="gameover"
            if self.player.y >= HEIGHT-GROUND_HEIGHT-self.player.effective_radius-0.5:
                if self.player.shield_hits>0: self.player.shield_hits-=1; self.player.vy=-6
                else: self.splay("gameover"); self.state="gameover"
            if self.player.y <= self.player.effective_radius+0.5 and self.player.vy < -12:
                if self.player.shield_hits>0: self.player.shield_hits-=1; self.player.vy=2
                else: self.splay("gameover"); self.state="gameover"
            prx,pry,ps=self.player.rect()
            for pu in self.pickups:
                rx,ry,rw,rh=pu.rect()
                if (prx<rx+rw and prx+ps>rx and pry<ry+rh and pry+ps>ry):
                    pu.taken=True
                    if pu.kind=="oxivir_five16": self.player.shield_hits=1
                    elif pu.kind=="oxivir1_wipes": self.player.small_timer=5.0
                    elif pu.kind=="suma_grill_d9": self.player.dash_timer=0.35
                    elif pu.kind=="taski_mymicro": self.player.lowg_timer=5.0
                    elif pu.kind=="water_only_bottle": self.score+=3; self.splay("point")
                    self.splay("powerup")

        self.draw_pipes(); self.draw_pickups(); self.draw_player(); self.draw_hud()

    def draw_menu(self):
        from kivy.core.text import Label as CoreLabel
        def text(txt,x,y,fs=28):
            lbl=CoreLabel(text=txt, font_size=fs, color=(0,0,0,1)); lbl.refresh()
            Rectangle(texture=lbl.texture, pos=(x,y), size=lbl.texture.size)
        text("Diversey Flappy (Android)", 40, HEIGHT-140, 34)
        text("Tik om te starten • tik om character te wisselen", 40, HEIGHT-180, 20)
        xs=[WIDTH//2-180, WIDTH//2-90, WIDTH//2, WIDTH//2+90, WIDTH//2+180]; y=HEIGHT//2-40
        for i,pr in enumerate(self.products):
            tex=pr.sprite.tex
            with self.canvas:
                if tex: Rectangle(texture=tex, pos=(xs[i]-32,y-32), size=(64,64))
                else: Color(0.8,0.8,0.8,1); Ellipse(pos=(xs[i]-22,y-22), size=(44,44))

    def draw_pipes(self):
        with self.canvas:
            for p in self.pipes:
                Color(60/255,190/255,120/255,1); Rectangle(pos=(p.x,0), size=(p.width, p.gap_y - p.gap//2))
                Color(40/255,130/255,80/255,1); Rectangle(pos=(p.x, p.gap_y - p.gap//2 - 18), size=(p.width, 18))
                Color(60/255,190/255,120/255,1); Rectangle(pos=(p.x, p.gap_y + p.gap//2), size=(p.width, HEIGHT-GROUND_HEIGHT-(p.gap_y + p.gap//2)))
                Color(40/255,130/255,80/255,1); Rectangle(pos=(p.x, p.gap_y + p.gap//2), size=(p.width, 18))

    def draw_pickups(self):
        with self.canvas:
            for pu in self.pickups:
                if pu.taken: continue
                if pu.tex: Rectangle(texture=pu.tex, pos=(pu.x-18, pu.y-18), size=(36,36))
                else: Color(1,1,0,1); Ellipse(pos=(pu.x-14, pu.y-14), size=(28,28))

    def draw_player(self):
        pr=self.player.product; tex=pr.sprite.tex; x,y=self.player.x,self.player.y; r=self.player.effective_radius
        with self.canvas:
            if tex: Rectangle(texture=tex, pos=(x-(r+4), y-(r+4)), size=((r+4)*2, (r+4)*2))
            else: Color(0.9,0.9,0.9,1); Ellipse(pos=(x-r,y-r), size=(r*2,r*2))
            if self.player.shield_hits>0: Color(1,1,0.7,1); Line(circle=(x,y,r+8), width=1.8)

    def draw_hud(self):
        from kivy.core.text import Label as CoreLabel
        lbl=CoreLabel(text=f"Score: {self.score}", font_size=24, color=(0,0,0,1)); lbl.refresh()
        Rectangle(texture=lbl.texture, pos=(10, HEIGHT-34), size=lbl.texture.size)

class DiverseyApp(App):
    def build(self):
        self.title="Diversey Flappy (Android)"
        return GameWidget()

if __name__=="__main__":
    DiverseyApp().run()
