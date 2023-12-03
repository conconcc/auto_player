import cv2
import numpy as np
import pyautogui
import time
import os

def find_image(template_path, threshold=0.8):
    # 화면 캡처
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    # 경로에서 템플릿 이미지 로드
    template = cv2.imread(template_path)
    h, w = template.shape[:-1]

    # 캡처와 이미지 매칭
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    return loc
def check_and_skip(template_path, side):
    loc = find_image(template_path)

    # 특정 위치에서 매칭이 확인되면 동영상 스킵 수행
    if loc[0].size > 0 and loc[1].size > 0:
        print(f"특정 영역이 화면에 나타남. 동영상 스킵을 수행합니다.")

        # 동영상 스킵 및 특정 위치로 이동
        if side == 'left':
            pyautogui.moveTo(765, 10, duration=0.5)
            pyautogui.mouseDown()
        else:
            pyautogui.moveTo(1750, 20, duration=0.5)
            pyautogui.mouseDown()
        pyautogui.hotkey('shift', 'n')
        pyautogui.mouseUp()
        quit()

    else:
        print("특정 영역이 화면에 나타나지 않음.")
def run(side):
    # 템플릿 이미지의 경로를 설정 스크립트 = 현재 스크립트가 실행되는 디렉토리
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # 폴더 안에 있는 파일 경로 설정
    folder_path = os.path.join(script_directory, "icon")
    file_path = os.path.join(folder_path, "replay.PNG")

    # 일정 시간마다 특정 영역 확인 및 동영상 스킵
    while True:
        check_and_skip(file_path, side)
        time.sleep(10)

        print("특정 영역이 화면에 나타나지 않음.")
