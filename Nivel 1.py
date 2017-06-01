import tkinter
from tkinter import messagebox
import time
import random

v1 = tkinter.Tk() #Nombre de la variable de la ventana principal
v1.title("Road Fighter - WILLIAM AGUIRRE ZAPATA - WTechnology.co") #Titulo de la ventana
v1.geometry('800x460') #Tamaño de la ventana


#----------------------Variables-------------------
x=None
z=None
presiono = False
i = 0
j = 0
i1 = 0
j1 = 0

posxal=random.randint(240,380) #Posicion aleatoria en JUGADOR 1
posxal2=random.randint(510,655) #Posicion aleatoria en JUGADOR 2

c=0
c2=0

contbarra=6 #El contador de la vida del jugador 1
contbarra2=6 #El contador de la vida del jugador 2

cMini1=0
cMini2=0

cRunner1=0
cRunner2=0

cFighter1=0
cFighter2=0

aaa=0
bbb=0
ccc=0
ddd=0

Texto1="                         Aprende a jugar ROAD FIGHTER \n \n Selecciona cualquier NIVEL de dificultad \n \n Los controles para el JUGADOR 1: \n Tecla A = carro se mueve a la izquierda \n Tecla D = carro se mueve a la derecha \n \n Los controles para el JUGADOR 2: \n Tecla J = carro se mueve a la izquierda \n Tecla L = carro se mueve a la derecha \n \n Para Guardar el juego con la tecla SPACE \n \n Para cerrar presionar la tecla ESC \n \n La idea del juego es llegar a la meta antes de que se acabe la gasolina esquivando el tráfico y dificultades de la carretera \n \n                                      ¡MUCHA SUERTE! " 

#--------------------MONTAR IMAGENES------------------------------------------
fondo1 = tkinter.PhotoImage(file="img\menu.png")
fondoMulti1 = tkinter.PhotoImage(file="img\menu1.png")
carro = tkinter.PhotoImage(file="img\carro.png")
carro2 = tkinter.PhotoImage(file="img\carro2.png")
minivan = tkinter.PhotoImage(file="img\minivan.png")
runner = tkinter.PhotoImage(file="runner.png")
fighter = tkinter.PhotoImage(file="fighter.png")
vida = tkinter.PhotoImage(file="vida.png")
hueco = tkinter.PhotoImage(file="img\hueco.png")
choqueder = tkinter.PhotoImage(file="img\carroder.png")
choqueder2 = tkinter.PhotoImage(file="img\carroder2.png")
choqueizq = tkinter.PhotoImage(file="img\carroizq.png")
choqueizq2 = tkinter.PhotoImage(file="img\carroizq2.png")
explosion = tkinter.PhotoImage(file="img\explosion.png")
fondoMov = tkinter.PhotoImage(file="nivel1.png")
gasolina=tkinter.PhotoImage(file="img\gasolina.png")
barra=tkinter.PhotoImage(file="barra.png")
ganador01=tkinter.PhotoImage(file="img\ganador1.png")
ganador02=tkinter.PhotoImage(file="img\ganador2.png")

#-------------------CARGAR IMAGENES-----------------------------------------
photo = tkinter.Label(v1,image=fondo1, width=800, height=460).place(x=0,y=0)

#------------Caja de Texto para Variable de Jugador 1--------------------------
jugador1=tkinter.StringVar()
NomJugador1=tkinter.Entry(v1,bd=4,fg="white",bg="black",textvariable=jugador1).place(x=200,y=305)


#------------Caja de Texto para Variable de Jugador 1--------------------------
jugador2=tkinter.StringVar()
NomJugador2=tkinter.Entry(v1,bd=4,fg="white",bg="black",textvariable=jugador2).place(x=200,y=375)



#-----------------------------FUNCIONES-------------------------------------

def manual():
    """
    Descripción: Funcion que llama a mensaje sobre las instrucciones del juego.
    """
    messagebox.showinfo("Instrucciones de Juego",Texto1)

#------------------------ENEMIGOS DE JUGADOR1--------------------------------

def movMinivan():
    """
    Descripción: Función que llama un carro MiniVan el cual solo se mueve en eje y y aparece aleatoriamente desde la parte de arriba y desaparece en la parte de abajo.
    """
    global x,contbarra,cMini1
    contadormini1=0
    aleatorio=random.randint(aaa,bbb)
    
    if(c<30):
        canvas1.move(minivan1,0,velocidadMini)
        cMini1 = cMini1 + 1
    if(canvas1.coords(minivan1)[1]>=500):
        cMini1=0
        canvas1.move(minivan1,aleatorio-canvas1.coords(minivan1)[0],-canvas1.coords(minivan1)[1])  
    
    if(contadormini1<250):
        
        contadormini1 = contadormini1 + 1
        posx1 = canvas1.coords(x)[0]
        posy1 = canvas1.coords(x)[1]
        posx2 = canvas1.coords(minivan1)[0]
        posy2 = canvas1.coords(minivan1)[1]
        
        if(posx1>=posx2 and posx1<=posx2+20 and posy1>=posy2 and posy1<=posy2+30 or(posx1+20>=posx2 and posx1+20<=posx2+20 and posy1>=posy2 and posy1<=posy2+30) ):
            print("Choque Minivan JUGADOR 1")
            l=x
            x = canvas1.create_image(canvas1.coords(l)[0],canvas1.coords(l)[1],image=choqueizq)
            canvas1.delete(l)
            mermarGasolina1()
            contbarra=contbarra-1
            canvas1.move(minivan1,aleatorio-canvas1.coords(minivan1)[0],-canvas1.coords(z)[1])
            v3.after(10,movMinivan)
            
        else:
            v3.after(10,movMinivan)


