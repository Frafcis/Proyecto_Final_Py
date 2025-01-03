import pygame, sys
import pygame.locals
import random

from sprites import *
mons = {0:'Lioll_Digitama.png', 1:'Popomon.png',
        2:'Nyaromon.png',3:'Leomon.png',
        4:'Panjyamon.png', 5:'BanchoLeomon.png'}

state = 0 # 0idle 1move

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
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_h]:
			print ("Mensaje de ayuda")
			
		#Evolution
		if pygame.time.get_ticks() in range(5000,7000):
			player.hatch()
		if pygame.time.get_ticks() in range(7000,7100):
			player.digitize(1)
			state = 1

		# Drawing
		screen.fill((255,255,255))
		screen.blit(bg,(0, 0))
		moving_sprites.draw(screen)
		match state:
			case 0:
				moving_sprites.update(0.07,0)
			case 1:
				moving_sprites.update(0.07,1)
		pygame.display.flip()
		clock.tick(15)