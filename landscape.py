# This program was inspired after hyperspace from Star Wars

import pygame
import random

pygame.init()

fps = 30
screen_width = 550
screen_height = 350
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Landscape Assignment")

area_length = 50
distr_scaling = 7

x_center = screen_width / 2
y_center = screen_height / 2

wing_x = x_center
wing_y = y_center
wing_speed = 1

# Generate random stars
dot_coords = []
for x in range(0,screen_width, area_length):
    for y in range(0, screen_height, area_length):
        coords = random.randint(x+distr_scaling, x+area_length-distr_scaling), random.randint(y+distr_scaling, y+area_length-distr_scaling)
        if coords[0] != x_center:
            dot_coords.append(coords)

# Loop until the user clicks the close button.
done = False
stars_done = 0
animation_done = 0
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if wing_x <= x_center - 20 or wing_x >= x_center +20:
        wing_speed = -wing_speed

    wing_x += wing_speed
            
    # --- Screen-clearing code goes here
    screen.fill("black")
    # Drawing
    if stars_done <= (fps*2):
        for i in dot_coords:
            pygame.draw.rect(screen, "white", (*i, 4, 4))
        stars_done += 1
    else:
        if animation_done <= fps * 3.5:
            for i in dot_coords:
                slope = (i[1] - y_center) / (i[0] - x_center)
                if i[0] > x_center:
                    pygame.draw.line(screen, "white", i, (i[0] + animation_done * 5, i[1] + animation_done * 5 * slope), 3)
                else:
                    pygame.draw.line(screen, "white", i, (i[0] - animation_done * 5, i[1] - animation_done * 5 * slope), 3)
            animation_done += 1
        else:
            stars_done = 0
            animation_done = 0

    pygame.draw.rect(screen, "orange", (wing_x, wing_y, 15, 12))
    pygame.draw.line(screen, "orange", (wing_x+14, wing_y), (wing_x+37, wing_y-6), 3)
    pygame.draw.line(screen, "orange", (wing_x+15, wing_y+12), (wing_x+31, wing_y+17), 3)
    pygame.draw.line(screen, "orange", (wing_x, wing_y+12), (wing_x-14, wing_y+21), 3)
    pygame.draw.line(screen, "orange", (wing_x, wing_y-1), (wing_x-18, wing_y-5), 3)
    
    # FPS
    pygame.display.flip()
    clock.tick(fps)
