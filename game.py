# IMPORTS
import player
import pygame
import settings as s

# BASE SETTINGS
pygame.init()
ACTIVE_RES=2
window = pygame.display.set_mode(s.resolutions[ACTIVE_RES])
WIDTH=s.resolutions[ACTIVE_RES][0]
HEIGHT=s.resolutions[ACTIVE_RES][1]
if s.fullscreen:
	pygame.display.toggle_fullscreen()
pygame.display.set_caption("Best game CZ/SK/UA")
icon = pygame.image.load("assets/lilnig.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
delta_time = 0
run = True
pause = False

# FONTS AND TEXTS
comicsans = pygame.font.Font("assets/comicsans.ttf", 28)

pauset_var = "**PAUSED**"
pauset = comicsans.render(pauset_var, True, (255, 0, 0))
pauset_rect = pauset.get_rect()
pauset_rect.center = (WIDTH / 2, 100)

# FUNCTIONS
def pause_menu():
	global helpm, help_var, help_rect
	window.blit(helpm, help_rect)

def player_function():
	global pause, run
	plr = pygame.image.load("assets/ch0.0.png")
	window.blit(plr, (round(player.x),round(player.y)))
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w] and player.y > 0 or keys[pygame.K_UP] and player.y > 0: player.y -= player.vel
	if keys[pygame.K_s] and player.y < HEIGHT-96 or keys[pygame.K_DOWN] and player.y < HEIGHT-96: player.y += player.vel
	if keys[pygame.K_a] and player.x > -18 or keys[pygame.K_LEFT] and player.x > 0-18:
		player.x -= player.vel
		plr = pygame.image.load("assets/spritesheetLEFT.png")
	if keys[pygame.K_d] and player.x < WIDTH-78 or keys[pygame.K_RIGHT] and player.x < WIDTH-78:
		player.x += player.vel
		plr = pygame.image.load("assets/spritesheetRIGHT.png")
	if keys[pygame.K_ESCAPE]: run = False


# MAIN LOOP
while run:
	for e in pygame.event.get():
		if e.type == pygame.QUIT: run = False

	# main events
	window.fill("grey")
	player_function()

	# update screen
	pygame.display.update()
	delta_time = clock.tick(240) / 1000

pygame.quit()