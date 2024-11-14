import pygame
import constantes
from personaje import Personaje
from weadpoon import Weadpoon
from texto import DamageText
import os
from items import Item
from mundog import Mundo
import csv



#Funciones
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen
# Función para contar elementos en un directorio
def contar_elemento(directorio):
    return len(os.listdir(directorio))

# Función para listar el contenido de un directorio
def nombre_carpeta(directorio):
    return os.listdir(directorio)



pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Juego")
#variable
posicion_pantalla = [0, 0]

nivel = 1

ruta_base = os.path.dirname(os.path.abspath(__file__))
def cargar_ruta(*path):
    return  os.path.join(ruta_base,*path)

#Fuentes
font =pygame.font.Font(cargar_ruta("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//font//brackeys_platformer_assets//PixelOperator8-Bold.ttf"), 25)
font_game_over = pygame.font.Font(cargar_ruta("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//font//brackeys_platformer_assets//PixelOperator8-Bold.ttf"), 70)
font_reinicio= pygame.font.Font(cargar_ruta("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//font//brackeys_platformer_assets//PixelOperator8-Bold.ttf"), 15)
font_inicio = pygame.font.Font(cargar_ruta("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//font//brackeys_platformer_assets//PixelOperator8-Bold.ttf"), 25)
font_salir = pygame.font.Font(cargar_ruta("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//font//brackeys_platformer_assets//PixelOperator8-Bold.ttf"), 25)



game_over_text= font_game_over.render("Game over",True,constantes.BLANCO)
text_botom_reinicio = font_reinicio.render("Reiniciar", True,constantes.NEGRO)
boton_jugar = pygame.Rect(constantes.ANCHO_VENTANA / 2 -100, constantes.ALTO_VENTANA /2 - 50,200,50)
boton_salir = pygame.Rect(constantes.ANCHO_VENTANA / 2 -100, constantes.ALTO_VENTANA /2 + 50,200,50)
texto_boton_jugar =font_inicio.render("Jugar",True,constantes.NEGRO)
texto_boton_salir = font_salir.render("Salir",True,constantes.BLANCO)

def pantalla_inicio():
    ventana.fill(constantes.MORADO)
    dibujar_score("Warrior",font_salir,constantes.BLANCO,
                  constantes.ANCHO_VENTANA / 2 - 200,
                  constantes.ALTO_VENTANA / 2 - 200)
    pygame.draw.rect(ventana,constantes.AMARILLO,boton_jugar)
    pygame.draw.rect(ventana,constantes.ROJO,boton_salir)
    ventana.blit(texto_boton_jugar,(boton_jugar.x + 50, boton_jugar.y+10))
    ventana.blit(texto_boton_salir,(boton_salir.x + 50, boton_salir.y+10))
    pygame.display.update()
def pantalla_final():
    ventana.fill(constantes.NEGRO)
    dibujar_score("GANASTE", font_salir, constantes.BLANCO,
                  constantes.ANCHO_VENTANA / 2 - 200,
                  constantes.ALTO_VENTANA / 2 - 200)





