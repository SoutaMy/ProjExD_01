import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img3 = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img = pg.image.load("ex01-20230926/fig/3.png")
    bg_img = pg.transform.flip(bg_img, True, False)
    bg_img7 = pg.transform.flip(bg_img3, True, False)# 反転背景
    bg_img2 = pg.transform.rotozoom(bg_img, 10, 1.0)
    bg_img4 = pg.transform.rotozoom(bg_img, 15, 1.0)
    bg_img5 = pg.transform.rotozoom(bg_img, 20, 1.0)
    bg_img8 = pg.transform.rotozoom(bg_img, 15, 1.0)
    bg_img9 = pg.transform.rotozoom(bg_img, 13, 1.0)
    bg_imgs = [bg_img, bg_img2, bg_img4, bg_img5, bg_img8, bg_img9]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        
        screen.blit(bg_img3, [-x, 0]) 
        screen.blit(bg_img7, [1600-x, 0]) 
        screen.blit(bg_img7, [1600-x, 0])
        screen.blit(bg_img3, [3200-x, 0]) 
    
        screen.blit(bg_imgs[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()