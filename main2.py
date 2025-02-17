# preparation start
import image
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

x_button = image.btn(950, 0, x_img, 0.1)
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