def movHueco():
    """
    Descripción: Función que llama un hueco en la Carretera el cual solo se mueve en eje y del jugador 1 y aparece aleatoriamente desde la parte de arriba y desaparece en la parte de abajo.
    """
    global x,contbarra,cHueco,contadorhueco1
    
    cHueco=0
    contadorhueco1=0
    aleatorio=random.randint(aaa,bbb)
    
    if(cHueco<30):
        canvas1.move(hueco1,0,velocidadHueco)
        cHueco = cHueco + 1
    if(canvas1.coords(hueco1)[1]>=500):
        cHueco=0
        canvas1.move(hueco1,aleatorio-canvas1.coords(hueco1)[0],-canvas1.coords(hueco1)[1])  
    
    if(contadorhueco1<250):
        
        contadorhueco1 = contadorhueco1 + 1
        posx1 = canvas1.coords(x)[0]
        posy1 = canvas1.coords(x)[1]
        posx2 = canvas1.coords(hueco1)[0]
        posy2 = canvas1.coords(hueco1)[1]
        
        if(posx1>=posx2 and posx1<=posx2+20 and posy1>=posy2 and posy1<=posy2+30 or(posx1+20>=posx2 and posx1+20<=posx2+20 and posy1>=posy2 and posy1<=posy2+30) ):
            print("Choque Hueco JUGADOR 1")
            l=x
            x = canvas1.create_image(canvas1.coords(l)[0],canvas1.coords(l)[1],image=choqueder)
            canvas1.delete(l)
            mermarGasolina1()
            contbarra=contbarra-1
            canvas1.move(hueco1,aleatorio-canvas1.coords(hueco1)[0],-canvas1.coords(z)[1])
            v3.after(10,movHueco)
            
        else:
            v3.after(10,movHueco)


def movFighter():
    """
    Descripción: Función que llama un carro Fighter el cual solo se mueve en eje y con forme en la posicion del eje x del jugador 1 y aparece aleatoriamente desde la parte de arriba y desaparece en la parte de abajo.
    """    
    global contadorFighter,x,contbarra
    
    contadorFighter=0
    aleatoriofighter=random.randint(aaa,bbb)
    
    if(canvas1.coords(x)[0]<canvas1.coords(fight)[0]):
        canvas1.move(fight,-anguloFighter,velocidadFighter)
    elif(canvas1.coords(x)[0]>canvas1.coords(fight)[0]):
        canvas1.move(fight,anguloFighter,velocidadFighter)
    else:
        canvas1.move(fight,0,velocidadFighter)
    if(canvas1.coords(x)[1]==canvas1.coords(fight)[1]):
        canvas1.move(fight,aleatoriofighter-canvas1.coords(fight)[0],-canvas1.coords(fight)[1])
                
    if(contadorFighter<250):
        
        contadorFighter = contadorFighter + 1
        posx11 = canvas1.coords(x)[0]
        posy11 = canvas1.coords(x)[1]
        posx22 = canvas1.coords(fight)[0]
        posy22 = canvas1.coords(fight)[1]
        
        if(posx11>=posx22 and posx11<=posx22+20 and posy11>=posy22 and posy11<=posy22+30 or(posx11+20>=posx22 and posx11+20<=posx22+20 and posy11>=posy22 and posy11<=posy22+30) ):
            print("Choque Fighter JUGADOR 1")
            l=x
            x = canvas1.create_image(canvas1.coords(l)[0],canvas1.coords(l)[1],image=choqueizq)
            canvas1.delete(l)
            mermarGasolina1()
            contbarra=contbarra-1
            canvas1.move(fight,aleatoriofighter-canvas1.coords(fight)[0],-canvas1.coords(fight)[1])
            v3.after(10,movFighter)
            canvas1.move(y,0,-canvas1.coords(y)[1])
        else:
            contadorFighter=0
            v3.after(10,movFighter)



def carroVida():
    
    global x,contbarra,cVida,contadorvida
    
    cVida=0
    contadorvida=0
    aleatorio=random.randint(aaa,bbb)
    
    if(cVida<30):
        canvas1.move(vida1,0,velocidadVida)
        cVida = cVida + 1
        
    if(canvas1.coords(vida1)[1]>=1000):
        cVida=0
        canvas1.move(vida1,aleatorio-canvas1.coords(vida1)[0],-canvas1.coords(vida1)[1])

    if(contadorvida<250):
        
        contadorvida = contadorvida + 1
        posx1 = canvas1.coords(x)[0]
        posy1 = canvas1.coords(x)[1]
        posx2 = canvas1.coords(vida1)[0]
        posy2 = canvas1.coords(vida1)[1]
        
        if(posx1>=posx2 and posx1<=posx2+20 and posy1>=posy2 and posy1<=posy2+30 or(posx1+20>=posx2 and posx1+20<=posx2+20 and posy1>=posy2 and posy1<=posy2+30) ):
            print("Conseguiste Vida JUGADOR 1")
            if(contbarra<6):
                aumentoGasolina1()
                contbarra=contbarra+1
            canvas1.move(vida1,aleatorio-canvas1.coords(vida1)[0],-canvas1.coords(z)[1])
            v3.after(10,carroVida)
            
        else:
            v3.after(10,carroVida)




def movRunner():
    pass





#-------------------------------------------------------


#------------------ENEMIGOS JUGADOR 2--------------------

def movMinivan2():
    """
    Descripción: Función que llama un hueco en la Carretera el cual solo se mueve en eje y del jugador 2 y aparece aleatoriamente desde la parte de arriba y desaparece en la parte de abajo.
    """
    global z,contbarra2,cMini2
    cMini2=0
    contadormini2=0
    aleatorio=random.randint(ccc,ddd)
    
    if(cMini2<30):
        canvas1.move(minivan2,0,velocidadMini)
        cMini2 = cMini2 + 1
    if(canvas1.coords(minivan2)[1]>=500):
        cMini2=0
        canvas1.move(minivan2,aleatorio-canvas1.coords(minivan2)[0],-canvas1.coords(minivan2)[1])  
    
    if(contadormini2<250):
        
        contadormini2 = contadormini2 + 1
        posx1 = canvas1.coords(z)[0]
        posy1 = canvas1.coords(z)[1]
        posx2 = canvas1.coords(minivan2)[0]
        posy2 = canvas1.coords(minivan2)[1]
        
        if(posx1>=posx2 and posx1<=posx2+20 and posy1>=posy2 and posy1<=posy2+30 or(posx1+20>=posx2 and posx1+20<=posx2+20 and posy1>=posy2 and posy1<=posy2+30) ):
            print("Choque Minivan JUGADOR 2")
            l=z
            z = canvas1.create_image(canvas1.coords(l)[0],canvas1.coords(l)[1],image=choqueizq2)
            canvas1.delete(l)
            mermarGasolina2()
            contbarra2=contbarra2-1
            canvas1.move(minivan2,aleatorio-canvas1.coords(minivan2)[0],-canvas1.coords(z)[1])
            v3.after(10,movMinivan2)
            
        else:
            v3.after(10,movMinivan2)




