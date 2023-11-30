import pygame # 파이게임 라이브러리 불러옴
import random

pygame.init() #초기화

# 화면 크기 설정
screen_width = 500 # 가로 크기
screen_height = 500 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("낙하물 피하기")

# FPS
clock = pygame.time.Clock()

# 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("./image/back.png")
character = pygame.image.load("./image/player_small.png")
enemy = pygame.image.load("./image/enemy_small.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

enemy_x_pos = random.randint(0, (screen_width - character_width))
enemy_y_pos = 0

to_x = 0
to_y = 0

character_speed = 0.5
enemy_speed = 1
time_elapsed = 0
spawn_interval = 5

game_over_font = pygame.font.Font(None, 100)
game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()
avoid_enemies = 0

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)
    to_y = 0
    to_y += enemy_speed
    time_elapsed += dt / 1000

    if time_elapsed >= spawn_interval:
        # 일정 시간이 경과하면 속도와 생성 간격을 조정
        enemy_speed += 0.2 # 0.2초마다 속도 증가
        spawn_interval -= 0.5 # 0.5초마다 생성 간격 감소
        time_elapsed = 0
    screen.fill((0, 0, 0))
    # 2. 키 입력 이벤트 처리

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

# 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    enemy_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, (screen_width - character_width))
        enemy_y_pos = 0
        avoid_enemies += 1

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render('Time:{}'.format(round(elapsed_time, 2)), True, (255, 255, 255))
    avoided = game_font.render('You avoided: {}'.format(avoid_enemies), True, (255, 255, 255))
    game_over = game_over_font.render('GameOver!', True, (255, 255, 255))

 # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    screen.blit(avoided, (200, 10))

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        screen.blit(game_over, (50, 100))
        running = False

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()  # 게임 종료
