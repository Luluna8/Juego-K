import pygame
import constantes
import math
import random

class Weadpoon():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.image_original = image
        self.angulo = 0
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.image.get_rect()
        self.dispara = False
        self.ultimo_disparo = pygame.time.get_ticks()


    def update(self, personaje):
        disparo_cooldown = constantes.COOLDOWN_BALAS
        bala = None
        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width/2
            self.rotar_arma(False)
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width/2
            self.rotar_arma(True)

            # Mover pistola con mouse y clicks
        mouse_pos = pygame.mouse.get_pos()
        diferencia_x = mouse_pos[0] - self.forma.centerx
        diferencia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(diferencia_y, diferencia_x))

        # Disparar si se hace clic y si ha pasado el cooldown
        if pygame.mouse.get_pressed()[0] and not self.dispara and (
                pygame.time.get_ticks() - self.ultimo_disparo >= disparo_cooldown):
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.dispara = True
            self.ultimo_disparo = pygame.time.get_ticks()
            #Reseteo clicl
        if pygame.mouse.get_pressed()[0] == False:
            self.dispara = False
        return bala
       #coliciones

    def dibujar(self, interfaz):
        self.image = pygame.transform.rotate(self.image, self.angulo)
        interfaz.blit(self.image, self.forma)

    def rotar_arma(self, rotar):
        if rotar == True:
            image_flip = pygame.transform.flip(self.image_original, True, False)
            self.image = pygame.transform.rotate(image_flip, self.angulo)
        else:
            image_flip = pygame.transform.flip(self.image_original, False, False)
            self.image = pygame.transform.rotate(image_flip, self.angulo)

class Bullet(pygame.sprite.Sprite):
  def __init__(self, image, x, y, angle):
      pygame.sprite.Sprite.__init__(self)
      self.imagen_original = image
      self.angulo = angle
      self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)
      # Velocidad de bala
      self.delta_x = math.cos(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA
      self.delta_y = -math.sin(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA

  def update(self, lista_enemigos,obstaculos_tiles):
      daño = 0
      pos_daño = None
      self.rect.x = self.rect.x + self.delta_x
      self.rect.y = self.rect.y + self.delta_y
      if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.bottom < 0 or self.rect.top > constantes.ALTO_VENTANA:
          self.kill()

      #Colisiones
      for enemigo in lista_enemigos:
          if enemigo.forma.colliderect(self.rect):
              daño = 15 + random.randint(-7,7)
              pos_daño = enemigo.forma
              enemigo.energia = enemigo.energia - daño
              self.kill()
              break
      for obs in obstaculos_tiles:
          if obs[1].colliderect(self.rect):
              self.kill()
              break

      return daño, pos_daño

  def dibujar(self, interfaz):
      interfaz.blit(self.image, (self.rect.centerx, self.rect.centery - int(self.image.get_height())))

