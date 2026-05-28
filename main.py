import random
import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))

# player
x = 50
y = 450
vel = 0.3

# meteorite
m_x = random.randint(32, 500-32)
y = 16
vel = 0.5

# settings
pygame.time.delay(100)
run = True

# main loop
while run:
	for e in pygame.event.get():
		if e.type == pygame.QUIT: run = False

	# main
	window.fill("green")
	player = pygame.image.load("lilnig.png")
	window.blit(player, (x,y))

	keys = pygame.key.get_pressed()
	if keys[pygame.K_w] and y > 0: y -= vel
	if keys[pygame.K_s] and y < 500-32: y += vel
	if keys[pygame.K_a] and x > 0: x -= vel
	if keys[pygame.K_d] and x < 500-32: x += vel

	# update screen
	pygame.display.update()

pygame.quit()
