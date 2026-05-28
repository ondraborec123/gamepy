import player
import pygame
import constants as c
pygame.init()
window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Best game CZ/SK/UA")
# settings
pygame.time.delay(100)
run = True

# font and texts
comicsans = pygame.font.Font("assets/comicsans.ttf", 28)

nadpis_var = "Welcome to best game in all of Czechia, Slovakia AND Ukraine!!"
nadpis = comicsans.render(nadpis_var, True, (255, 0, 0))
nadpis_rect = nadpis.get_rect()
nadpis_rect.center = (c.WIDTH/2,100)

# FUNCTIONS
def player_function():
	plr = pygame.image.load("assets/lilnig.png")
	window.blit(plr, (player.x,player.y))
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w] and player.y > 0: player.y -= player.vel
	if keys[pygame.K_s] and player.y < 500-32: player.y += player.vel
	if keys[pygame.K_a] and player.x > 0: player.x -= player.vel
	if keys[pygame.K_d] and player.x < 500-32: player.x += player.vel

# class Button:
# 	def __init__(self,x,y,width,height):
# 		global window
# 		self.x = x
# 		self.y = y
#
# 		self.btn = pygame.Rect(x, y, 150, 70)
# 		pygame.draw.rect(window, colour, btn)
# 		txt = comicsans.render(text, True, (255, 0, 0))
# 		txt_rect = txt.get_rect()
# 		txt_rect.center = (x+x/4, y+y/7)
# 		window.blit(txt, txt_rect)


# main loop
while run:
	for e in pygame.event.get():
		if e.type == pygame.QUIT: run = False

	# MAIN EVENTS
	window.fill("skyblue")
	window.blit(nadpis, nadpis_rect)

	# update screen
	pygame.display.update()

pygame.quit()