import pyautogui as pg
import time
from PIL import ImageGrab
import keyboard

# 현재 마우스 포인터 위치 반환코드
'''
while True:
    #print(pg.position())
    #time.sleep(.5)
    '''

width, height = pg.size() # 현재 페이지의 사이즈 반환
box = (0, 0, width/2, height)

taps = [(295,770), (416,770), (525,770), (644,770)]

def play():
    screen = ImageGrab.grab(box) # box : 캡처하는 부분의 좌표 왼쪽 아래와 오른쪽 위 2군데 인듯
    for tap in taps:
        if (0,0,0) == screen.getpixel(tap):  # rgb (0,0,0) : 검정
            pg.click(*tap)

state = False  # 게임 진행중이라면 True
while True:
    if not state and keyboard.is_pressed('a'):
        state = True
        print('Game Start!')
    elif state and keyboard.is_pressed('s'):
        state = False
        print('Game Stop!')
    if state:
        play()