def carroVida2():
    global z,contbarra2,cVida2,contadorvida2
    
    cVida2=0
    contadorvida2=0
    aleatorio=random.randint(ccc,ddd)
    
    if(cVida2<30):
        canvas1.move(vida2,0,velocidadVida)
        cVida2 = cVida2 + 1
        
    if(canvas1.coords(vida2)[1]>=1000):
        cVida2=0
        canvas1.move(vida2,aleatorio-canvas1.coords(vida2)[0],-canvas1.coords(vida2)[1])

    if(contadorvida2<250):
        
        contadorvida2 = contadorvida2 + 1
        posx1 = canvas1.coords(z)[0]
        posy1 = canvas1.coords(z)[1]
        posx2 = canvas1.coords(vida2)[0]
        posy2 = canvas1.coords(vida2)[1]
        
        if(posx1>=posx2 and posx1<=posx2+20 and posy1>=posy2 and posy1<=posy2+30 or(posx1+20>=posx2 and posx1+20<=posx2+20 and posy1>=posy2 and posy1<=posy2+30) ):
            print("Conseguiste Vida JUGADOR 2")
            if(contbarra2<6):
                aumentoGasolina2()
                contbarra2=contbarra2+1
            canvas1.move(vida2,aleatorio-canvas1.coords(vida2)[0],-canvas1.coords(z)[1])
            v3.after(10,carroVida2)
            
        else:
            v3.after(10,carroVida2)


def movHueco2():
    global z,contbarra2,cHueco2,contadorhueco2
    
    cHueco2=0
    contadorhueco2=0
    aleatorio=random.randint(ccc,ddd)
    
    if(cHueco2<30):
        canvas1.move(hueco2,0,velocidadHueco)
        cHueco2 = cHueco2 + 1
    if(canvas1.coords(hueco2)[1]>=500):
        cHueco2=0
        canvas1.move(hueco2,aleatorio-canvas1.coords(hueco2)[0],-canvas1.coords(hueco2)[1])  
    
    if(contadorhueco2<250):
        
        contadorhueco2 = contadorhueco2 + 1
        posx1 = canvas1.coords(z)[0]
        posy1 = canvas1.coords(z)[1]
        posx2 = canvas1.coords(hueco2)[0]
        posy2 = canvas1.coords(hueco2)[1]
        
        if(posx1>=posx2 and posx1<=posx2+20 and posy1>=posy2 and posy1<=posy2+30 or(posx1+20>=posx2 and posx1+20<=posx2+20 and posy1>=posy2 and posy1<=posy2+30) ):
            print("Choque Hueco JUGADOR 2")
            l=z
            z = canvas1.create_image(canvas1.coords(l)[0],canvas1.coords(l)[1],image=choqueder2)
            canvas1.delete(l)
            mermarGasolina2()
            contbarra2=contbarra2-1
            canvas1.move(hueco2,aleatorio-canvas1.coords(hueco2)[0],-canvas1.coords(z)[1])
            v3.after(10,movHueco2)
            
        else:
            v3.after(10,movHueco2)


def movFighter2():
    
    global contadorFighter2,z,contbarra2
    
    contadorFighter2=0
    aleatoriofighter=random.randint(ccc,ddd)
    
    if(canvas1.coords(z)[0]<canvas1.coords(fight2)[0]):
        canvas1.move(fight2,-anguloFighter,velocidadFighter)
    elif(canvas1.coords(z)[0]>canvas1.coords(fight2)[0]):
        canvas1.move(fight2,anguloFighter,velocidadFighter)
    else:
        canvas1.move(fight2,0,velocidadFighter)
    if(canvas1.coords(z)[1]==canvas1.coords(fight2)[1]):
        canvas1.move(fight2,aleatoriofighter-canvas1.coords(fight2)[0],-canvas1.coords(fight2)[1])
                
    if(contadorFighter2<250):
        
        contadorFighter2 = contadorFighter2 + 1
        posx11 = canvas1.coords(z)[0]
        posy11 = canvas1.coords(z)[1]
        posx22 = canvas1.coords(fight2)[0]
        posy22 = canvas1.coords(fight2)[1]
        
        if(posx11>=posx22 and posx11<=posx22+20 and posy11>=posy22 and posy11<=posy22+30 or(posx11+20>=posx22 and posx11+20<=posx22+20 and posy11>=posy22 and posy11<=posy22+30) ):
            print("Choque Fighter JUGADOR 2")
            l=z
            z = canvas1.create_image(canvas1.coords(l)[0],canvas1.coords(l)[1],image=choqueizq2)
            canvas1.delete(l)
            mermarGasolina2()
            contbarra2=contbarra2-1
            canvas1.move(fight2,aleatoriofighter-canvas1.coords(fight2)[0],-canvas1.coords(fight2)[1])
            v3.after(10,movFighter2)
            canvas1.move(y1,0,-canvas1.coords(y1)[1])
        else:
            contadorFighter2=0
            v3.after(10,movFighter2)


#----------------MERMAR GASOLINA---------------------------

def mermarGasolina1():
    global contbarra
    if(contbarra==6):
        canvas1.delete(barra11)
    if(contbarra==5):
        canvas1.delete(barra12)
    if(contbarra==4):
        canvas1.delete(barra13)
    if(contbarra==3):
        canvas1.delete(barra14)
    if(contbarra==2):
        canvas1.delete(barra15)
    if(contbarra==1):
        canvas1.delete(barra16)
        gameOver1()
    if(contbarra==0):
        pass

def mermarGasolina2():
    global contbarra2
    if(contbarra2==6):
        canvas1.delete(barra21)
    if(contbarra2==5):
        canvas1.delete(barra22)
    if(contbarra2==4):
        canvas1.delete(barra23)
    if(contbarra2==3):
        canvas1.delete(barra24)
    if(contbarra2==2):
        canvas1.delete(barra25)
    if(contbarra2==1):
        canvas1.delete(barra26)
        gameOver2()
    if(contbarra2==0):
        pass




#------------AUMENTAR GASOLINA---------------------
    
def aumentoGasolina1():
    global contbarra,barra11,barra12,barra13,barra14,barra15
    if(contbarra==5):
        barra11=canvas1.create_image(830,75, image=barra)
    if(contbarra==4):
        barra12=canvas1.create_image(830,90, image=barra)
    if(contbarra==3):
        barra13=canvas1.create_image(830,105, image=barra)
    if(contbarra==2):
        barra14=canvas1.create_image(830,120, image=barra)
    if(contbarra==1):
        barra15=canvas1.create_image(830,135, image=barra)

