from tkinter import Tk, Canvas
from math import sin, cos, radians, atan, degrees
from random import randint  as  ri

state = "Menu"
mx,my,mp=0,0,False
esize = 0
st = state


class Player:
    def __init__(self):
        self.x = 360
        self.y = 240
        self.sx = 0
        self.sy = 0
        self.px = 0
        self.py = 0
        self.st = 0
        self.dir = 0
        self.life = 50
        self.health = 50
        self.control_up = "up"
        self.control_down = "down"
        self.control_right = "right"
        self.control_left = "left"
        self.control_right = "right"
        self.control_shoot = "space"
        self.heldec = 0
        self.aa = 0

    def event(self, event, event_type):
        if event_type == "P":
            match event.keysym.lower():
                case self.control_up:
                    self.py = 0.5
                case self.control_down:
                    self.py = -0.25
                case self.control_right:
                    if state == "Play PvC":
                        self.px = -1.5
                    else:
                        self.px = -1
                case self.control_left:
                    if state == "Play PvC":
                        self.px = 1.5
                    else:
                        self.px = 1
                case self.control_shoot:
                    if self.st == 0:
                        bullets.append(Bullet(self.x, self.y, self.dir))
                    self.st += 1
                    
        if event_type == "R":
            match event.keysym.lower():
                case self.control_up:
                    self.py = 0
                case self.control_down:
                    self.py = 0
                case self.control_right:
                    self.px = 0
                case self.control_left:
                    self.px = 0
                case self.control_shoot:
                    self.st = 0

    
    def tick(self,ptype):
        if self.heldec:
            self.dir += 90 * self.aa
        
        self.x += self.sy * sin(radians(self.dir))
        self.y += self.sy * cos(radians(self.dir))
        self.dir += self.sx
        
        self.sx += self.px
        self.sy += self.py

        self.health += (self.life - self.health) / 6
        
        self.sx *= 0.75
        self.sy *= 0.85

        if self.x < 10:
            self.x = 10

        if self.y < 10:
            self.y = 10
            
        if self.x > 710:
            self.x = 710

        if self.y > 470:
            self.y = 470

        if ptype == "C2":
            try:
                if int(self.health) - (self.life) > 1:
                    self.sy += -2.5
                    self.aa = 1
                    self.heldec = 1
                else:
                    self.sy *= 0.8
                    self.heldec = 0   
                a =  atan( (self.x - player.x) / (self.y - player.y ))
                if abs(self.x - player.x) < 128:
                    if abs(self.y - player.y) < 128:
                        self.heldec = 1
                        self.py = -0.5
                        if self.aa == 0:
                            self.aa = ri(-1,1)
                    else:
                        self.aa = 0
                        self.py = 1
                else:
                    self.py = 0.5
                if 0 - (self.y - player.y ) < 0:
                    a += 135
                self.dir += (degrees(a) - self.dir)
                if abs(self.dir - degrees(a)) < 3:
                        
                    self.st += 1
                    if self.st > 16:
                        bullets.append(Bullet(self.x, self.y, self.dir))
                        self.st = 0
                else:
                    self.py = 0

            except:... 
        self.draw()
        
    def draw(self):
        d = radians(self.dir)
        
        sd = sin(d)
        cd = cos(d)
        
        x,y = self.x, self.y
        
        y -= 25
        x -= 25

        canvas.create_line(x - 1,y,x + 51, y, width = 8)
        canvas.create_line(x,y,x + self.health , y, width = 6, fill = "green")

        x,y = self.x, self.y

        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill = "#d9bd6a", outline = "#d9bd6a")
        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill = "#222222", outline = "#222222")
        
        canvas.create_line(x + 9 *  cd, y  - 9 *  sd, x + 25 * sd, y + 25 * cd, fill = "#b3912d", width = 3)
        canvas.create_line(x - 9 *  cd, y  + 9 *  sd, x + 25 * sd, y + 25 * cd, fill = "#b3912d", width = 3)
        
        canvas.create_line( x + 25 * sd, y + 25 * cd, x + 31 * sd , y + 31 * cd, fill = "black", width = 3)

        canvas.create_text(360,16,text = "use ⇦⇕⇨ keys to move around, space to shoot for player 1 \n use wasd keys to move around, f to shoot for player 2 ", font = ("terminal", 11, "bold"), fill = "red")


class Bullet:
    def __init__(self, x, y, dire):
        self.x = x
        self.y = y

        d = radians(dire)

        self.sx = sin(d)
        self.sy = cos(d)
        
        self.x += self.sx * 32
        self.y += self.sy * 32
        
        self.sx *= 8
        self.sy *= 8

    def draw(self):
        self.x += self.sx
        self.y += self.sy

        canvas.create_oval(self.x, self.y, self.x + 4, self.y + 4, fill = "yellow")


