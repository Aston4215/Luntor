"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Program Name : Luntor 2.0.0

    Author : Daniel Kim
    Language : Python
    Version : 2.0.0
    Update Log : Program Commercialized
                 Notice System Added
                 Back-End CUI Added

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os, subprocess, requests, pyperclip, time
from bs4 import BeautifulSoup
import pyautogui as pg
from datetime import datetime as dt

print('Console KakaoTalk Lunch Indicator, Luntor 2.0.0 in Python')
print('----------------------------------------------------------------\n')
print('Choose an Option from the Following list:')
print('\tp - Process Start in General')
print('\tn - Process Start with Notice')
print('Your Option? ', end = '')
answer = str(input())

if (answer == 'p') :
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
else :
    print('Error 707 : Input Function Error')
    exit()


now = dt.now()
weekday = dt.today().weekday()
temp = 0

while(True) :
    if (now.hour == 7 and now.minute == 0 and now.second == 0 and weekday != 5 and weekday != 6) :

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
                content_lunch = '<span class="content">Error 101 : Could not find content</span>'
                print(content_lunch.get_text())
                break


        ProcStart = subprocess.Popen('"C:/Program Files (x86)/Kakao/KakaoTalk/KakaoTalk.exe"')
        if (ProcStart.poll() != None) :
            print('Error 606 : Could not start Process')
            exit()

        again = 1

        while (again) :
            if (pg.locateOnScreen('Luntor 2.0.0/Chatting.png') != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 2.0.0/Chatting.png'))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            elif (pg.locateOnScreen('Luntor 2.0.0/Chatting On.png') != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 2.0.0/Chatting On.png'))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            elif (pg.locateOnScreen('Luntor 2.0.0/Chatting Ringing.png', confidence = 0.9) != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 2.0.0/Chatting Ringing.png', confidence = 0.9))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            elif (pg.locateOnScreen('Luntor 2.0.0/Chatting Ringing On.png', confidence = 0.9) != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 2.0.0/Chatting Ringing On.png', confidence = 0.9))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            else :
                print('Error 202 : Waiting for The Target...')
                time.sleep(1)

        while (pg.locateOnScreen('Luntor 2.0.0/Chatting Room.png') == None) :
            print('Error 202 : Waiting for The Target...')
            time.sleep(1)
        roomloc = pg.center(pg.locateOnScreen('Luntor 2.0.0/Chatting Room.png'))
        pg.moveTo(roomloc)
        pg.doubleClick()
        time.sleep(1)

        
        if (answer == 'u') :
            pg.write('[Luntor ' + str(version) + ' has been released!]')
            pg.hotkey('shift', 'enter')
            pg.hotkey('shift', 'enter')
            pg.write('Update Log :')
            pg.hotkey('shift', 'enter')
            for i in range(logcount) :
                pg.write('    ' + str(i + 1) + '. ' + str(locals()['log' + str(i)]))
                pg.hotkey('shift', 'enter')
            pg.hotkey('shift', 'enter')
            pg.write('Please Enjoy the Service!')
            pg.hotkey('shift', 'enter')
            pyperclip.copy("[COPYRIGHT © 2022 김태윤")
            pg.hotkey('ctrl', 'v')
            pg.hotkey('shift', 'enter')
            pg.write('ALL Rights Reserved.]\n')
        elif (answer == 'a') :
            pg.write('[' + str(notice) + ']\n')

        
        if (weekday == 0) : weekday_text = '(월)'
        elif (weekday == 1) : weekday_text = '(화)'
        elif (weekday == 2) : weekday_text = '(수)'
        elif (weekday == 3) : weekday_text = '(목)'
        elif (weekday == 4) : weekday_text = '(금)'
        else :
            print('Error 505 : Variable error')
            exit()
        pyperclip.copy('[성덕고등학교] ' + dt.today().strftime('%Y-%m-%d') + weekday_text)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('shift', 'enter')
        pg.hotkey('shift', 'enter')

        pyperclip.copy("[중식]")
        pg.hotkey('ctrl', 'v')
        pg.hotkey('shift', 'enter')
        pyperclip.copy(content_lunch.get_text())
        pg.hotkey('ctrl', 'v')


        if (weekday != 2) :

            content_dinner = None
            i = 0
            while (content_dinner == None) :
                content_dinner = soup.select_one('#xb_fm_list > div.calendar > ul:nth-child(' + str(i) + ') > li.today > div > dl > dd.con3 > div.content_info > span')
                i += 1
                if (i == 10) :
                    content_dinner = '<span class="content">Error 101 : Could not find content</span>'
                    print(content_dinner.get_text())
                    break

            pg.hotkey('shift', 'enter')
            pg.hotkey('shift', 'enter')
            pyperclip.copy("[석식]")
            pg.hotkey('ctrl', 'v')
            pg.hotkey('shift', 'enter')
            pyperclip.copy(content_dinner.get_text())
            pg.hotkey('ctrl', 'v')
        
        pg.write('\n')


        os.system('taskkill /f /im KakaoTalk.exe')


        now = dt.now()

    else :
        now = dt.now()
        weekday = dt.today().weekday()

        if (temp == 0) :
            print("Not the Time... =>", now.replace(microsecond = 0), end = '')
            temp = 1
        else :
            print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", now.replace(microsecond = 0), end = '')


    time.sleep(1)