def aumentoGasolina2():
    global contbarra2,barra21,barra22,barra23,barra24,barra25
    if(contbarra2==5):
        barra21=canvas1.create_image(950,75, image=barra)
    if(contbarra2==4):
        barra22=canvas1.create_image(950,90, image=barra)
    if(contbarra2==3):
        barra23=canvas1.create_image(950,105, image=barra)
    if(contbarra2==2):
        barra24=canvas1.create_image(950,120, image=barra)
    if(contbarra2==1):
        barra25=canvas1.create_image(950,135, image=barra)



#------------MENSAJE DE GAME OVER Y GANADOR------------

def gameOver1():
    ganador1=canvas1.create_image(440,212.5, image=ganador01)


        
    
def gameOver2():
    ganador2=canvas1.create_image(440,212.5, image=ganador02)

    
def cerrar():
    global contbarra,contbarra2
    contbarra=6
    contbarra2=6
    v3.destroy()
    v1.destroy()
    
    
    






#----------------TECLAS NIVEL1 ---------------
h = [] 
def keyup(e):
    global h
    #print(e.keycode)
    if(e.keycode in h):
        h.pop(h.index(e.keycode))
        
def keydown(e):
    global h
    if not e.keycode in h:
        h.append(e.keycode)
        
def keyJuego():
    """
    Descripcion: funcion que permite al jugador con las teclas 'd' 'a' y 'l' 'j' mover el carro de ambos jugadores
    Entradas: entra por parametro como evento del main
    Salida: cambia la posicion del carro del jugador dando efecto del movimiento
    """
    global h,x,i,j,y,i1,j1,z
    if(68 in h):
        if(i<30):
            canvas1.delete(x)
            i = i + 3
            x = canvas1.create_image(350+i,350+j,image=carro)
        else:
            canvas1.delete(x)
            x = canvas1.create_image(350+i,350+j,image=choqueizq) 
    if(65 in h):
        if(i > -111):
            canvas1.delete(x)
            i = i - 3
            x = canvas1.create_image(350+i,350+j,image=carro)
        else:
            canvas1.delete(x)
            x = canvas1.create_image(350+i,350+j,image=choqueder)
    if(76 in h):
        if(i1 < 30):
            canvas1.delete(z)
            i1 = i1 + 3
            z = canvas1.create_image(620+i1,350+j1,image=carro2)
        else:
            canvas1.delete(z)
            z = canvas1.create_image(620+i1,350+j1,image=choqueizq2)
    if(74 in h):
        if(i1 > -120):
             canvas1.delete(z)
             i1 = i1 - 3
             z = canvas1.create_image(620+i1,350+j,image=carro2)
        else:
             canvas1.delete(z)
             z = canvas1.create_image(620+i1,350+j1,image=choqueder2)
     
    if(32 in h):
         guardarPartida()

    if(27 in h):
        cerrar()
    
        
    v3.after(10,keyJuego)


#----------------MOVIMIENTO DEL FONDO ------------
    
def movFondo1Multi1():
    """
    """
    i=0
    if(i<5):
        canvas1.move(y,0,velocidadMapa)
        i=i+1
    if(canvas1.coords(y)[1]>=2500):
        i=0
        canvas1.move(y,0,-canvas1.coords(y)[1])
    v3.after(10,movFondo1Multi1)



def movFondo1Multi2():
    """
    """
    i=0
    if(i<5):
        canvas1.move(y1,0,velocidadMapa)
        i=i+1
    if(canvas1.coords(y1)[1]>=2500):
        i=0
        canvas1.move(y1,0,-canvas1.coords(y)[1])        
    v3.after(10,movFondo1Multi2)



#----------VENTANAS DEL MENU--------------------- 


