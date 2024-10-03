import tkinter as tk

def loop():
  canvas.delete("all")
  root.after(20, loop)

root = tk.Tk()
root.title("game")
root.geometry("720x480")

canvas = tk.Canvas(root,width = 720, 
                   height = 480, 
                   bg ="lightblue")
canvas.pack()


if __name__ == "main":
  loop()
  root.mainloop()
