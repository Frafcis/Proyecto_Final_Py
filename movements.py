## Clases

import pygame, sys
from Proyecto_final import mons

class Mon(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		
		self.sheet = []
		self.l_m = 1
  
		self.current_mon(0)

		self.current_sprite = 0
		self.image = self.sheet[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]
	def current_mon(self, id):
		self.current_mon = SpriteSheet(mons[id])
		fpa = 2
		for i in range(fpa):
			self.sheet.append(self.current_mon.get_sprite(i*16,0,16,16))
		return 0

class State(Mon):
    def __init__(self,properties):
        self.attack_animation = False
        self.animation = False
        self.current_sprite = properties.current_sprite
    def idle(self):
        self.animation = True
        if self.animation == True:
            if int(self.current_sprite) >= len(self.sheet):
                self.current_sprite = 0
                self.attack_animation = False
    def update(self,speed):
        if self.current_sprite == 0:
            movement = random.randint(0,1)
            if self.l_m != movement:
                sprite_change(self)
            if movement == 0 or self.rect.x <= 50:
                self.rect.x += 1
            elif movement == 1 or self.rect.x >= 200:
                self.rect.x -= 1
            self.l_m = movement
        self.image = self.sheet[int(self.current_sprite)]
        
class SpriteSheet():
	def __init__(self, file):
		self.sheet = pygame.image.load(file)
	
	def get_sprite(self, x, y, w, h):
		sprite = pygame.Surface([w,h])
		sprite.blit(self.sheet, (0,0), (x,y,w,h))
		sprite.set_alpha
		return sprite

def sprite_change(self):
	for i in range(len(self.sheet)):
		self.sheet[i] = pygame.transform.flip(self.sheet[i],1,0)