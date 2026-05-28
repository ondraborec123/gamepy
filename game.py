# IMPORTS
import player
import pygame
import constants as c

# BASE SETTINGS
pygame.init()
window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Best game CZ/SK/UA")
icon = pygame.image.load("assets/lilnig.png")
pygame.display.set_icon(icon)
pygame.time.delay(100)
run = True

# FONTS AND TEXTS
comicsans = pygame.font.Font("assets/comicsans.ttf", 28)

nadpis_var = "Welcome to best game in all of Czechia, Slovakia AND Ukraine!!"
nadpis = comicsans.render(nadpis_var, True, (255, 0, 0))
nadpis_rect = nadpis.get_rect()
nadpis_rect.center = (c.WIDTH / 2, 100)

# FUNCTIONS
def player_function():
	plr = pygame.image.load("assets/ch0.0.png")
	window.blit(plr, (player.x,player.y))
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w] and player.y > 0 or keys[pygame.K_UP] and player.y > 0: player.y -= player.vel
	if keys[pygame.K_s] and player.y < c.HEIGHT-96 or keys[pygame.K_DOWN] and player.y < c.HEIGHT-96: player.y += player.vel
	if keys[pygame.K_a] and player.x > -18 or keys[pygame.K_LEFT] and player.x > 0-18: player.x -= player.vel
	if keys[pygame.K_d] and player.x < c.WIDTH-78 or keys[pygame.K_RIGHT] and player.x < c.WIDTH-78: player.x += player.vel


# MAIN LOOP
while run:
	for e in pygame.event.get():
		if e.type == pygame.QUIT: run = False

	# main events
	window.fill("grey")
	player_function()

	# update screen
	pygame.display.update()

pygame.quit()