def loop():

    if player.life < 1:
        canvas.delete("all")
        canvas.create_text(360, 240, text = "Player 2 won,\n press R to restart", font = ("terminal", 20))
        canvas.create_text(362, 242, text = "Player 2 won,\n press R to restart", font = ("terminal", 20), fill = "grey")

    elif player2.life < 1:
        canvas.delete("all")
        canvas.create_text(360, 240, text = "Player 1 won,\n press R to restart", font = ("terminal", 20))
        canvas.create_text(362, 242, text = "Player 1 won,\n press R to restart", font = ("terminal", 20), fill = "grey")
        
    else:
        canvas.delete("all")
        match state:
            case "Play PvP":
                player.tick("P1")
                player2.tick("P2")
                del_list = []
                all_id = []
                if bullets.__len__() != 0:
                    for i,b in enumerate(bullets):
                        b.draw()
                        if b.x > 720:
                            del_list.append(i)
                            break
                        if b.x < 0:
                            del_list.append(i)
                            break
                        if b.y > 480:
                            del_list.append(i)
                            break
                        if b.y < 0:
                            del_list.append(i)
                            break
                        if abs(player.x - b.x) < 10 and abs(player.y - b.y) < 10:
                            player.life -= 5
                            del_list.append(i)
                            break
                        if abs(player2.x - b.x) < 10 and abs(player2.y - b.y) < 10:
                            player2.life -= 5
                            del_list.append(i)
                            break
                        all_id.append((b.x, b.y, i))
                        
                        for a in all_id:
                            x,y,ia = a[0], a[1], a[2]
                            if ia == i:
                                continue
                            if abs(x - b.x) < 8 and abs(y - b.y) < 8:
                                del_list.append(i)
                                del_list.append(ia)
                                break
                        
                                    
                    for i in del_list:
                        del bullets[i]

            case "Play PvC":
                player.tick("P1")
                player2.tick("C2")
                del_list = []
                all_id = []
                if bullets.__len__() != 0:
                    for i,b in enumerate(bullets):
                        b.draw()
                        if b.x > 720:
                            del_list.append(i)
                            break
                        if b.x < 0:
                            del_list.append(i)
                            break
                        if b.y > 480:
                            del_list.append(i)
                            break
                        if b.y < 0:
                            del_list.append(i)
                            break
                        if abs(player.x - b.x) < 10 and abs(player.y - b.y) < 10:
                            player.life -= 5
                            del_list.append(i)
                            break
                        if abs(player2.x - b.x) < 10 and abs(player2.y - b.y) < 10:
                            player2.life -= 5
                            del_list.append(i)
                            break
                        all_id.append((b.x, b.y, i))
                        
                        for a in all_id:
                            x,y,ia = a[0], a[1], a[2]
                            if ia == i:
                                continue
                            if abs(x - b.x) < 8 and abs(y - b.y) < 8:
                                del_list.append(i)
                                del_list.append(ia)
                                break
                        
                                    
                    for i in del_list:
                        del bullets[i]

            case "SubMenu":  
                x,y = 360,150
                xw,yw = 120,50

                if abs(x - mx) < xw / 2:
                    if abs(y - my) < yw / 2:
                        if mp:
                            global st
                            st = "Play PvP"
                            initPvP()
                            set_mp(False)

                canvas.create_rectangle(x - xw / 2, y - yw / 2, x + xw / 2, y + yw / 2,fill = "#0000ff", outline = "black", width = 4)
                
                canvas.create_text(x, y, text = "Play PvP", font = ("Courier", 18,"bold"))

                
                x,y = 360,300
                xw,yw = 120,50

                if abs(x - mx) < xw / 2:
                    if abs(y - my) < yw / 2:
                        if mp:
                            st = "Play PvC"
                            initPvC()
                            set_mp(False)
                
                canvas.create_rectangle(x - xw / 2, y - yw / 2, x + xw / 2, y + yw / 2,fill = "#0000ff", outline = "black", width = 4)
                
                canvas.create_text(x, y, text = "Play PvC", font = ("Courier", 18,"bold"))

            case "Menu":
                global esize
                x,y = 360,150
                xw,yw = 200,100

                if abs(x - mx) < xw / 2:
                    if abs(y - my) < yw / 2:
                        esize += (20 - esize) / 9
                        if mp:
                            st = "SubMenu"
                            set_mp(False)
                else:
                    esize += (0 - esize) / 9

                xw += esize
                yw += esize
                
                canvas.create_rectangle(x - xw / 2, y - yw / 2, x + xw / 2, y + yw / 2,fill = "#0000ff", outline = "black", width = 9)
                
                canvas.create_text(x, y, text = "Play 🎮", font = ("Courier", 24,"bold"))
                
                canvas.create_text(x, y + 120, text = "This is a game made by Rishal 👨🏻‍💻\n  this a 2p(🤼/👥)‍Game\n    you can also play with 🤖(robot/computer)", font = ("Courier", 20))
    set_state(st)
                
    root.after(15, loop)

def set_state(st):
    global state
    
    state = st

def set_mp(smp):
    global mp
    
    mp = smp

def event(e, etype):
    global mx,my,mp
    player.event(e, etype)
    if state == "Play PvP":
        player2.event(e, etype)

    mx,my = e.x, e.y
    
    mp = True if etype == "MP" else False
    
    if etype == "P":
        if e.keysym.lower() == "r":
            global st
            initPvP()
            st = "SubMenu"
            set_state("SubMenu")

def initPvP():
    global player, player2, bullets
    
    bullets = []

    player = Player()

    player.dir = 90
    player.x = 30

    player2 = Player()

    player2.dir = -90
    player2.x = 690

    player2.control_up = "w"
    player2.control_down = "s"
    player2.control_left = "a"
    player2.control_right = "d"
    player2.control_shoot = "f"

def initPvC():
    global player, player2, bullets
    
    bullets = []

    player = Player()

    player.dir = 100
    player.x = 30

    player2 = Player()
    player2.y -= 64

root = Tk()
root.title("Shooting Game")
root.geometry("720x480")
root.resizable(False, False)

canvas = Canvas(root, width = 720, height = 480, bg = "#555555")

canvas.pack()

bullets = None

player = None

player2 = None

initPvP()

loop()

root.bind("<KeyPress>", lambda ev: event(ev,"P"))
root.bind("<KeyRelease>", lambda ev: event(ev,"R"))

root.bind("<ButtonPress>", lambda ev: event(ev,"MP"))
root.bind("<ButtonRelease>", lambda ev: event(ev,"MR"))
root.bind("<Motion>", lambda ev: event(ev,"M"))


root.mainloop()