def ventanaNivel1Multi():
    global aaa,bbb,ccc,ddd,velocidadMapa,velocidadMini,velocidadHueco,velocidadFighter,anguloFighter,velocidadVida,velocidadRunner,x,y,canvas1,v3,z,y1,fight,fight2,minivan1,minivan2,runner1,runner2,hueco1,hueco2,vida1,vida2,barra11,barra12,barra13,barra14,barra15,barra16,barra21,barra22,barra23,barra24,barra25,barra26
    
    v3 =tkinter.Toplevel(v1)
    canvas1 = tkinter.Canvas(v3, width=1025, height=425)#Crea Widgets
    v3.title("Nivel 1 Road Fighter") 

    canvas1.focus_set()# Pone el foco en el canvas
    canvas1.pack()#Empaqueta el canvas
    keyJuego()
    canvas1.bind("<KeyPress>", keydown)#Liga el evento key al canvas
    canvas1.bind("<KeyRelease>", keyup)

    canvas1.create_image(512.5, 212.5, image=fondoMulti1) #FONDO ESTÁTICO
    x = canvas1.create_image(350+i,350+j,image=carro) # CARRO DEL JUGADOR 1
    z = canvas1.create_image(620,350,image=carro2) # CARRO DEL JUGADOR 2
    y = canvas1.create_image(345, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    y1 = canvas1.create_image(615, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    Gasolina=canvas1.create_image(790,120, image=gasolina) #GASOLINA DE LA PANTALLA


    #----Variables de velocidad, etc...-----------
    
    aaa=240 #Variables del rango de la carretera en x Jugador 1
    bbb=380 #Variables del rango de la carretera en x Jugador 1
    
    ccc=510 #Variables del rango de la carretera en x Jugador 2
    ddd=655 #Variables del rango de la carretera en x Jugador 2
    
    velocidadMapa=2
    
    velocidadMini=3
    
    velocidadHueco=velocidadMapa
    
    velocidadFighter=2
    
    anguloFighter=0.5
    
    velocidadVida=3

    velocidadRunner=3






    #-----VIDA EN BARRA DEL JUGADOR 1------------------
    barra11=canvas1.create_image(830,75, image=barra)
    barra12=canvas1.create_image(830,90, image=barra)
    barra13=canvas1.create_image(830,105, image=barra)
    barra14=canvas1.create_image(830,120, image=barra)
    barra15=canvas1.create_image(830,135, image=barra)
    barra16=canvas1.create_image(830,150, image=barra)
    
    #-----VIDA EN BARRA DEL JUGADOR 2------------------
    barra21=canvas1.create_image(950,75, image=barra)
    barra22=canvas1.create_image(950,90, image=barra)
    barra23=canvas1.create_image(950,105, image=barra)
    barra24=canvas1.create_image(950,120, image=barra)
    barra25=canvas1.create_image(950,135, image=barra)
    barra26=canvas1.create_image(950,150, image=barra)
    

    
    
    TextoJugador1=tkinter.Label(v3,text=jugador1.get(),fg="white",bg="black",font=("Arial",13)).place(x=130,y=10)
    TextoJugador2=tkinter.Label(v3,text=jugador2.get(),fg="white",bg="black",font=("Arial",13)).place(x=405,y=10)

    Jugador1=tkinter.Label(v3,text=jugador1.get(),fg="white",bg="black",font=("Arial",13)).place(x=790,y=10)
    Jugador2=tkinter.Label(v3,text=jugador2.get(),fg="white",bg="black",font=("Arial",13)).place(x=900,y=10)


    movFondo1Multi1()
    movFondo1Multi2()

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan1 = canvas1.create_image(posxal,-100,image=minivan)
    vida1 = canvas1.create_image(posxal,-1000,image=vida)
    runner1 = canvas1.create_image(posxal,-150,image=runner)
    fight = canvas1.create_image(posxal,-550,image=fighter)
    hueco1= canvas1.create_image(posxal,-300,image=hueco)

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan2 = canvas1.create_image(posxal2,-100,image=minivan)
    vida2 = canvas1.create_image(posxal2,-1000,image=vida)
    runner2 = canvas1.create_image(posxal2,-150,image=runner)
    fight2 = canvas1.create_image(posxal2,-550,image=fighter)
    hueco2= canvas1.create_image(posxal2,-300,image=hueco)
    
    #----------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 1------------
    
    movMinivan()
    #movRunner()
    movFighter()
    carroVida()
    movHueco()

    #---------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 2------------

    movMinivan2()
    #movRunner2()
    movFighter2()
    carroVida2()
    movHueco2()

    
    v1.iconify()



def ventanaNivel2Multi():
    global aaa,bbb,ccc,ddd,velocidadMapa,velocidadMini,velocidadHueco,velocidadFighter,anguloFighter,velocidadVida,velocidadRunner,x,y,canvas1,v3,z,y1,fight,fight2,minivan1,minivan2,runner1,runner2,hueco1,hueco2,vida1,vida2,barra11,barra12,barra13,barra14,barra15,barra16,barra21,barra22,barra23,barra24,barra25,barra26
    
    v3 =tkinter.Toplevel(v1)
    canvas1 = tkinter.Canvas(v3, width=1025, height=425)#Crea Widgets
    v3.title("Nivel 2 Road Fighter") 
    canvas1.focus_set()# Pone el foco en el canvas
    canvas1.pack()#Empaqueta el canvas
    keyJuego()
    canvas1.bind("<KeyPress>", keydown)#Liga el evento key al canvas
    canvas1.bind("<KeyRelease>", keyup)

    canvas1.create_image(512.5, 212.5, image=fondoMulti1) #FONDO ESTÁTICO
    x = canvas1.create_image(350+i,350+j,image=carro) # CARRO DEL JUGADOR 1
    z = canvas1.create_image(620,350,image=carro2) # CARRO DEL JUGADOR 2
    y = canvas1.create_image(345, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    y1 = canvas1.create_image(615, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    Gasolina=canvas1.create_image(790,120, image=gasolina) #GASOLINA DE LA PANTALLA


    #----Variables de velocidad, etc...-----------
    
    aaa=240 #Variables del rango de la carretera en x Jugador 1
    bbb=380 #Variables del rango de la carretera en x Jugador 1
    
    ccc=510 #Variables del rango de la carretera en x Jugador 2
    ddd=655 #Variables del rango de la carretera en x Jugador 2
    
    velocidadMapa=2.5
    
    velocidadMini=3.5
    
    velocidadHueco=velocidadMapa
    
    velocidadFighter=2.5
    
    anguloFighter=1
    
    velocidadVida=3.5

    velocidadRunner=3.5








    #-----VIDA EN BARRA DEL JUGADOR 1------------------
    barra11=canvas1.create_image(830,75, image=barra)
    barra12=canvas1.create_image(830,90, image=barra)
    barra13=canvas1.create_image(830,105, image=barra)
    barra14=canvas1.create_image(830,120, image=barra)
    barra15=canvas1.create_image(830,135, image=barra)
    barra16=canvas1.create_image(830,150, image=barra)
    
    #-----VIDA EN BARRA DEL JUGADOR 2------------------
    barra21=canvas1.create_image(950,75, image=barra)
    barra22=canvas1.create_image(950,90, image=barra)
    barra23=canvas1.create_image(950,105, image=barra)
    barra24=canvas1.create_image(950,120, image=barra)
    barra25=canvas1.create_image(950,135, image=barra)
    barra26=canvas1.create_image(950,150, image=barra)
    

    
    
    TextoJugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=130,y=10)
    TextoJugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=405,y=10)

    Jugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=790,y=10)
    Jugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=900,y=10)


    movFondo1Multi1()
    movFondo1Multi2()

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan1 = canvas1.create_image(posxal,-100,image=minivan)
    vida1 = canvas1.create_image(posxal,-1000,image=vida)
    runner1 = canvas1.create_image(posxal,-150,image=runner)
    fight = canvas1.create_image(posxal,-550,image=fighter)
    hueco1= canvas1.create_image(posxal,-300,image=hueco)

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan2 = canvas1.create_image(posxal2,-100,image=minivan)
    vida2 = canvas1.create_image(posxal2,-1000,image=vida)
    runner2 = canvas1.create_image(posxal2,-150,image=runner)
    fight2 = canvas1.create_image(posxal2,-550,image=fighter)
    hueco2= canvas1.create_image(posxal2,-300,image=hueco)
    
    #----------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 1------------
    
    movMinivan()
    #movRunner()
    movFighter()
    carroVida()
    movHueco()

    #---------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 2------------

    movMinivan2()
    #movRunner2()
    movFighter2()
    carroVida2()
    movHueco2()

    
    v1.iconify()

    





