import pygame, sys
from pygame.locals import *

from sprites import *
mons = {0:'Lioll_Digitama.png', 1:'Popomon.png',
        2:'Nyaromon.png',3:'Leomon.png',
        4:'Panjyamon.png', 5:'BanchoLeomon.png'}

state = 0 # 0idle 1move 2evol

menu = []
menu_items ={0:'Items',1:'Training'}

	# Color de fondo personalizado
BG_COLOR = (200, 230, 255)  # Color editable RGB

if __name__ == "__main__":
	# General setup
	pygame.init()
	clock = pygame.time.Clock()
 
    # Configuración de escalado
	SCALE_FACTOR = 3  # Valor ajustable para el tamaño de la interfaz

	# Game Screen
	BASE_WIDTH = 256
	BASE_HEIGHT = 192
 
    # Dimensiones escaladas
	screen_width = BASE_WIDTH * SCALE_FACTOR
	screen_height = BASE_HEIGHT * SCALE_FACTOR
    
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
	player = Mon(100,100)
	menu_objects = ['bp.png','training.png']
	i = 0
	for str in menu_objects:
		menu.append(Menu(str,i))
		moving_sprites.add(menu[i])
		i += 1
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
		if pygame.time.get_ticks() in range(5000,9000):
			player.hatch(1)
			state = 2
		if pygame.time.get_ticks() in range(9001,9100):
			player.digitize(1)
			state = 1

		#Menu!
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			x, y = pygame.mouse.get_pos()
			for i in range(len(menu)):
				target = menu[i].rect.collidepoint(x/3, y/3)
				if target == True:
					print('Boton pulsado en '+ menu_items[i])
		#Stats!

		# Drawing
        # Primero dibujamos todo en la superficie base
		game_surface.fill(BG_COLOR)
		if bg:
			game_surface.blit(bg, (0, 0))
		moving_sprites.draw(game_surface)
        
        # Escalar la superficie base a la pantalla
		scaled_surface = pygame.transform.scale(game_surface, (screen_width, screen_height))
		screen.blit(scaled_surface, (0, 0))
		moving_sprites.update(0.07,state)

		pygame.display.flip()
		clock.tick(15)