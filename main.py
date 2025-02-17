# preparation start

import pygame
# importing pygame extention
Screen_width, Screen_height = 1000, 500
# width and height of screen
Screen = pygame.display.set_mode((Screen_width, Screen_height), pygame.RESIZABLE)
# setting screen width and height
favicon = pygame.image.load("favicon.png")

pygame.display.set_icon(favicon)

x_img = pygame.image.load('x.png').convert_alpha()
# loading in image

# preparation end

# making a function called Make_btn
class Make_x_btn():
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

x_button = Make_x_btn(950, 0, x_img, 0.1)
# making a variable that uses the "Make_x_btn" function to be on the screen.
run = True
# making a variable called "run" and setting it to be true
while run:
# making a while loop which works only if the run variable is True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x_button.draw()
# setting the run variable to False if you click the X button on the top or the custom X button that you made
    pygame.display.update()
    pygame.display.flip()
# updates the screen to show the button