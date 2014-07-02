#import pygame,  sys#imports the pygame function

pygame.init()

screen = pygame.display.set_mode([445, 300])#Displays the canvas

b = pygame.Color("blue")#assigns colours
w = pygame.Color("white")#assigns colours
r = pygame.Color("red")
y = pygame.Color("yellow")
data = [#Gives a multiple list of of colours to  make the space invader
  [ w, w, b, w, w, w, b, w, w, w, w, w, w, w, w, w, w, w ],
  [ w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w ],
  [ w, w, w, w, r, w, w, w, w, w, w, w, w, w, w, w, w, w ],
  [ w, y, w, w, w, w, w, y, w, w, w, w, w, w, w, w, w, w ],
  [ w, w, y, y, y, y, y, w, w, w, w, w, w, w, w, w, w, w ],
  [ r, r, w, r, r, r, r, r, w, r, w, r, w, w, w, r, r, r ],
  [ r, w, w, r, w, r, w, r, w, w, w, r, w, w, w, r, w, w ],
  [ r, r, w, r, w, r, w, r, w, r, w, r, w, w, w, r, r, r ],
  [ w, r, w, r, w, r, w, r, w, r, w, r, w, w, w, r, w, w ],
  [ r, r, w, r, w, r, w, r, w, r, w, r, r, r, w, r, r, r ],
  [ w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w ],
  [ w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w ],
  [ w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w ] 
  ]
  
  

for y, row in enumerate(data):
  for x, colour in enumerate(row):
    rect = pygame.Rect(x*25, y*25, 25, 25)
    screen.fill(colour, rect=rect)#fills the screen

pygame.display.update()#display the feature

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
