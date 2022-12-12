#Snake 
from tarfile import BLOCKSIZE
from this import d
from turtle import color, right
import pygame
import sys
import random 
import turtle

pygame.init()

Colors = {
    "Red" : (0,100,0),
    "Minty Green" : (40, 210, 180),
    "Yellow" : (100, 0, 0),
}
Food = {
    "X": 0,
    "Y": 0,
    "Color": Colors["Yellow"],
}
config = {
    "ScreenX" : 800,
    "ScreenY" : 600,
    "ScreenTitle" : "Snake",
    "background" : Colors["Red"],   
    "BLOCKSIZE" : 10,
    "speed" : 15,
}
Snake = {
    "X" : config["ScreenX"] / 2 ,
    "Y" : config["ScreenY"] / 2 ,
    "Direction" : "none",
    "Color" : Colors["Minty Green"],
    "Length" : 0,
    "Tail" : [],
}
def RandomizeFoodLocation():
    Food["X"] = round(random.randrange(0,config["ScreenX"]-config["BLOCKSIZE"]), -1)
    Food["Y"] = round(random.randrange(0,config["ScreenY"]-config["BLOCKSIZE"]), -1)

def DrawGame(screen):
    screen.fill(Colors["Red"])
    pygame.draw.rect(screen,Snake["Color"], [Snake["X"], Snake["Y"], config["BLOCKSIZE"], config["BLOCKSIZE"]])
    for tail in Snake["Tail"]:
        pygame.draw.rect(screen,Snake["Color"], [tail[0], tail[1], config["BLOCKSIZE"], config["BLOCKSIZE"]])
    pygame.draw.rect(screen,Food["Color"], [Food["X"], Food["Y"], config["BLOCKSIZE"], config["BLOCKSIZE"]])
    pygame.display.update()

def  main():
    screen = pygame.display.set_mode([config["ScreenX"], config["ScreenY"]])
    clock = pygame.time.Clock()
    pygame.display.set_caption(config["ScreenTitle"])
    pygame.display.update()
    RandomizeFoodLocation()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if Snake["Direction"] != "right":
                        Snake["Direction"] = "left"
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if Snake["Direction"] != "left":
                        Snake["Direction"] = "right"                
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if Snake["Direction"] != "up":
                        Snake["Direction"] = "down"               
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if Snake["Direction"] != "down":
                        Snake["Direction"] = "up" 
                
        if Snake["Direction"] == "left":
            Snake["X"] -= config["BLOCKSIZE"]
        if Snake["Direction"] == "right":
            Snake["X"] += config["BLOCKSIZE"]
        if Snake["Direction"] == "up":
            Snake["Y"] -= config["BLOCKSIZE"]
        if Snake["Direction"] == "down":
            Snake["Y"] += config["BLOCKSIZE"]

        DrawGame(screen) 

        if Snake["X"] <  0 or Snake["X"] >= config["ScreenX"] or Snake["Y"] < 0 or Snake["Y"] >= config["ScreenY"]:
            print("Dumbass")
            break
        

        if [Snake["X"], Snake["Y"]] in Snake["Tail"]:
            print("you hit yourself")
            break

        if Snake["X"] == Food["X"] and Snake["Y"] == Food["Y"]:
            Snake["Length"] += 1 
            Snake["Tail"].append([Food["X"], Food["Y"]])
            RandomizeFoodLocation()

        Snake["Tail"].append([Snake["X"],Snake["Y"]])
        if len(Snake["Tail"]) > Snake["Length"]:
            del Snake["Tail"][0]
        


        clock.tick(config["speed"])
    

    
if __name__ == "__main__":
    main()
