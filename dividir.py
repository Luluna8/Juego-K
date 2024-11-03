from PIL import Image
import os
def dividir_guardar(ruta_imagen, carpeta_destino, division_de_columnas):
    #cARGA IMAGEN

    with Image.open(ruta_imagen) as img:
        ancho, alto = img.size


        # Calcular el numero de divisiones por fila
        tamaño_cuadrado = ancho // division_de_columnas
        divisiones_por_fila = alto // tamaño_cuadrado

        # Crear la carpeta de destino si no existe
        os.makedirs(carpeta_destino, exist_ok=True)

        # Dividir y guardar cada tile
        contador = 0
        for i in range(divisiones_por_fila):
            for j in range(division_de_columnas):
                # Coordenadas del cuadrado
                izquierda = j * tamaño_cuadrado
                superior = i * tamaño_cuadrado
                derecha = izquierda + tamaño_cuadrado
                inferior = superior + tamaño_cuadrado

                # Cortar y guardar el cuadrado
                cuadrado = img.crop((izquierda, superior, derecha, inferior))
                nombre_archivo = f"tile_{contador}.png"
                cuadrado.save(os.path.join(carpeta_destino, nombre_archivo))
                contador += 1


    img.close()
dividir_guardar("C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/tiles/Dungeon_Tileset.png","C:/Users/Lucia/Desktop/Python/pygame/Juego/asset/tiles",10)

