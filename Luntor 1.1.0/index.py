"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Program Name : Luntor 1.1.0

    Author : Daniel Kim
    Language : Python
    Version : 1.1.0
    Update Log : Code shortened
                 Variable optimized

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import requests
from bs4 import BeautifulSoup
import pyautogui as pg
import pyperclip
import time
from datetime import datetime as dt


now = dt.now()
weekday = dt.today().weekday()


while(True) :
    if (now.hour == 7 and now.minute == 10 and now.second == 0 and weekday != 5 and weekday != 6) :

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


        while (pg.locateOnScreen('Luntor 1.1.0/icon 1.1.0.png') == None) :
                print('Error 202 : Waiting for The Target...')
                time.sleep(1)
        iconloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/icon 1.1.0.png'))
        pg.moveTo(iconloc)
        pg.doubleClick()

        again = 1

        while (again) :
            if (pg.locateOnScreen('Luntor 1.1.0/Chatting 1.1.0.png') != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/Chatting 1.1.0.png'))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            elif (pg.locateOnScreen('Luntor 1.1.0/Chatting On 1.1.0.png') != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/Chatting On 1.1.0.png'))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            elif (pg.locateOnScreen('Luntor 1.1.0/Chatting Ringing 1.1.0.png', confidence = 0.9) != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/Chatting Ringing 1.1.0.png', confidence = 0.9))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            elif (pg.locateOnScreen('Luntor 1.1.0/Chatting Ringing On 1.1.0.png', confidence = 0.9) != None) :
                chatloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/Chatting Ringing On 1.1.0.png', confidence = 0.9))
                pg.moveTo(chatloc)
                pg.doubleClick()
                again = 0
            else :
                print('Error 202 : Waiting for The Target...')
                time.sleep(1)

        while (pg.locateOnScreen('Luntor 1.1.0/United Unions 1.1.0.png') == None) :
            print('Error 202 : Waiting for The Target...')
            time.sleep(1)
        roomloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/United Unions 1.1.0.png'))      
        pg.moveTo(roomloc)
        pg.doubleClick()
        time.sleep(1)

        
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


        while (pg.locateOnScreen('Luntor 1.1.0/Room X 1.1.0.png') == None) :
            print('Error 202 : Waiting for The Target...')
            time.sleep(1)
        RoomXloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/Room X 1.1.0.png'))      
        pg.moveTo(RoomXloc)
        pg.doubleClick()
        time.sleep(1)

        while (pg.locateOnScreen('Luntor 1.1.0/X 1.1.0.png') == None) :
            print('Error 202 : Waiting for The Target...')
            time.sleep(1)
        Xloc = pg.center(pg.locateOnScreen('Luntor 1.1.0/X 1.1.0.png'))
        pg.moveTo(Xloc)
        pg.doubleClick()
        time.sleep(1)


        now = dt.now()

    else :
        now = dt.now()
        weekday = dt.today().weekday()

        print("Not the Time... => ", now.replace(microsecond = 0))


    time.sleep(1)