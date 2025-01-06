##Sprites
import pygame
import random

import pandas as pd
from Proyecto_final import mons,mons_names,data_base


class Mon(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.idle_sprites = []
		self.animation = True
		self.data_base = pd.read_csv('sleep_data_final.csv')
		self.digitize(0)

		self.current_sprite = 0
		self.image = self.idle_sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]
  
		#Stats!
		self.attack = 0
		self.hp = 0
		self.stage = 'Baby I'
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
				self.rect.x += 2
			elif movement == 1 or self.rect.x >= 200:
				self.rect.x -= 2
			self.l_m = movement
		elif anim_id == 3:
			entrance(self,1) #izquierda
		elif anim_id == 4:
			entrance(self,-1) #derecha
		elif anim_id == 5:
			victory(self)
		elif anim_id ==6:
			defeat(self)
		self.image = self.idle_sprites[int(self.current_sprite)]

	def digitize(self,id):
		self.idle_sprites = []
		self.current_stats = None
		self.current_mon = SpriteSheet(mons[id])
		self.current_stats = data_base.loc[data_base['name'] == mons_names[id]]
		self.l_m = 1 #1derecha #0izquierda
		fpa = 2
		for i in range(fpa):
			self.idle_sprites.append(self.current_mon.get_sprite(i*16,0,16,16))
		if id >= 2:
			self.attack = self.current_stats['attack'].item()
			self.hp = self.current_stats['hp'].item()
			self.stage = self.current_stats['stage'].item()
		return 0
	
	def hatch(self):
		self.idle_sprites = []
		self.idle_sprites.append(self.current_mon.get_sprite(1*16,0,16,16))
		self.idle_sprites.append(self.current_mon.get_sprite(2*16,0,16,16))

		return 0

	def idle(self):
		self.animation = True


class SpriteSheet():
	def __init__(self, file):
		self.sheet = pygame.image.load(file).convert_alpha()
		self.file_name = file
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
	def __init__(self,id,i,j):
		super().__init__()
		self.materialize(id,i,j)
		self.menu_sprites = []

	def materialize(self,id,i,j):
		self.menu_sprites = []
		self.current_sprite = SpriteSheet(id)
		self.menu_sprites.append(self.current_sprite.get_sprite(0,0,64,32))
		self.current_sprite = 0
		self.image = self.menu_sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [i*64,j*161]


##Funciones
def sprite_change(self):
	for i in range(len(self.idle_sprites)):
		self.idle_sprites[i] = pygame.transform.flip(self.idle_sprites[i],1,0)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))
    
def evolution(player,state):
	if pygame.time.get_ticks() in range(5000,9000):
		player.hatch()
		state = 2
	if pygame.time.get_ticks() in range(9001,9100):
		player.digitize(3)
		state = 1
	# if pygame.time.get_ticks() in range(15000,19000):
	# 	player.hatch()
	# 	state = 2
	# if pygame.time.get_ticks() in range(19001,20000):
	# 	player.digitize(2)
	# 	state = 1
	# if pygame.time.get_ticks() in range(30000,34000):
	# 	player.hatch()
	# 	state = 2
	# if pygame.time.get_ticks() in range(34001,34100):
	# 	player.digitize(3)
	# 	state = 1
	# if pygame.time.get_ticks() in range(50000,54000):
	# 	player.hatch()
	# 	state = 2
	# if pygame.time.get_ticks() in range(54001,54100):
	# 	player.digitize(4)
	# if pygame.time.get_ticks() in range(70000,74000):
	# 	player.hatch()
	# 	state = 2
	# if pygame.time.get_ticks() in range(74001,74100):
	# 	player.digitize(5)
	# 	state = 1
	return state

def battle(player,enemy,state):
	rng_player = random.randint(1,5)
	rng_enemy = random.randint(1,5)
	enemy_attack = rng_enemy*enemy.attack
	player_attack = rng_player*player.attack
	player_hp = player.hp
	enemy_hp = enemy.hp
	while player_hp > 0 and enemy_hp > 0:
		if player_attack >= enemy_attack:
			enemy_hp -= enemy_hp+(int(player_attack/10))
		elif player_attack < enemy_attack:
			player_hp -= player_hp+(int(enemy_attack/10))
	
	if enemy_hp <= 0:
		return 5
	elif player_hp <= 0:
		return 6

#Movement
def entrance(self,dir):
	if self.l_m > 1:
		sprite_change(self)
		self.l_m = 1
	self.rect.x += 1*dir

def victory(self):
	self.idle_sprites = []
	self.idle_sprites.append(self.current_mon.get_sprite(0*16,2*16,16,16))
	self.idle_sprites.append(self.current_mon.get_sprite(1*16,2*16,16,16))
 
def defeat(self):
	self.idle_sprites = []
	self.idle_sprites.append(self.current_mon.get_sprite(0*16,3*16,16,16))
	self.idle_sprites.append(self.current_mon.get_sprite(1*16,3*16,16,16))