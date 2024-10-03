import tkinter as tk

class Player:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.sy = 0
    self.sx = 0
    
  def tick(self):
    self.x += self.sx
    self.y += self.sy
    
    self.sx *= 0.85
    self.sy += 1
    self.draw()
  def draw(self):
    canvas.create_rectangle(self.x,self.y,
                            self.x+32,self.y+32,
                            fill ="red")

def loop():
  canvas.delete("all")
  player.tick()
  root.after(20, loop)

root = tk.Tk()
root.title("game")
root.geometry("720x480")

canvas = tk.Canvas(root,width = 720, 
                   height = 480, 
                   bg ="lightblue")
canvas.pack()

player = Player()

if __name__ == "main":
  loop()
  root.mainloop()
