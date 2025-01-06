import pygame

class ItemMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_visible = False
        self.selected_option = None
        self.font = pygame.font.Font(None, 24)
        self.items = [
            {'name': 'Food', 'action': None},
            {'name': 'BigFood', 'action': None},
            {'name': 'Medicine', 'action': None},
            {'name': 'BigMedicine', 'action': None}
        ]
        
        # Configuración visual
        self.width = 120
        self.item_height = 30
        self.padding = 5
        self.colors = {
            'background': (255, 255, 255),
            'border': (100, 100, 100),
            'text': (0, 0, 0),
            'hover': (200, 200, 255)
        }
        
        # Calcular altura total
        self.height = (self.item_height * len(self.items)) + (self.padding * 2)
        
        # Crear rectángulos para cada item
        self.item_rects = []
        for i in range(len(self.items)):
            item_y = self.y + (i * self.item_height) + self.padding
            self.item_rects.append(
                pygame.Rect(self.x, item_y, self.width, self.item_height)
            )
    
    def toggle(self):
        self.is_visible = not self.is_visible
        
    def draw(self, surface):
        if not self.is_visible:
            return
            
        # Dibujar fondo del menú
        menu_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.colors['background'], menu_rect)
        pygame.draw.rect(surface, self.colors['border'], menu_rect, 2)
        
        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()
        # Ajustar posición del mouse por el factor de escala (3)
        scaled_mouse_pos = (mouse_pos[0] / 3, mouse_pos[1] / 3)
        
        # Dibujar cada item
        for i, (rect, item) in enumerate(zip(self.item_rects, self.items)):
            # Verificar si el mouse está sobre el item
            if rect.collidepoint(scaled_mouse_pos):
                pygame.draw.rect(surface, self.colors['hover'], rect)
            
            # Dibujar texto del item
            text = self.font.render(item['name'], True, self.colors['text'])
            text_rect = text.get_rect(
                midleft=(rect.left + 10, rect.centery)
            )
            surface.blit(text, text_rect)
    
    def handle_click(self, pos):
        if not self.is_visible:
            return None
            
        # Ajustar posición del click por el factor de escala
        scaled_pos = (pos[0] / 3, pos[1] / 3)
        
        for i, rect in enumerate(self.item_rects):
            if rect.collidepoint(scaled_pos):
                self.selected_option = self.items[i]['name']
                print(f"Selected item: {self.selected_option}")
                # Aquí puedes agregar la lógica para cada item
                return self.selected_option
        
        return None