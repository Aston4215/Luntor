"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Program Name : Luntor 2.2.0

    Author : Daniel Kim
    Language : Python
    Version : 2.2.0
    Update Log : Running Process in CMD
                 Code Shortened

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os, subprocess, requests, pyperclip, time, win32con, win32api, win32gui
from bs4 import BeautifulSoup
from datetime import datetime as dt
import pyautogui as pg

def ctrl_chatroom(function, chatroom_name):
    kakao = win32gui.FindWindow(None, "카카오톡")
    kakao_edit1 = win32gui.FindWindowEx( kakao, None, "EVA_ChildWindow", None)
    kakao_edit2_1 = win32gui.FindWindowEx( kakao_edit1, None, "EVA_Window", None)
    kakao_edit2_2 = win32gui.FindWindowEx( kakao_edit1, kakao_edit2_1, "EVA_Window", None)
    kakao_edit3 = win32gui.FindWindowEx( kakao_edit2_2, None, "Edit", None)

    if (function == 0) :
        win32api.SendMessage(kakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    elif (function == 1) :
        win32api.SendMessage(kakao_edit3, win32con.WM_SETTEXT, 0, '')
    else :
        print('Error 505 : Variable error')
        exit()
    time.sleep(1)
    win32api.PostMessage(kakao_edit3, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(kakao_edit3, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(1)

def enter (index) :
    for i in range(index) : pg.hotkey('shift', 'enter')
    time.sleep(0.01)

def write (statement) :
    pyperclip.copy(statement)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.01)

now = dt.now()
weekday = dt.today().weekday()
temp = 0
passive = 0
error_l = 0
error_d = 0

print('Console KakaoTalk Lunch Indicator, Luntor 2.2.0 in Python')
print('----------------------------------------------------------------\n')
print('Choose an Option from the Following list:')
print('\tg - Process Start in General')
print('\tn - Process Start with Notice')
print('\tp - Process Start passively')
print('Your Option? ', end = '')
answer = str(input())

if (answer == 'g') :
    print('Process Starting...')
elif (answer == 'n') :
    print('Choose an Option from the Following list:')
    print('\tu - Update Notice')
    print('\ta - Another Notice')
    print('Your Option? ', end = '')
    answer = str(input())
    if (answer == 'u') :
        print('Enter the Version : ', end = '')
        version = str(input())
        print('Enter the Number of Update Log : ', end = '')
        logcount = int(input())
        for i in range(logcount) :
             print('Enter the Update Log : ', end = '')
             locals()['log' + str(i)] = str(input())
        print('Process Starting...')
    elif (answer == 'a') :
        print('Enter the Notice : ', end = '')
        notice = str(input())
        print('Process Starting...')
    else :
        print('Error 707 : Input Function Error')
        exit()
elif (answer == 'p') :
    print('Process Starting...')
    passive = 1
else :
    print('Error 707 : Input Function Error')
    exit()


while(True) :
    if ((now.hour == 7 and now.minute == 0 and now.second == 0 and weekday != 5 and weekday != 6) or passive == 1) :

        print('\n')

        response = requests.get('http://seongdeok.gen.hs.kr/xboard/board.php?tbnum=35')
        soup = BeautifulSoup(response.text, 'html.parser')
        if (response.status_code != 200) :
            print('Error 404 : Website access denied')
            exit()

        content_lunch = None
        i = 0
        while (content_lunch == None) :
            content_lunch = soup.select_one('#xb_fm_list > div.calendar > ul:nth-child(' + str(i) + ') > li.today > div > dl > dd.con2 > div.content_info > span')
            i += 1
            if (i == 10) :
                content_lunch = 'Error 101 : Could not find content'
                error_l = 1
                print(content_lunch)
                break

        
        ctrl_chatroom(0, "2022 성덕고 1-11")

        
        if (answer == 'u') :
            write('[Luntor ' + str(version) + ' has been released!]')
            enter(2)
            write('Update Log :')
            enter(1)
            for i in range(logcount) :
                write('    ' + str(i + 1) + '. ' + str(locals()['log' + str(i)]))
                enter(1)
            enter(1)
            write('Please Enjoy the Service!')
            enter(1)
            write("[COPYRIGHT © 2022 김태윤")
            enter(1)
            write('ALL Rights Reserved.]')
            pg.write('\n')
        elif (answer == 'a') :
            write('[Notice]')
            enter(1)
            write(str(notice))
            pg.write('\n')
        
        if (weekday == 0) : weekday_text = '(월)'
        elif (weekday == 1) : weekday_text = '(화)'
        elif (weekday == 2) : weekday_text = '(수)'
        elif (weekday == 3) : weekday_text = '(목)'
        elif (weekday == 4) : weekday_text = '(금)'
        else :
            print('Error 505 : Variable error')
            exit()
        write('[성덕고등학교] ' + dt.today().strftime('%Y-%m-%d') + weekday_text)
        enter(2)

        write("[중식]")
        enter(1)
        if (error_l == 0) : write(content_lunch.get_text())
        else : write(content_lunch)

        if (weekday != 2) :

            content_dinner = None
            i = 0
            while (content_dinner == None) :
                content_dinner = soup.select_one('#xb_fm_list > div.calendar > ul:nth-child(' + str(i) + ') > li.today > div > dl > dd.con3 > div.content_info > span')
                i += 1
                if (i == 10) :
                    content_dinner = 'Error 101 : Could not find content'
                    error_d = 1
                    print(content_dinner)
                    break

            enter(2)
            write("[석식]")
            enter(1)
            if (error_d == 0) : write(content_dinner.get_text())
            else : write(content_dinner)
        
        pg.write('\n')


        ctrl_chatroom(1, '2022 성덕고 1-11')
        os.system('taskkill /f /im KakaoTalk.exe')


        now = dt.now()
        temp = 0
        passive = 0

    else :
        now = dt.now()
        weekday = dt.today().weekday()

        if (temp == 0) :
            print("Not the Time... =>", now.replace(microsecond = 0), end = '')
            temp = 1
        else :
            print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", now.replace(microsecond = 0), end = '')

    time.sleep(1)