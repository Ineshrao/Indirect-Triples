from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
import code

def btn_clicked():
	
    exp = T2.get("1.0", "end-1c")

    text1,text2=code.IndirectTriple(exp)

    T.delete('1.0',"end")
    T.insert('1.0', text1)    

    T3.delete('1.0',"end")
    T3.insert('1.0', text2)  

    


window = Tk()

window.title("Indirect Triples")

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
T = scrolledtext.ScrolledText(window,wrap = WORD,width = 30,height = 11,font = ("Consolas",15))
T3 = scrolledtext.ScrolledText(window,wrap = WORD,width = 30,height = 11,font = ("Consolas",15))
T2 = Text(window, height = 1, width = 32,font = ("Consolas",16))
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 314.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 415, y = 165,
    width = 230,
    height = 122)
T.grid(column = 0, pady = 10, padx = 10)
# Placing cursor in the text area
T.pack()
T.place(x=192,y=294)

T3.grid(column = 0, pady = 10, padx = 10)
# Placing cursor in the text area
T3.pack()
T3.place(x=550,y=294)

T2.pack()
T2.place(x=470,y=121)
T2.insert(END, '')


window.resizable(False, False)
window.mainloop()