#importar imagenes
#energia
corazon_vacio = pygame.image.load( os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//items//vida3.png")).convert_alpha()
corazon_vacio = escalar_img(corazon_vacio, constantes.SCALA_CORAZON)
corazon_medio = pygame.image.load( os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//items//vida2.png")).convert_alpha()
corazon_medio = escalar_img(corazon_medio, constantes.SCALA_CORAZON)
corazon_lleno = pygame.image.load( os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//items//vida1.png")).convert_alpha()
corazon_lleno = escalar_img(corazon_lleno, constantes.SCALA_CORAZON)






animaciones =[]
for i in range(3):
    img = pygame.image.load(os.path.join(f"C://Users//Lucia//Desktop//Python//pygame//Juego//asset//player//je{i}.png"))
    img = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)

#Enemigos
directorio_enemigos = os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//enemy")
tipo_enemigos = nombre_carpeta(directorio_enemigos)
animaciones_enemigos = []
for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = os.path.join(f"C://Users//Lucia//Desktop//Python//pygame//Juego//asset//enemy//{eni}")
    num_animaciones = contar_elemento(ruta_temp)

    for i in range(num_animaciones):
        img_enemigo = pygame.image.load( os.path.join(f"{ruta_temp}//{eni}_{i+1}.png"))
        img_enemigo = escalar_img(img_enemigo, constantes.SCALA_ENEMIGO)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)
print(animaciones_enemigos)

#Carga del mundo
tile_list = []
for x in range (constantes.TILE_TYPE):
    tile_image = pygame.image.load(os.path.join(f"C://Users//Lucia//Desktop//Python//pygame//Juego//asset//tiles//tile_{x}.png"))
    tile_image = pygame.transform.scale(tile_image,(constantes.TILET_SIZE,constantes.TILET_SIZE))
    tile_list.append(tile_image)




#items
posion_verde = pygame.image.load(os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//item//pocion//pocion1.png"))
posion_verde = escalar_img(posion_verde, 1)

coin_image =[]
ruta_imag = os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//item//moneda")
num_coin_img = contar_elemento(ruta_imag)
for i in range(num_coin_img):
    img = pygame.image.load( os.path.join(f"C://Users//Lucia//Desktop//Python//pygame//Juego//asset//item//moneda//moneda_{i+1}.png"))
    img= escalar_img(img,1)
    coin_image.append(img)
item_imagenes = [coin_image, [posion_verde]]

def dibujar_score(texto, fuente, color, x, y):
    img =fuente.render(texto, True, color)
    ventana.blit(img, (x,y))

def vida_jugador():
    c_mitad_dibujado = False
    for i in range(4):
        if jugador.energia >= ((i+1)*25):
            ventana.blit(corazon_lleno, (5+i*50,5))
        elif jugador.energia % 25  >0 and c_mitad_dibujado == False:
            ventana.blit(corazon_medio, (5+i*50,5))
            c_mitad_dibujado = True
        else:
            ventana.blit(corazon_vacio, (5+i*50,5))

def resetear_mundo():
    grupo_items.empty()
    grupo_damage_text.empty()
    grupo_balas.empty()
    data = []
    for fila in range(constantes.FILAS):
        filas = [2] * constantes.COLUMNAS
        data.append(filas)
    return  data

world_data=[]
for fila in range(constantes.FILAS):
    filas = [5] * constantes.FILAS
    world_data.append(filas)

# Cargar el nivel
with open("C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/niveles/nivel_1.csv", newline="" )as  csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y]= int(columna)


world = Mundo()
world.process_data(world_data, tile_list,item_imagenes, animaciones_enemigos)


def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.BLANCO, (x*constantes.TILE_SIZE, 0),(x*constantes.TILE_SIZE,constantes.ALTO_VENTANA))
        pygame.draw.line(ventana, constantes.BLANCO, (0, x*constantes.TILE_SIZE),(constantes.ANCHO_VENTANA, x*constantes.TILE_SIZE))

#Personaje
jugador = Personaje(50, 50, animaciones, 20, 1)

#Enemigo

lista_enemigos = []
for ene in world.lista_enemigo:
    lista_enemigos.append(ene)


