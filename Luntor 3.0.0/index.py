"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Program Name : Luntor 3.0.0

    Author : Daniel Kim
    Language : Python
    Version : 3.0.0
    Update Log : Canvas System Added

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import requests, pyperclip, time, win32con, win32api, win32gui
from bs4 import BeautifulSoup
from datetime import datetime as dt
import pyautogui as pg


def parse_content(index):
    response = requests.get(
        'http://seongdeok.gen.hs.kr/xboard/board.php?tbnum=35')
    soup = BeautifulSoup(response.text, 'html.parser')
    if (response.status_code != 200):
        print('Error 404 : Website access denied')
        exit()

    content = None
    i = 0
    while (content == None):
        content = soup.select_one('#xb_fm_list > div.calendar > ul:nth-child(' + str(
            i) + ') > li.today > div > dl > dd.con' + (str(2) if index == 'lunch' else str(3)) + ' > div.content_info > span')
        i += 1
        if (i == 10):
            print('Error 101 : Could not find content')
            exit()

    if (content.get_text() == ''):
        content_text = '등록된 식단이 없습니다'
    else:
        content_text = content.get_text()

    return content_text


def ctrl_chatroom(function, chatroom_name):
    kakao = win32gui.FindWindow(None, "카카오톡")
    kakao_edit1 = win32gui.FindWindowEx(kakao, None, "EVA_ChildWindow", None)
    kakao_edit2_1 = win32gui.FindWindowEx(kakao_edit1, None, "EVA_Window", None)
    kakao_edit2_2 = win32gui.FindWindowEx(kakao_edit1, kakao_edit2_1, "EVA_Window", None)
    kakao_edit3 = win32gui.FindWindowEx(kakao_edit2_2, None, "Edit", None)

    if (function == 'open'):
        win32api.SendMessage(
            kakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    elif (function == 'close'):
        win32api.SendMessage(kakao_edit3, win32con.WM_SETTEXT, 0, '')
        pg.hotkey('alt', 'f4')
    else:
        print('Error 505 : Variable error')
        exit()

    time.sleep(1)
    win32api.PostMessage(kakao_edit3, win32con.WM_KEYDOWN,
                         win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(kakao_edit3, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(1)

def write_canvas():
    canvas = open('canvas.txt', 'r', -1, 'utf-8')
    pyperclip.copy(str(canvas.read()))
    pg.hotkey('ctrl', 'v')
    pg.write('\n')
    canvas.close()


now = dt.now()
weekday = dt.today().weekday()
passive = 0
Print_Time_Notice = 1

print('Console KakaoTalk Lunch Indicator, Luntor 3.0.0 in Python')
print('----------------------------------------------------------------\n')
print('Choose an Option from the Following list:')
print('\tg - Process Start in General')
print('\tn - Process Start with Notice')
print('\tp - Process Start passively')
print('Your Option? ', end='')
answer = str(input())

if (answer == 'g'):
    print('Process Starting...')
elif (answer == 'n'):
    print('Choose an Option from the Following list:')
    print('\tu - Update Notice')
    print('\ta - Another Notice')
    print('Your Option? ', end='')
    answer = str(input())
    if (answer == 'u'):
        print('Enter the Version : ', end='')
        version = str(input())
        print('Enter the Number of Update Log : ', end='')
        logcount = int(input())
        for i in range(logcount):
             print('Enter the Update Log : ', end='')
             locals()['log' + str(i)] = str(input())
        print('Process Starting...')
    elif (answer == 'a'):
        print('Enter the Notice : ', end='')
        notice = str(input())
        print('Process Starting...')
    else:
        print('Error 707 : Input Function Error')
        exit()
elif (answer == 'p'):
    print('Process Starting...')
    passive = 1
else:
    print('Error 707 : Input Function Error')
    exit()


while (True):
    if ((now.hour == 7 and now.minute == 0 and now.second == 0 and weekday != 5 and weekday != 6) or passive == 1):
        print('\n')

        now = dt.now()
        passive = 0
        Print_Time_Notice = 1

        ctrl_chatroom('open', '2022 성덕고 1-11')

        if (answer == 'u'):
            canvas = open('canvas.txt', 'w', -1, 'utf-8')
            canvas.write('[Luntor ' + str(version) + ' has been released!]\n')
            canvas.write('\n')
            canvas.write('Update Log :\n')
            for i in range(logcount):
                canvas.write('    ' + str(i + 1) + '. ' + str(locals()['log' + str(i)]) + '\n')
            canvas.write('\n')
            canvas.write('Please Enjoy the Service!\n')
            canvas.write('[COPYRIGHT 2022 Team.\nCrypto ALL Rights Reserved.]')
            canvas.close()
            write_canvas()
            time.sleep(0.01)
            answer = 'g'
        elif (answer == 'a'):
            canvas = open('canvas.txt', 'w', -1, 'utf-8')
            canvas.write('[Notice]\n')
            canvas.write(str(notice))
            canvas.close()
            write_canvas()
            time.sleep(0.01)
            answer = 'g'

        if (weekday == 0):
            weekday_text = '(월)'
        elif (weekday == 1):
            weekday_text = '(화)'
        elif (weekday == 2):
            weekday_text = '(수)'
        elif (weekday == 3):
             weekday_text = '(목)'
        elif (weekday == 4):
            weekday_text = '(금)'
        else:
            print('Error 505 : Variable error')
            exit()

        content_lunch = parse_content('lunch')
        content_dinner = parse_content('dinner')

        canvas = open('canvas.txt', 'w', -1, 'utf-8')
        canvas.write('[성덕고등학교] ' + dt.today().strftime('%Y-%m-%d') + weekday_text + '\n')
        canvas.write('\n')
        canvas.write('[중식]\n')
        canvas.write(content_lunch + '\n')
        if (weekday != 2):
            canvas.write('\n')
            canvas.write('[석식]\n')
            canvas.write(content_dinner)
        canvas.close()
        
        write_canvas()
        ctrl_chatroom('close', None)

    else :
        now = dt.now()
        weekday = dt.today().weekday()

        if (Print_Time_Notice == 1) :
            print("Not the Time... =>", now.replace(microsecond = 0), end = '')
            Print_Time_Notice = 0
        else :
            print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", now.replace(microsecond = 0), end = '')
        
        time.sleep(1)