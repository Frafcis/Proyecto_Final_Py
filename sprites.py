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
	
	def hatch(self,):
		self.idle_sprites = []
		self.idle_sprites.append(self.current_mon.get_sprite(2*16,0,16,16))
		self.idle_sprites.append(self.current_mon.get_sprite(3*16,0,16,16))

		return 0
	def idle(self):
		self.animation = True
	
	def moving(self):
		return 0


class SpriteSheet():
	def __init__(self, file):
		self.sheet = pygame.image.load(file)
	
	def get_sprite(self, x, y, w, h):
		sprite = pygame.Surface([w,h])
		sprite.blit(self.sheet, (0,0), (x,y,w,h))
		sprite.set_alpha
		return sprite


##Funciones
def sprite_change(self):
	for i in range(len(self.idle_sprites)):
		self.idle_sprites[i] = pygame.transform.flip(self.idle_sprites[i],1,0)