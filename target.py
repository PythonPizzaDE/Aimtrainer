import pygame

class Target(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.image.load('assets/target.png')
		self.rect = self.image.get_rect(center=pos)

	def is_pressed(self):
		button = pygame.mouse.get_pressed()
		return button[0] and self.rect.collidepoint(pygame.mouse.get_pos())