def ventanaNivel3Multi():
    global aaa,bbb,ccc,ddd,velocidadMapa,velocidadMini,velocidadHueco,velocidadFighter,anguloFighter,velocidadVida,velocidadRunner,x,y,canvas1,v3,z,y1,fight,fight2,minivan1,minivan2,runner1,runner2,hueco1,hueco2,vida1,vida2,barra11,barra12,barra13,barra14,barra15,barra16,barra21,barra22,barra23,barra24,barra25,barra26
    
    v3 =tkinter.Toplevel(v1)
    canvas1 = tkinter.Canvas(v3, width=1025, height=425)#Crea Widgets
    v3.title("Nivel 3 Road Fighter") 
    canvas1.focus_set()# Pone el foco en el canvas
    canvas1.pack()#Empaqueta el canvas
    keyJuego()
    canvas1.bind("<KeyPress>", keydown)#Liga el evento key al canvas
    canvas1.bind("<KeyRelease>", keyup)

    canvas1.create_image(512.5, 212.5, image=fondoMulti1) #FONDO ESTÁTICO
    x = canvas1.create_image(350+i,350+j,image=carro) # CARRO DEL JUGADOR 1
    z = canvas1.create_image(620,350,image=carro2) # CARRO DEL JUGADOR 2
    y = canvas1.create_image(345, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    y1 = canvas1.create_image(615, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    Gasolina=canvas1.create_image(790,120, image=gasolina) #GASOLINA DE LA PANTALLA


    #----Variables de velocidad, etc...-----------
    
    aaa=240 #Variables del rango de la carretera en x Jugador 1
    bbb=380 #Variables del rango de la carretera en x Jugador 1
    
    ccc=510 #Variables del rango de la carretera en x Jugador 2
    ddd=655 #Variables del rango de la carretera en x Jugador 2
    
    velocidadMapa=3
    
    velocidadMini=4
    
    velocidadHueco=velocidadMapa
    
    velocidadFighter=3
    
    anguloFighter=1.5
    
    velocidadVida=4

    velocidadRunner=4









    #-----VIDA EN BARRA DEL JUGADOR 1------------------
    barra11=canvas1.create_image(830,75, image=barra)
    barra12=canvas1.create_image(830,90, image=barra)
    barra13=canvas1.create_image(830,105, image=barra)
    barra14=canvas1.create_image(830,120, image=barra)
    barra15=canvas1.create_image(830,135, image=barra)
    barra16=canvas1.create_image(830,150, image=barra)
    
    #-----VIDA EN BARRA DEL JUGADOR 2------------------
    barra21=canvas1.create_image(950,75, image=barra)
    barra22=canvas1.create_image(950,90, image=barra)
    barra23=canvas1.create_image(950,105, image=barra)
    barra24=canvas1.create_image(950,120, image=barra)
    barra25=canvas1.create_image(950,135, image=barra)
    barra26=canvas1.create_image(950,150, image=barra)
    

    
    
    TextoJugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=130,y=10)
    TextoJugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=405,y=10)

    Jugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=790,y=10)
    Jugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=900,y=10)


    movFondo1Multi1()
    movFondo1Multi2()

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan1 = canvas1.create_image(posxal,-100,image=minivan)
    vida1 = canvas1.create_image(posxal,-1000,image=vida)
    runner1 = canvas1.create_image(posxal,-150,image=runner)
    fight = canvas1.create_image(posxal,-550,image=fighter)
    hueco1= canvas1.create_image(posxal,-300,image=hueco)

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan2 = canvas1.create_image(posxal2,-100,image=minivan)
    vida2 = canvas1.create_image(posxal2,-1000,image=vida)
    runner2 = canvas1.create_image(posxal2,-150,image=runner)
    fight2 = canvas1.create_image(posxal2,-550,image=fighter)
    hueco2= canvas1.create_image(posxal2,-300,image=hueco)
    
    #----------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 1------------
    
    movMinivan()
    #movRunner()
    movFighter()
    carroVida()
    movHueco()

    #---------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 2------------

    movMinivan2()
    #movRunner2()
    movFighter2()
    carroVida2()
    movHueco2()

    
    v1.iconify()




def ventanaNivel4Multi():
    global aaa,bbb,ccc,ddd,velocidadMapa,velocidadMini,velocidadHueco,velocidadFighter,anguloFighter,velocidadVida,velocidadRunner,x,y,canvas1,v3,z,y1,fight,fight2,minivan1,minivan2,runner1,runner2,hueco1,hueco2,vida1,vida2,barra11,barra12,barra13,barra14,barra15,barra16,barra21,barra22,barra23,barra24,barra25,barra26
    
    v3 =tkinter.Toplevel(v1)
    canvas1 = tkinter.Canvas(v3, width=1025, height=425)#Crea Widgets
    v3.title("Nivel 4 Road Fighter") 
    canvas1.focus_set()# Pone el foco en el canvas
    canvas1.pack()#Empaqueta el canvas
    keyJuego()
    canvas1.bind("<KeyPress>", keydown)#Liga el evento key al canvas
    canvas1.bind("<KeyRelease>", keyup)

    canvas1.create_image(512.5, 212.5, image=fondoMulti1) #FONDO ESTÁTICO
    x = canvas1.create_image(350+i,350+j,image=carro) # CARRO DEL JUGADOR 1
    z = canvas1.create_image(620,350,image=carro2) # CARRO DEL JUGADOR 2
    y = canvas1.create_image(345, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    y1 = canvas1.create_image(615, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    Gasolina=canvas1.create_image(790,120, image=gasolina) #GASOLINA DE LA PANTALLA


    #----Variables de velocidad, etc...-----------
    
    aaa=240 #Variables del rango de la carretera en x Jugador 1
    bbb=380 #Variables del rango de la carretera en x Jugador 1
    
    ccc=510 #Variables del rango de la carretera en x Jugador 2
    ddd=655 #Variables del rango de la carretera en x Jugador 2
    
    velocidadMapa=3.5
    
    velocidadMini=4.5
    
    velocidadHueco=velocidadMapa
    
    velocidadFighter=3.5
    
    anguloFighter=2
    
    velocidadVida=4.5

    velocidadRunner=4.5






    #-----VIDA EN BARRA DEL JUGADOR 1------------------
    barra11=canvas1.create_image(830,75, image=barra)
    barra12=canvas1.create_image(830,90, image=barra)
    barra13=canvas1.create_image(830,105, image=barra)
    barra14=canvas1.create_image(830,120, image=barra)
    barra15=canvas1.create_image(830,135, image=barra)
    barra16=canvas1.create_image(830,150, image=barra)
    
    #-----VIDA EN BARRA DEL JUGADOR 2------------------
    barra21=canvas1.create_image(950,75, image=barra)
    barra22=canvas1.create_image(950,90, image=barra)
    barra23=canvas1.create_image(950,105, image=barra)
    barra24=canvas1.create_image(950,120, image=barra)
    barra25=canvas1.create_image(950,135, image=barra)
    barra26=canvas1.create_image(950,150, image=barra)
    

    
    
    TextoJugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=130,y=10)
    TextoJugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=405,y=10)

    Jugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=790,y=10)
    Jugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=900,y=10)


    movFondo1Multi1()
    movFondo1Multi2()

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan1 = canvas1.create_image(posxal,-100,image=minivan)
    vida1 = canvas1.create_image(posxal,-1000,image=vida)
    runner1 = canvas1.create_image(posxal,-150,image=runner)
    fight = canvas1.create_image(posxal,-550,image=fighter)
    hueco1= canvas1.create_image(posxal,-300,image=hueco)

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan2 = canvas1.create_image(posxal2,-100,image=minivan)
    vida2 = canvas1.create_image(posxal2,-1000,image=vida)
    runner2 = canvas1.create_image(posxal2,-150,image=runner)
    fight2 = canvas1.create_image(posxal2,-550,image=fighter)
    hueco2= canvas1.create_image(posxal2,-300,image=hueco)
    
    #----------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 1------------
    
    movMinivan()
    #movRunner()
    movFighter()
    carroVida()
    movHueco()

    #---------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 2------------

    movMinivan2()
    #movRunner2()
    movFighter2()
    carroVida2()
    movHueco2()

    
    v1.iconify()