#Balas
imagen_bala = pygame.image.load(os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//armas//bala2.png"))
imagen_bala = escalar_img(imagen_bala, constantes.SCALA_ARMA)

#Arma

image_pistola = pygame.image.load(os.path.join("C://Users//Lucia//Desktop//Python//pygame//Juego//asset//armas//gun.png"))
image_pistola = escalar_img(image_pistola, constantes.SCALA_ARMA)
pistola = Weadpoon(image_pistola, imagen_bala)



#Grupo de sprites

grupo_damage_text = pygame.sprite.Group()

grupo_balas = pygame.sprite.Group()

grupo_items = pygame.sprite.Group()

for item in world.lista_item:
    grupo_items.add(item)







# Definir variables
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

pygame.mixer.music.load(os.path.join("C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/sound/time_for_adventure.mp3"))
pygame.mixer.music.play(-1)
somido_disparo = pygame.mixer.Sound(os.path.join("C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/sound/disparo2.mp3"))


boton_reinicio = pygame.Rect(constantes.ANCHO_VENTANA/2-100,
                                         constantes.ALTO_VENTANA/2 +100,200,40)

mostrar_inicio = True
run = True
reloj = pygame.time.Clock()

while run:
    if mostrar_inicio == True:
        pantalla_inicio()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.collidepoint(event.pos):
                        mostrar_inicio = False
                    if boton_salir.collidepoint(event.pos):
                        run = False

    else:
        # 60fps
        reloj.tick(constantes.FPS)
        ventana.fill(constantes.MORADO)



        if jugador.vivo == True:




         delta_x = 0
         delta_y = 0

         if mover_derecha == True:
             delta_x = constantes.VELOCIDAD
         if mover_izquierda == True:
             delta_x = -constantes.VELOCIDAD
         if mover_arriba == True:
             delta_y = -constantes.VELOCIDAD
         if mover_abajo == True:
             delta_y = constantes.VELOCIDAD

        # Mover al jugador
         posicion_pantalla, nivel_completado= jugador.movimiento(delta_x, delta_y,world.obstaculo_tiles,world.exit_tile)



         world.update(posicion_pantalla)

        #Animacion llamado
         jugador.update()


        #Animacion enemigo
         for ene in lista_enemigos:
             ene.update()




        #Arma llamado
         bala = pistola.update(jugador)
         if bala:
             grupo_balas.add(bala)
             somido_disparo.play()

         for bala in grupo_balas:
             damage, pos_damage = bala.update(lista_enemigos, world.obstaculo_tiles)
             if damage !=0:
                 damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(damage), font, constantes.ROJO)
                 grupo_damage_text.add(damage_text)

       #actualizar daño
         grupo_damage_text.update(posicion_pantalla)


       #Actualiza el item
         grupo_items.update(posicion_pantalla,jugador)

        if nivel_completado == True:
            if nivel < constantes.NIVEL_MAXIMO:
             nivel +=1
             world_data = resetear_mundo()
            # Cargar el nivel
             with open(f"C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/niveles/nivel_{nivel}.csv", newline="") as csvfile:
                 reader = csv.reader(csvfile, delimiter=",")
                 for x, fila in enumerate(reader):
                     for y, columna in enumerate(fila):
                         world_data[x][y] = int(columna)

             world = Mundo()
             world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigos)
             jugador.actualizar_coordenada(constantes.COORDENADAS[str(nivel)])
            #Enemigo

             lista_enemigos = []
             for ene in world.lista_enemigo:
                 lista_enemigos.append(ene)
            #Item
             for item in world.lista_item:
                 grupo_items.add(item)
            

         # Dibujar mundo
        world.draw(ventana)

         # Dibujar arma
        pistola.dibujar(ventana)




        # Dibujar la juagador
        jugador.dibujar(ventana)

        #Dibujar enemigpo
        for ene in lista_enemigos:
            if ene.energia == 0:
                lista_enemigos.remove(ene)
            if ene.energia >0:
                ene.enemigos(jugador,world.obstaculo_tiles,posicion_pantalla,world.exit_tile)
                ene.dibujar(ventana)




        #dibujar balas
        for bala in grupo_balas:
            bala.dibujar(ventana)

        #dibujo corazon
        vida_jugador()


        #dibujar el texto
        grupo_damage_text.draw(ventana)
        dibujar_score(f"Score: {jugador.score}",font, (255,255,0),600,5)

        #nivel
        dibujar_score(f"Nivel: "+ str(nivel),font,constantes.BLANCO,constantes.ANCHO_VENTANA/ 2,5)
        #Dibujar items
        grupo_items.draw(ventana)


        if jugador.vivo == False:
            ventana.fill(constantes.ROJO_OBSCURO)
            text_rect = game_over_text.get_rect(center=(constantes.ANCHO_VENTANA / 2, constantes.ALTO_VENTANA/2))

            ventana.blit(game_over_text,text_rect)

            pygame.draw.rect(ventana, constantes.AMARILLO,boton_reinicio)
            ventana.blit(text_botom_reinicio,(boton_reinicio.x + 40, boton_reinicio.y + 10))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_a:
                    mover_izquierda = True

                if event.key == pygame.K_d:
                    mover_derecha = True

                if event.key == pygame.K_w:
                    mover_arriba = True

                if event.key == pygame.K_s:
                    mover_abajo = True
                if event.key == pygame.K_e:
                    if world.Cambiar_puerta(jugador,tile_list):
                        print("Puerta cambiada")



            if event.type == pygame.KEYUP:

                if event.key == pygame.K_a:
                    mover_izquierda = False

                if event.key == pygame.K_d:
                    mover_derecha = False

                if event.key == pygame.K_w:
                    mover_arriba = False

                if event.key == pygame.K_s:
                    mover_abajo = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_reinicio.collidepoint(event.pos) and not jugador.vivo:
                    jugador.vivo= True
                    jugador.energia = 100
                    jugador.score = 0
                    nivel = 1
                    world_data = resetear_mundo()
                    with open(f"C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/niveles/nivel_{nivel}.csv",
                              newline="") as csvfile:
                        reader = csv.reader(csvfile, delimiter=",")
                        for x, fila in enumerate(reader):
                            for y, columna in enumerate(fila):
                                world_data[x][y] = int(columna)
                    world = Mundo()
                    world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigos)
                    jugador.actualizar_coordenada(constantes.COORDENADAS[str(nivel)])
                    # Enemigo

                    lista_enemigos = []
                    for ene in world.lista_enemigo:
                        lista_enemigos.append(ene)
                    # Item
                    for item in world.lista_item:
                        grupo_items.add(item)





        pygame.display.update()

pygame.quit()
