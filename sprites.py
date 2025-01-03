##Sprites
import pygame


class SpriteSheet():
	def __init__(self, file):
		self.sheet = pygame.image.load(file)
	
	def get_sprite(self, x, y, w, h):
		sprite = pygame.Surface([w,h])
		sprite.blit(self.sheet, (0,0), (x,y,w,h))
		sprite.set_alpha
		return sprite

def sprite_change(self):
	for i in range(len(self.idle_sprites)):
		self.idle_sprites[i] = pygame.transform.flip(self.idle_sprites[i],1,0)