def ventanaNivel5Multi():
    global aaa,bbb,ccc,ddd,velocidadMapa,velocidadMini,velocidadHueco,velocidadFighter,anguloFighter,velocidadVida,velocidadRunner,x,y,canvas1,v3,z,y1,fight,fight2,minivan1,minivan2,runner1,runner2,hueco1,hueco2,vida1,vida2,barra11,barra12,barra13,barra14,barra15,barra16,barra21,barra22,barra23,barra24,barra25,barra26
    
    v3 =tkinter.Toplevel(v1)
    canvas1 = tkinter.Canvas(v3, width=1025, height=425)#Crea Widgets
    v3.title("Nivel 5 Road Fighter") 
    canvas1.focus_set()# Pone el foco en el canvas
    canvas1.pack()#Empaqueta el canvas
    keyJuego()
    canvas1.bind("<KeyPress>", keydown)#Liga el evento key al canvas
    canvas1.bind("<KeyRelease>", keyup)

    canvas1.create_image(512.5, 212.5, image=fondoMulti1) #FONDO ESTÁTICO
    x = canvas1.create_image(350+i,350+j,image=carro) # CARRO DEL JUGADOR 1
    z = canvas1.create_image(620,350,image=carro2) # CARRO DEL JUGADOR 2
    y = canvas1.create_image(345, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    y1 = canvas1.create_image(615, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    Gasolina=canvas1.create_image(790,120, image=gasolina) #GASOLINA DE LA PANTALLA


    #----Variables de velocidad, etc...-----------
    
    aaa=240 #Variables del rango de la carretera en x Jugador 1
    bbb=380 #Variables del rango de la carretera en x Jugador 1
    
    ccc=510 #Variables del rango de la carretera en x Jugador 2
    ddd=655 #Variables del rango de la carretera en x Jugador 2
    
    velocidadMapa=4.5
    
    velocidadMini=5.5
    
    velocidadHueco=velocidadMapa
    
    velocidadFighter=3

    anguloFighter=1
    
    velocidadVida=5.5

    velocidadRunner=5.5






    



    #-----VIDA EN BARRA DEL JUGADOR 1------------------
    barra11=canvas1.create_image(830,75, image=barra)
    barra12=canvas1.create_image(830,90, image=barra)
    barra13=canvas1.create_image(830,105, image=barra)
    barra14=canvas1.create_image(830,120, image=barra)
    barra15=canvas1.create_image(830,135, image=barra)
    barra16=canvas1.create_image(830,150, image=barra)
    
    #-----VIDA EN BARRA DEL JUGADOR 2------------------
    barra21=canvas1.create_image(950,75, image=barra)
    barra22=canvas1.create_image(950,90, image=barra)
    barra23=canvas1.create_image(950,105, image=barra)
    barra24=canvas1.create_image(950,120, image=barra)
    barra25=canvas1.create_image(950,135, image=barra)
    barra26=canvas1.create_image(950,150, image=barra)
    

    
    
    TextoJugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=130,y=10)
    TextoJugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=405,y=10)

    Jugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=790,y=10)
    Jugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=900,y=10)


    movFondo1Multi1()
    movFondo1Multi2()

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan1 = canvas1.create_image(posxal,-100,image=minivan)
    vida1 = canvas1.create_image(posxal,-1000,image=vida)
    runner1 = canvas1.create_image(posxal,-150,image=runner)
    fight = canvas1.create_image(posxal,-550,image=fighter)
    hueco1= canvas1.create_image(posxal,-300,image=hueco)

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan2 = canvas1.create_image(posxal2,-100,image=minivan)
    vida2 = canvas1.create_image(posxal2,-1000,image=vida)
    runner2 = canvas1.create_image(posxal2,-150,image=runner)
    fight2 = canvas1.create_image(posxal2,-550,image=fighter)
    hueco2= canvas1.create_image(posxal2,-300,image=hueco)
    
    #----------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 1------------
    
    movMinivan()
    #movRunner()
    movFighter()
    carroVida()
    movHueco()

    #---------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 2------------

    movMinivan2()
    #movRunner2()
    movFighter2()
    carroVida2()
    movHueco2()

    
    v1.iconify()
















def menuPrincipal():
    otra_ventana = tkinter.Toplevel(v1)
    v1.iconify()


def guardarPartida():
    global contbarra,contbarra2

    archivo = open("guardar.txt", "w")
    
    posicionX=canvas1.coords(x)[0]
    posicionY=canvas1.coords(x)[1]
    
    posicionX2=canvas1.coords(z)[0]
    posicionY2=canvas1.coords(z)[1]

    if(contbarra>0 and contbarra2>0):  
        
            archivo.write(str(posicionX)+"\n")
            archivo.write(str(posicionY)+"\n")
            archivo.write(str(posicionX2)+"\n")
            archivo.write(str(posicionY2)+"\n")
            archivo.write(str(contbarra)+"\n")
            archivo.write(str(contbarra2)+"\n")

    print("Se guardo Correctamente")
    archivo.close()

