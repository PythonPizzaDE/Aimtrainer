import pygame

from random import randint

from start_button import StartButton
from target import Target

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Aimtrainer')

button = StartButton((1280/2, 720/2))
button_group = pygame.sprite.Group()
button_group.add(button)

target_group = pygame.sprite.Group()

for i in range(-5, 5):
	target_group.add(Target((1280/2 + (i * 10), 720/2 + (i * 10))))

bg = pygame.image.load('assets/background.png')

class game:

	state = 'main_menu'


	@staticmethod
	def game():
		target_group.draw(screen)
		for t in target_group:
			if t.is_pressed():
				target_group.remove(t)
				target_group.add(Target((randint(50, 1230), randint(50, 670))))
				del t

	@staticmethod
	def main_menu():
		button_group.draw(screen)
		if button.is_pressed():
			game.state = 'game'

	@staticmethod
	def handle():
		if game.state == 'main_menu':
			game.main_menu()
		elif game.state == 'game':
			game.game()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(bg, (0, 0))
	game.handle()
	pygame.display.flip()