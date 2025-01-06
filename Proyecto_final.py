import pygame, sys
from pygame.locals import *

import pandas as pd
data_base = pd.read_csv('sleep_data_final.csv')

pygame.font.init()

from item_menu import *
from sprites import *


mons = {0:'Lioll_Digitama.png', 1:'Popomon.png',
        2:'Nyaromon.png',3:'Leomon.png',
        4:'Panjyamon.png', 5:'BanchoLeomon.png'}
mons_names = {0:'Lioll_Digitama', 1:'Popomon',
        2:'Nyaromon',3:'Leomon',
        4:'Panjyamon', 5:'BanchoLeomon'}


state = 0 # 0idle 1move 2evol 3move

# Game Screen
BASE_WIDTH = 256
BASE_HEIGHT = 192

# Configuración de escalado
SCALE_FACTOR = 3  # Valor ajustable para el tamaño de la interfaz

# Dimensiones escaladas
screen_width = BASE_WIDTH * SCALE_FACTOR
screen_height = BASE_HEIGHT * SCALE_FACTOR

#Textos
TEXT_COL =(255,255,255)
font = pygame.font.SysFont("Arialblack", 40)

menu = []
menu_items ={0:'Items',1:'Training',2:'battle',3:'alarm',
            4:'sleep',5:'library',6:'bath',7:'link'}
menu_objects = ['bp.png','training.png','battle.png','alarm.png',
                'sleep.png','library.png','bath.png','link.png']

# Color de fondo personalizado
BG_COLOR = (200, 230, 255)  # Color editable RGB


if __name__ == "__main__":
	# General setup
	pygame.init()
	clock = pygame.time.Clock()
    
	screen = pygame.display.set_mode((screen_width,screen_height))

	# Crear una superficie para renderizar el juego en resolución base
	game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))

	pygame.display.set_caption("Sprite Animation")

    # Cargar y configurar el fondo
	try:
		bg = pygame.image.load("test_bg.png").convert_alpha()
	except:
		bg = None
	# Creating the sprites and groups
	moving_sprites = pygame.sprite.Group()
	player = Mon(100,130)
	moving_sprites.add(player)
	i = 0
	j=0
	k=0
	for str in menu_objects:
		menu.append(Menu(str,i,j))
		moving_sprites.add(menu[k])
		i += 1
		if i >= 4:
			j = 1
			i = 0
		k += 1
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_h]:
			print (enemy.attack,enemy.hp)
			
		#Evolution
		state = evolution(player,state)

		#Menu!
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			x, y = pygame.mouse.get_pos()
			for i in range(len(menu)):
				target = menu[i].rect.collidepoint(x/3, y/3)
				print(x,y)
				if target == True:
					match i:
						case 0:
							print('Boton pulsado en '+ menu_items[i])
						case 1:
							print('Boton pulsado en '+ menu_items[i])
							player.rect.x = 100
							state = 5
							nabo_sprite = pygame.sprite.Group()
							nabo = Nabo(120,84)
							nabo_sprite.add(nabo)
						case 2:
							if player.stage == 'Baby I' or state == 2:
								break
							print('Boton pulsado en '+ menu_items[i])
							player.rect.x = 0
							state = 3
							enemy_sprite = pygame.sprite.Group()
							enemy = Mon(260,130)
							enemy.digitize(random.randint(2,3))
							enemy_sprite.add(enemy)
						case _: break

        # Primero dibujamos todo en la superficie base
		game_surface.fill(BG_COLOR)
		if bg:
			game_surface.blit(bg, (0, 0))

		#Training!
		try:
			nabo_sprite.draw(game_surface)
			nabo.update(event)
		except:
			pass

		#Battle!
		try:
			enemy_sprite.draw(game_surface)
			if enemy.rect.x >=150:
				enemy.update(0.07,4)
			if enemy.rect.x <=150:
				enemy.update(0.07,1)
		except:
			pass
		if state == 3 and player.rect.x >= 110:
			state = battle(player,enemy,state)
			del enemy_sprite
		#calcular tiempo desde victoria

		# Drawing
		moving_sprites.draw(game_surface)
        
        # Escalar la superficie base a la pantalla
		scaled_surface = pygame.transform.scale(game_surface, (screen_width, screen_height))
		screen.blit(scaled_surface, (0, 0))
		moving_sprites.update(0.07,state)

		pygame.display.flip()
		clock.tick(15)