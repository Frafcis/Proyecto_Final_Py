##Sprites
import pygame
import random

from Proyecto_final import mons

class Mon(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.idle_sprites = []
		self.animation = True
		self.digitize(0)

		self.current_sprite = 0
		self.image = self.idle_sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]
  
		#Stats!
		self.attack = 0
		self.hp = 0
  
		#Health
		self.care_mistakes = 0
		self.hunger = 0

	def update(self,speed,anim_id):
		if self.animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.idle_sprites):
				self.current_sprite = 0
				self.attack_animation = False
		if self.current_sprite == 0 and anim_id == 1:
			movement = random.randint(0,1)
			if self.l_m != movement:
				sprite_change(self)
			if movement == 0 or self.rect.x <= 50:
				self.rect.x += 1
			elif movement == 1 or self.rect.x >= 200:
				self.rect.x -= 1
			self.l_m = movement
		self.image = self.idle_sprites[int(self.current_sprite)]

	def digitize(self,id):
		self.idle_sprites = []
		self.current_mon = SpriteSheet(mons[id])
		self.l_m = 1
		fpa = 2
		for i in range(fpa):
			self.idle_sprites.append(self.current_mon.get_sprite(i*16,0,16,16))
		return 0
	
	def hatch(self,id):
		self.idle_sprites = []
		self.idle_sprites.append(self.current_mon.get_sprite(1*16,0,16,16))
		self.idle_sprites.append(self.current_mon.get_sprite(2*16,0,16,16))

		return 0

	def idle(self):
		self.animation = True


class SpriteSheet():
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()
    
    def get_sprite(self, x, y, w, h, scale=1):
        # Crear superficie con canal alpha
        sprite = pygame.Surface([w, h], pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, w, h))
        
        if scale != 1:
            # Escalar el sprite al tamaño deseado
            scaled_w = w * scale
            scaled_h = h * scale
            sprite = pygame.transform.scale(sprite, (scaled_w, scaled_h))
        
        return sprite

class Menu(pygame.sprite.Sprite):
	def __init__(self,id,i):
		super().__init__()
		self.materialize(id,i)
		self.menu_sprites = []

	def materialize(self,id,i):
		self.menu_sprites = []
		self.current_sprite = SpriteSheet(id)
		self.menu_sprites.append(self.current_sprite.get_sprite(0,0,64,32))
		self.current_sprite = 0
		self.image = self.menu_sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [i*64,0]


##Funciones
def sprite_change(self):
	for i in range(len(self.idle_sprites)):
		self.idle_sprites[i] = pygame.transform.flip(self.idle_sprites[i],1,0)