import pygame

Screen_width, Screen_height = 1000, 500
Screen = pygame.display.set_mode((Screen_width, Screen_height), pygame.RESIZABLE)

class btn():
    def __init__(self, x, y, image, scale):
        x_btn_width = image.get_width()
        x_btn_height = image.get_height()
 
        self.image = pygame.transform.scale(image, (int(x_btn_width * scale), int(x_btn_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
 
    def draw(self):
 
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                pygame.quit()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
 
        Screen.blit(self.image, (self.rect.x, self.rect.y))