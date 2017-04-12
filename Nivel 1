import tkinter

# Crea la ventana y la asocia a la variable v
v = tkinter.Tk()

presiono = False
x = None
i = 0
j = 0
i1 = 0
j1 = 0
posxMinivan1=100
posyMinivan1=100
posxMinivan2=10
posyMinivan2=10

def derecha():
    """
    """
    global presiono,x,i,j
    canvas.delete(x)
    i = i + 10
    #x = canvas.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
    x = canvas.create_image(350+i,350+j,image=filename)

def izquierda():
    """
    """
    global presiono,x,i,j
    canvas.delete(x)
    i = i - 10
    #x = canvas.create_polygon(100+i,100+j,100+i,200+j,200+i,200+j,200+i,100+j,outline="black",fill="orange")
    x = canvas.create_image(350+i,350+j,image=filename2)




def key(event):
    """
    """
    global x,i,j,y,i1,j1
    tecla = repr(event.char)
    print(tecla)
    if(tecla == "'d'"):
        if(i < 10):
            canvas.delete(x)
            i = i + 10
            x = canvas.create_image(350+i,350+j,image=carro)
        else:
            canvas.delete(x)
            x = canvas.create_image(350+i,350+j,image=choqueizq)            
    if(tecla == "'a'"):
        if(i > -140):
            canvas.delete(x)
            i = i - 10
            x = canvas.create_image(350+i,350+j,image=carro)
        else:
            canvas.delete(x)
            x = canvas.create_image(350+i,350+j,image=choqueder)

    
    if(tecla == "'w'"):
        if(i1 < 500):
            canvas.delete(y)
            j1 = j1 + 10
            y = canvas.create_image(320+i1,-500+j1,image=fondoMov)
        else:
            canvas.delete(y)
            i1 = -100
            y = canvas.create_image(320+i1,-500+j1,image=fondoMov) 


def movMinivan():
    """
    """
    global posxMinivan1,posyMinivan1,canvas,p,v,posyMinivan2,posxMinivan2
    i=0
    if(i<250):
        canvas.move(minivan1,0,1)
        canvas.move(minivan2,0,1)        
        i=i+1
        posxMinivan1 = posxMinivan1 + 1
        posyMinivan1 = posyMinivan1 + 1
        posxMinivan2 = posxMinivan2 + 1
        posyMinivan2 = posyMinivan2 + 1
        if(posxMinivan1 <= posxMinivan2 and posxMinivan2 <= posxMinivan1 + 50 and posyMinivan1 <= posyMinivan2 and posyMinivan2 <= posyMinivan1 + 50):
            print("crash")
        else:
            v.after(10,movMinivan)

def movMinivan1():
    """
    """
    global posxMinivan1,posyMinivan1,canvas,p,v,posyMinivan2,posxMinivan2
    i=0
    if(i<250):
        canvas.move(minivan1,0,1)
        canvas.move(minivan2,0,1)        
        i=i+1
        posxMinivan1 = posxMinivan1 + 1
        posyMinivan1 = posyMinivan1 + 1
        posxMinivan2 = posxMinivan2 + 1
        posyMinivan2 = posyMinivan2 + 1
        if(posxMinivan1 <= posxMinivan2 and posxMinivan2 <= posxMinivan1 + 50 and posyMinivan1 <= posyMinivan2 and posyMinivan2 <= posyMinivan1 + 50):
            print("crash")
        else:
            v.after(10,movMinivan)
        




# Crea los widgets
b1 = tkinter.Button(v,text="->",command=derecha)
c = tkinter.Label(v,text="Programa William")
b2 = tkinter.Button(v,text="<-",command=izquierda)
canvas = tkinter.Canvas(v, width=640, height=425)

# Liga el evento key al canvas
canvas.bind("<Key>", key)

# Pone el foco en el canvas
canvas.focus_set()

# Empaqueta (muestra) los widgets
c.pack()
b1.pack()
b2.pack()
canvas.pack()
#movimientoCalle()

# Carga una imagen
carro = tkinter.PhotoImage(file="img\carro.png")

minivan = tkinter.PhotoImage(file="img\minivan.png")
"""
runner = tkinter.PhotoImage(file="img\runne.png")

fighter = tkinter.PhotoImage(file="img\fighter.png")

vida = tkinter.PhotoImage(file="img\vida.png")

camion = tkinter.PhotoImage(file="img\camion.png")
"""
choqueder = tkinter.PhotoImage(file="img\carroder.png")

choqueizq = tkinter.PhotoImage(file="img\carroizq.png")

explosion = tkinter.PhotoImage(file="img\explosion.png")


fondoMov = tkinter.PhotoImage(file="nivel1.png")

fondo = tkinter.PhotoImage(file="a.png")



#---------------------------------------------

canvas.create_image(320, 212.5, image=fondo)

x = canvas.create_image(350,350,image=carro)

y = canvas.create_image(320, -500, image=fondoMov)

minivan1 = canvas.create_image(250,-100,image=minivan)

minivan2 = canvas.create_image(350,-200,image=minivan)

movMinivan()

"""
x2 = canvas.create_image(350,350,image=runner)

x3 = canvas.create_image(350,350,image=fighter)

x4 = canvas.create_image(350,350,image=vida)

x5 = canvas.create_image(350,350,image=camion)
"""






# Ciclo para escuchar los eventos
v.mainloop()
