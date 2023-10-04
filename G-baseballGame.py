import sys
import pygame
import random
from pygame.locals import *


pygame.init()


screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Baseball Game')

font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0

class button():
		
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 100
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action


# 랜덤 변수 생성
answer = random.randrange(100,900,1)

# 사용자 입력 숫자의 총합
checkPlace = 0 # 사용자가 누른 숫자의 자릿수 체크
playtime = 0 # 사용자가 숫자를 맞춘 횟수 
place1 = 0
place10 = 0
place100 = 0
totalNum = 0

# 사용자 입력 버튼 변수
one = button(600, 200, '1')
two = button(700, 200, '2')
three = button(800, 200, '3')
four = button(600, 300, '4')
five = button(700, 300, '5')
six = button(800, 300, '6')
seven = button(600, 400, '7')
eight = button(700, 400, '8')
nine = button(800, 400, '9')
zero = button(700, 500, '0')
deleteNum = button(600, 500, 'Del')
checkNum = button(800, 500, 'Check')

# 출력창 변수
myFont = pygame.font.SysFont(None, 50) #(글자체, 글자크기) None=기본글자체
 
run = True
while run:

	screen.fill(bg)
	# 사용자 입력용 숫자 키패드	
	if one.draw_button():
		print('Two')
	if two.draw_button():
		print('Two')
	if three.draw_button():
		print('Two')
	if four.draw_button():
		print('Two')
	if five.draw_button():
		print('Two')
	if six.draw_button():
		print('Two')
	if seven.draw_button():
		print('Two')
	if eight.draw_button():
		print('Two')
	if nine.draw_button():
		print('Two')
	if zero.draw_button():
		print('Two')
	if deleteNum.draw_button():
		print('Two')
	if checkNum.draw_button():
		print('Two')

# render함수로 사용자가 누른 숫자 출력(문자열이 아니면 str로 변환해야함)
	#myText = myFont.render("Hello World " + True, (0,0,255)) #(Text,anti-alias, color)

	counter_img = font.render(str(counter), True, red)
	screen.blit(counter_img, (280, 450))
	#screen.blit(myText, (100,100)) #(글자변수, 위치)







	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()