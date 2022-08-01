import pygame

def createText(text,font,colour,x,y,display):
	text = font.render(text, True, colour)
	display.blit(text, (x, y))

def drawMenu(currentMenu,playerLives,computerLives,currentLevel,display,font):
    display.fill((0,0,0))
    if currentMenu == "mainMenu":
        createText("Rock Paper Sissors The Game",font,(255,255,255),10,10,display)
        createText("Press 'N' for new game",font,(255,255,255),10,460,display)
        createText("Hold 'H' for how to play",font,(255,255,255),10,500,display)
    elif currentMenu == "helpMenu":
        createText("N O",font,(255,255,255),10,10,display)
        createText("Press 'X' to exit",font,(255,255,255),10,500,display)
    elif currentMenu == "gameMenu":
        print("gameMenu")
        createText("Press 'X' to restart the game",font,(255,255,255),10,500,display)
    elif currentMenu == "endMenu":
        createText("Game Over",font,(255,255,255),10,10,display)
        createText("The winner was:",font,(255,255,255),10,50,display)
        createText("The ammount of rounds:",font,(255,255,255),10,90,display)
        createText("Press 'N' to start a new game",font,(255,255,255),10,500,display)
        createText("Press 'X' to return the menu",font,(255,255,255),10,460,display)
        
    else: 
        print("Please provide the correct args for 'currentMenu'")

     
        
    