def cargar():
    global x,z,contbarra,contbarra2,a1,a2,a3,a4,a5,a6
    
    archivo=open("guardar.txt","r")
    
    linea1 = archivo.readline()
    print(linea1)
    
    linea2=archivo.readline()
    print(linea2)

    linea3 = archivo.readline()
    print(linea3)

    linea4=archivo.readline()
    print(linea4)

    linea5 = archivo.readline()
    print(linea5)

    linea6=archivo.readline()
    print(linea6)
    ventadaGuardar()

    a1=canvas1.coords(x)[0]
    a2=canvas1.coords(x)[1]
    a3=canvas1.coords(z)[0]
    a4=canvas1.coords(z)[1]
    contbarra=int(linea5)
    contbarra2=int(linea6)
    
    a1=float(linea1)
    a2=float(linea2)
    a3=float(linea3)
    a4=float(linea4)


    
    archivo.close()


def ventadaGuardar():
    
    global aaa,bbb,ccc,ddd,velocidadMapa,velocidadMini,velocidadHueco,velocidadFighter,anguloFighter,velocidadVida,velocidadRunner,x,y,canvas1,v3,z,y1,fight,fight2,minivan1,minivan2,runner1,runner2,hueco1,hueco2,vida1,vida2,barra11,barra12,barra13,barra14,barra15,barra16,barra21,barra22,barra23,barra24,barra25,barra26
    
    v3 =tkinter.Toplevel(v1)
    canvas1 = tkinter.Canvas(v3, width=1025, height=425)#Crea Widgets

    canvas1.focus_set()# Pone el foco en el canvas
    canvas1.pack()#Empaqueta el canvas
    keyJuego()
    canvas1.bind("<KeyPress>", keydown)#Liga el evento key al canvas
    canvas1.bind("<KeyRelease>", keyup)

    canvas1.create_image(512.5, 212.5, image=fondoMulti1) #FONDO ESTÁTICO
    x = canvas1.create_image(350+i,350+j,image=carro) # CARRO DEL JUGADOR 1
    z = canvas1.create_image(620,350,image=carro2) # CARRO DEL JUGADOR 2
    y = canvas1.create_image(345, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    y1 = canvas1.create_image(615, -2100, image=fondoMov) #FONDO EN MOVIMIENTO JUGADOR1
    Gasolina=canvas1.create_image(790,120, image=gasolina) #GASOLINA DE LA PANTALLA


    #----Variables de velocidad, etc...-----------
    
    aaa=240 #Variables del rango de la carretera en x Jugador 1
    bbb=380 #Variables del rango de la carretera en x Jugador 1
    
    ccc=510 #Variables del rango de la carretera en x Jugador 2
    ddd=655 #Variables del rango de la carretera en x Jugador 2
    
    velocidadMapa=2
    
    velocidadMini=3
    
    velocidadHueco=velocidadMapa
    
    velocidadFighter=2
    
    anguloFighter=0.5
    
    velocidadVida=3

    velocidadRunner=3



    #-----VIDA EN BARRA DEL JUGADOR 1------------------
    
    barra16=canvas1.create_image(830,75, image=barra)

    barra15=canvas1.create_image(830,90, image=barra)

    barra14=canvas1.create_image(830,105, image=barra)

    barra13=canvas1.create_image(830,120, image=barra)

    barra12=canvas1.create_image(830,135, image=barra)

    barra11=canvas1.create_image(830,150, image=barra)

        
    #-----VIDA EN BARRA DEL JUGADOR 2------------------
    barra21=canvas1.create_image(950,75, image=barra)
    barra22=canvas1.create_image(950,90, image=barra)
    barra23=canvas1.create_image(950,105, image=barra)
    barra24=canvas1.create_image(950,120, image=barra)
    barra25=canvas1.create_image(950,135, image=barra)
    barra26=canvas1.create_image(950,150, image=barra)
    

    
    
    TextoJugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=130,y=10)
    TextoJugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=405,y=10)

    Jugador1=tkinter.Label(v3,text=jugador1.get(),font=("Arial",13)).place(x=790,y=10)
    Jugador2=tkinter.Label(v3,text=jugador2.get(),font=("Arial",13)).place(x=900,y=10)


    movFondo1Multi1()
    movFondo1Multi2()

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan1 = canvas1.create_image(posxal,-100,image=minivan)
    vida1 = canvas1.create_image(posxal,-1000,image=vida)
    runner1 = canvas1.create_image(posxal,-150,image=runner)
    fight = canvas1.create_image(posxal,-550,image=fighter)
    hueco1= canvas1.create_image(posxal,-300,image=hueco)

    #----------ENEMIGOS DEL JUGADOR 1---------------------
    
    minivan2 = canvas1.create_image(posxal2,-100,image=minivan)
    vida2 = canvas1.create_image(posxal2,-1000,image=vida)
    runner2 = canvas1.create_image(posxal2,-150,image=runner)
    fight2 = canvas1.create_image(posxal2,-550,image=fighter)
    hueco2= canvas1.create_image(posxal2,-300,image=hueco)
    
    #----------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 1------------
    
    movMinivan()
    #movRunner()
    movFighter()
    carroVida()
    movHueco()

    #---------PONER A CORRER LOS ENEMIGOS DEL JUGADOR 2------------

    movMinivan2()
    #movRunner2()
    movFighter2()
    carroVida2()
    movHueco2()

    
    v1.iconify()


#-------------------BOTONES Y WIDGETS---------------------------------------
Btnivel1Multi1 = tkinter.Button(v1, text="Nivel 1",fg="black",bg="yellow",font=("Arial",13), command=ventanaNivel1Multi).place(x=680,y=150)
Btnivel1Multi2 = tkinter.Button(v1, text="Nivel 2",fg="black",bg="yellow",font=("Arial",13), command=ventanaNivel2Multi).place(x=680,y=200)
Btnivel1Multi3 = tkinter.Button(v1, text="Nivel 3",fg="black",bg="yellow",font=("Arial",13), command=ventanaNivel3Multi).place(x=680,y=250)
Btnivel1Multi4 = tkinter.Button(v1, text="Nivel 4",fg="black",bg="yellow",font=("Arial",13), command=ventanaNivel4Multi).place(x=680,y=300)
Btnivel1Multi5 = tkinter.Button(v1, text="Nivel 5",fg="black",bg="yellow",font=("Arial",13), command=ventanaNivel5Multi).place(x=680,y=350)
BtNavegador = tkinter.Button(v1, text="Manual de Usuario",fg="white",bg="black", command=manual).place(x=150,y=430)
BtNavegador = tkinter.Button(v1, text="Instrucciones de Juego", fg="white",bg="black",command=manual).place(x=500,y=430)
Btcargar = tkinter.Button(v1, text="Cargar Juego Guardado", fg="white",bg="black",command=cargar).place(x=400,y=5)
  



v1.mainloop()


