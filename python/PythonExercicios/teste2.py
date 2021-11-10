'''from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(3)
    le
    left(3.5)
    if abs(pos()) < 1:
        break
end_fill()
done()'''


from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()

menu_inicial.title("Primeira Aplicação")

menu_inicial.geometry("500x250+750+400")

menu_inicial.resizable(True, True) #1 e 0 dão o mesmo resultado

#menu_inicial.minsize(500, 250)
#menu_inicial.maxsize(700, 400)

menu_inicial.mainloop()