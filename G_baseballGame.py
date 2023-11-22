import sys, pygame, random
from pygame.locals import *
from menu import MainMenu

class baseballGame():
	def __init__(self):
		pygame.init()
		self.running, self.playing = True, False
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
		self.DISPLAY_W, self.DISPLAY_H = 1000,600
		self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
		self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
		
		#self.font_name = '8-BIT WONDER.TTF'
		self.font_name = pygame.font.get_default_font()
		self.BLACK, self.WHTIE = (0,0,0), (255,255,255)
		self.curr_menu = MainMenu(self)

	def check_events(self):
		for  event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running, self.playing = False, False
				self.curr_menu.run_display = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.START_KEY = True
				if event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True
				if event.key == pygame.K_DOWN:
					self.DOWN_KEY = True
				if event.key == pygame.K_UP:
					self.UP_KEY = True


	def reset_keys(self):
		self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.UP_KEY = False, False, False, False
	

	def game_loop(self):
		while self.playing:
			self.check_events()
			if self.START_KEY:
				self.playing = False
			self.display.fill(self.BLACK)
			self.draw_text('Thanks for Playing',20,self.DISPLAY_W/2, self.DISPLAY_H/2)
			self.window.blit(self.display, (0,0))
			pygame.display.update()
			self.reset_keys()

	def draw_text(self, text, size, x,y):
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text, True, self.WHTIE)
		text_rect = text_surface.get_rect()
		text_rect.center = (x,y)
		self.display.blit(text_surface, text_rect)


				


   






'''
pygame.init()


screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Baseball Game')

font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = (0, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# 랜덤 변수 생성
answer = random.randrange(100,900,1)

#define global variable
clicked = False
counter = answer
firstNum = 0
secondNum = 0
thirdNum = 0

class panel():
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 100
	height = 70

	def __init__(self,x,y,answer):
		self.x = x
		self.y = y
		self.answer = answer
		
	def draw_panel(self):
		panel_rect = Rect(self.x, self.y, self.width, self.height)


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
				self.append_value(firstNum)
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

	def append_value(self,new_value):
	# Set a limit of values that can be entered
		if self.text.get_width() < 260:
			if self.value == "0" or self.new_entry:
				self.value = new_value
				self.new_entry = False
			else:
				self.value += new_value
			
		self.text = self.font.render(self.value,True,BLACK)
		# Set key_pressed as true
		self.key_pressed = True

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
panel_1 = panel(600,200,'1')


myFont = pygame.font.SysFont(None, 50) #(글자체, 글자크기) None=기본글자체
 
run = True
while run:
	screen.fill(bg)
	for turn in range(5):
		''





	
	# 사용자 입력용 숫자 키패드	
	if one.draw_button():
		firstNum = 1
		append

	if two.draw_button():
		firstNum = 2
	if three.draw_button():
		firstNum = 3
	if four.draw_button():
		firstNum = 4
	if five.draw_button():
		firstNum = 5
	if six.draw_button():
		firstNum = 6
	if seven.draw_button():
		firstNum = 7
	if eight.draw_button():
		firstNum = 8
	if nine.draw_button():
		firstNum = 9
	if zero.draw_button():
		firstNum = 0
	if deleteNum.draw_button():
		print('Two')
	if checkNum.draw_button():
		userNum = '사용자가 누르는 숫자 123'
		counter_img = font.render('ddd', True, red)
		screen.blit(counter_img, (280, 450))
		pygame.display.update() #모든 화면 그리기 업데이트

# render함수로 사용자가 누른 숫자 출력(문자열이 아니면 str로 변환해야함)
	#myText = myFont.render("Hello World " + True, (0,0,255)) #(Text,anti-alias, color)
	
	if panel_1.draw_panel():
		print('Yessssssssssssssssssssssssssssssssssss')





	counter_img = font.render(str(counter), True, red)
	screen.blit(counter_img, (280, 450))
	counter_img = font.render('Yessssssssssss', True, red)
	screen.blit(counter_img, (100, 100))
	#screen.blit(myText, (100,100)) #(글자변수, 위치)






	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()'''