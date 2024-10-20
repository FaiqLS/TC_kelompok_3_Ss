import pygame as pg
# print(pygame.__version__)

pg.init()
#membuat jendela game pertama
screen = pg.display.set_mode((1920,1080))
pg.display.set_caption('My First Game')

# tambahkan image
image = pg.image.load('C:\\Users\\faiql\\bikin game\\1920x1080.jpeg')

#loop game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #white background
    screen.fill((0,0,0))
    #menampilkan gambar
    screen.blit(image,(0,0))
    #update tampilan layar
    pg.display.update()

pg.quit()


