import pygame, sys
import pygame.locals
import random



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

class Mon(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.idle_sprites = []
		self.current_mon = SpriteSheet('Leomon_X.png')
		self.l_m = 1
		fpa = 2
		for i in range(fpa):
			self.idle_sprites.append(self.current_mon.get_sprite(i*16,0,16,16))

		self.current_sprite = 0
		self.image = self.idle_sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def idle(self):
		self.animation = True

	def update(self,speed):
		if self.animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.idle_sprites):
				self.current_sprite = 0
				self.attack_animation = False
		if self.current_sprite == 0:
			movement = random.randint(0,1)
			if self.l_m != movement:
				sprite_change(self)
			if movement == 0 or self.rect.x <= 50:
				self.rect.x += 1
			elif movement == 1 or self.rect.x >= 200:
				self.rect.x -= 1
			self.l_m = movement
		

		self.image = self.idle_sprites[int(self.current_sprite)]

if __name__ == "__main__":
	# General setup
	pygame.init()
	clock = pygame.time.Clock()
	bg = pygame.image.load("test_bg.png")

	# Game Screen
	screen_width = 256
	screen_height = 192
	screen = pygame.display.set_mode((screen_width,screen_height))
	pygame.display.set_caption("Sprite Animation")

	# Creating the sprites and groups
	moving_sprites = pygame.sprite.Group()
	player = Mon(100,100)
	moving_sprites.add(player)

	while True:
		player.idle()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		# Drawing
		screen.fill((255,255,255))
		screen.blit(bg, (0, 0))
		moving_sprites.draw(screen)
		moving_sprites.update(0.07)
		pygame.display.flip()
		clock.tick(15)