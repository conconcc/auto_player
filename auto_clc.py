import cv2
import numpy as np
import pyautogui
import time

def get_color(x, y):
    # 화면 캡처
    screenshot = pyautogui.screenshot()

    # Pillow Image를 OpenCV BGR 형식으로 변환
    screenshot = np.array(screenshot)

    # 특정 위치 (x, y)의 픽셀 색상 얻기
    color = screenshot[y, x]
    # 색상값을 정수로 변경한 값 반환
    return tuple(map(int, color))


def check(x, y, initial_color, tolerance=10, timeout=3600):
    
    start_time = time.time()
    while time.time() - start_time <= timeout:
        # 현재 색상 가져오기
        current_color = get_color(x, y) 
        # 이전 색상과 현재 색상 비교
        print("색상 비교를 실시합니다.")
        color_difference = np.abs(np.subtract(initial_color, current_color))

        # 특정 픽셀 색상의 변경을 감지하는 기준 값
        threshold = np.array([tolerance, tolerance, tolerance])
        
        # 색상 변경 여부 확인
        if np.any(color_difference > threshold):
            print("색상이 변경되었습니다. 클릭을 수행합니다.")
            break  # 색상이 변경되면 반복 종료
        else:
            print("색상 변경이 확인되지 않았습니다.")
        time.sleep(10)  # 1초마다 확인 (원하는 주기로 조절)

    print("색상 비교를 종료합니다.")



def click(next,ok,done,play):
    print("클릭을 실행합니다.")
    previous_color=get_color(ok[0],ok[1])
    pyautogui.click(next[0],next[1],duration=0.5)
    time.sleep(1)
    current_color = get_color(ok[0], ok[1])
    while(True):
        if current_color != previous_color:
            print("확인 위치의 색이 다름을 판별하였습니다. ")
            pyautogui.click(ok[0],ok[1],duration=0.5)
            pyautogui.doubleClick(ok[0], ok[1],duration=0.5)
            time.sleep(1)
            pyautogui.click(done[0],done[1],duration=1)
            time.sleep(1)
            quit()
        pyautogui.click(play[0],play[1],duration=0.5)


def run(side):
    global color,next,ok,done,play
    color=0,0
    next=0,0
    ok=0,0
    done=0,0
    play=0,0
    if side == "left":
        color=(900,750)
        next=(800,1015)
        ok=(675,180)
        done=(700,1007)
        play=(602,537)
    elif side == "right":
        color=(1850,750)
        next=(1750,1010)
        ok=(1638,177)
        done=(1855,1016)
        play=(1567,535)
    elif side == "main":
        color=(1850,750)
        next=(1750,1010)
        ok=(1155,170)
        done=(1855,1016)
        play=(1080,530)
    
    while True:
        # 초기 색상 가져오기 (최초 1회만 실행)
        initial_color = get_color(color[0], color[1])
        # 색상이 변경될 때까지 반복 (최대 1시간)
        check(color[0], color[1], initial_color)
        click(next,ok,done,play)
