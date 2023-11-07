import pygame

import time

import random

pygame.init()

screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption("Flappy Bird: Smurf Cat Edition")

fly = pygame.image.load("stand.png")
jump = pygame.image.load("jump.png")
pipe = pygame.image.load("pipe.png")
pipe2 = pygame.image.load("pipe2.png")

smurf = pygame.transform.scale(fly, (60, 60))
Pipe = pygame.transform.scale(pipe, (30, 300))
Pipe2 = pygame.transform.scale(pipe2, (30, 300))

font = pygame.font.SysFont('Monospace', 25)
def Message(msg, x, y):
  screen_text = font.render(msg, True, White)
  screen.blit(screen_text, (x, y))

y = 100

score = 0

pipex = 500
pipey = random.randint(100, 300)

pipec = pipex + 0
piped = pipey - 440

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Purple = (255, 0, 255)
Cyan = (0, 255, 255)
White = (255, 255, 255)
Black = (0, 0, 0)

Jump = False

timer = 0

running = True


while running == True:
  screen.fill(Cyan)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        Jump = True
        timer = 0
  if Jump == False:
    y = y + 5
    smurf = pygame.transform.scale(fly, (60, 60))
  if Jump == True:
    smurf = pygame.transform.scale(jump, (60, 60))
    y = y - 5
    timer += 1
    if timer >= 10:
      Jump = False
      timer = 0
  pipex = pipex - 3
  pipec = pipex + 0
  piped = pipey - 440
  if pipex <= 0:
    pipex = 500
    pipey = random.randint(100, 300)
    score = score + 1
  screen.blit(smurf, (100, y))
  screen.blit(Pipe, (pipex, pipey))
  screen.blit(Pipe2, (pipec, piped))
  if pipex <= 100 and pipex >= 40 and y >= pipey and y <= pipey + 300 or pipex <= 100 and pipex > 40 and y <= piped + 280 and y >= piped or y <= 0 and y >= 0 - 60:
    score = 0
    y = 100
  Message(str(score), 300, 10)
  pygame.display.update()