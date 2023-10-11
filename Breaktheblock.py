import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect, KEYUP
import time
 
class Block:
    """ 블록, 공, 패들 오브젝트 """
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270
 
    def move(self):
        """ 공을 움직인다 """
        self.rect.centerx += math.cos(math.radians(self.dir))\
             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
             * self.speed
 
    def draw(self):
        """ 블록, 공, 패들을 그린다 """
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)
 

 
def tick():
    """ 프레임별 처리 """
    global BALLS, BLOCKS, score, isFeverTime, startTime, endTime
 
    # 키 입력 처리
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                if PADDLE.rect.centerx > 55:
                    PADDLE.rect.centerx -= 5
            elif event.key == K_RIGHT:
                if PADDLE.rect.centerx < 545:
                    PADDLE.rect.centerx += 5
    for BALL in BALLS:
        if BALL.rect.centery < 1000:
            BALL.move()
 
        # 공이 블록과 충돌하면
        prevlen = len(BLOCKS)
        BLOCKS = [x for x in BLOCKS
                if not x.rect.colliderect(BALL.rect)]
        if len(BLOCKS) != prevlen:
            BALL.dir *= -1
            score += 10 * stage
 
 

        # 공이 패들과 충돌하면
        if PADDLE.rect.colliderect(BALL.rect):
            BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) \
                / PADDLE.rect.width * 80
 
        # 공이 벽과 충돌하면
        if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
            BALL.dir = 180 - BALL.dir
        if BALL.rect.centery < 0:
            BALL.dir = -BALL.dir
            BALL.speed = 15 - 1 + stage 

        # 패들과 벽이 충돌하면


pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALLS = [Block((242, 242, 0), Rect(300, 400, 20, 20), 10)]
 
isNeedToRestart = False
isFeverTime = False
score = 0
startTime = 0.0
endTime = 0.0
stage = 1

# 초기화
def init():
    global SURFACE, FPSCLOCK, BLOCKS, PADDLE, BALLS, isNeedToRestart, isFeverTime, score, stage, startTime, endTime
 
    pygame.init()
    pygame.key.set_repeat(5, 5)
    SURFACE = pygame.display.set_mode((600, 800))
    FPSCLOCK = pygame.time.Clock()
    BLOCKS = []
    PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
    BALLS = [Block((242, 242, 0), Rect(300, 400, 20, 20), 10)]
    isNeedToRestart = False
    isFeverTime = False
    score = 0
    stage = 1
    startTime = 0.0
    endTime = 0.0
 
def main():
    global isNeedToRestart, score, isFeverTime, startTime, endTime, stage
 
    """ 메인 루틴 """
    myfont = pygame.font.SysFont(None, 80)
    smallfont = pygame.font.SysFont(None, 36)
    scorefont = pygame.font.SysFont(None, 25)
    mess_clear = myfont.render("Cleared!", True, (255, 255, 0))
    mess_over = myfont.render("Game Over!", True, (255, 255, 0))
    mess_replay = smallfont.render("replay (press r)", True, (255, 0, 0))
    fps = 30
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0)]
 
    # 블록을 추가해준다.
    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color, Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))
 
    while True:
        tick()
 
        # 공을 그린다
        SURFACE.fill((0, 0, 0))
        for BALL in BALLS:
            BALL.draw()
        PADDLE.draw()
 
        # 블록을 그린다
        for block in BLOCKS:
            block.draw()        
 
        # 블록을 모두 제거하면 성공
        if len(BLOCKS) == 0:           
             stage += 1
             for ypos, color in enumerate(colors, start=0):
                for xpos in range(0, 5):
                    BLOCKS.append(Block(color, Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))       

        # 공이 패들 밑으로 내려가면 해당 공은 삭제
        for BALL in BALLS:
            if BALL.rect.centery > 800 and len(BLOCKS) > 0:
                BALLS.remove(BALL)
 

        # 공이 하나도 없는 경우(끝난 경우)
        if len(BALLS) <= 0:
            SURFACE.blit(mess_over, (150, 400))
            SURFACE.blit(mess_replay, (230, 460))
            isNeedToRestart = True
 
        # 스코어 보드
        mess_score = scorefont.render("score : " + str(score), True, (255, 255, 255))
        SURFACE.blit(mess_score, (10, 10))

        mess_stage = scorefont.render("stage : " + str(stage), True, (255, 255, 255))
        SURFACE.blit(mess_stage, (520, 10))
 
        pygame.display.update()
        FPSCLOCK.tick(fps)
 
        # r키를 누르면 재시작 가능하도록 설정
        while isNeedToRestart:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == pygame.K_r:
                    isNeedToRestart = False
                    break
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    break
 
            if isNeedToRestart == False:
                init()
                main()
                break
            
 
if __name__ == '__main__':
    main()