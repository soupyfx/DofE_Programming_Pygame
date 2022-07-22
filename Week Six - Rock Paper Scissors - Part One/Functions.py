import pygame

def createText(text,font,colour,x,y,display):
	text = font.render(text, True, colour)
	display.blit(text, (x, y))


