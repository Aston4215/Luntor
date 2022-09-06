"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Program Name : Luntor 1.0.0

    Author : Daniel Kim
    Language : Python
    Version : 1.0.0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import requests
from bs4 import BeautifulSoup
import pyautogui as pg
import pyperclip
import time
import datetime as dt


now = dt.datetime.now()
weekday = dt.datetime.today().weekday()


while (1) :
    if (now.hour == 7 and now.minute == 10 and now.second == 0 and weekday != 5 and weekday != 6) :
        url = 'http://seongdeok.gen.hs.kr/main/main.php'

        response = requests.get(url)

        if response.status_code == 200:
    
            html_month = response.text
            soup_month = BeautifulSoup(html_month, 'html.parser')
            title_month = soup_month.select_one('#container > div.default_layout > div.col_box.food > p > span:nth-child(1)')
            #print(title_month.get_text())

            html_date = response.text
            soup_date = BeautifulSoup(html_date, 'html.parser')
            title_date = soup_date.select_one('#container > div.default_layout > div.col_box.food > p > span:nth-child(2)')
            #print(title_date.get_text())

            html_day = response.text
            soup_day = BeautifulSoup(html_day, 'html.parser')
            title_day = soup_day.select_one('#container > div.default_layout > div.col_box.food > p > span.f_con2')
            #print(title_day.get_text())

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.select_one('#food_cont > p > a')
            #print(title.get_text())

    

            while (pg.locateOnScreen('icon.png') == None) :
                print('Error 101. Waiting...')
                time.sleep(1)
            iconloc = pg.center(pg.locateOnScreen('icon.png'))
            pg.moveTo(iconloc)
            pg.doubleClick()


            again = 1

            while (again) :
                if (pg.locateOnScreen('Chatting.png') != None) :
                    chatloc = pg.center(pg.locateOnScreen('Chatting.png'))
                    pg.moveTo(chatloc)
                    pg.doubleClick()
                    again = 0
                elif (pg.locateOnScreen('Chatting On.png') != None) :
                    chatloc = pg.center(pg.locateOnScreen('Chatting On.png'))
                    pg.moveTo(chatloc)
                    pg.doubleClick()
                    again = 0
                elif (pg.locateOnScreen('Chatting Ringing.png', confidence = 0.9) != None) :
                    chatloc = pg.center(pg.locateOnScreen('Chatting Ringing.png', confidence = 0.9))
                    pg.moveTo(chatloc)
                    pg.doubleClick()
                    again = 0
                elif (pg.locateOnScreen('Chatting Ringing On.png', confidence = 0.9) != None) :
                    chatloc = pg.center(pg.locateOnScreen('Chatting Ringing On.png', confidence = 0.9))
                    pg.moveTo(chatloc)
                    pg.doubleClick()
                    again = 0
                else :
                    print('Error 101. Waiting...')
                    time.sleep(1)
        


            while (pg.locateOnScreen('United Unions.png') == None) :
                print('Error 101. Waiting...')
                time.sleep(1)
            roomloc = pg.center(pg.locateOnScreen('United Unions.png'))      
            pg.moveTo(roomloc)
            pg.doubleClick()
            time.sleep(1)
    

            pg.write("[")

            pyperclip.copy(title_month.get_text())
            pg.hotkey('ctrl', 'v')
            pyperclip.copy('월 ')
            pg.hotkey('ctrl', 'v')

            pyperclip.copy(title_date.get_text())
            pg.hotkey('ctrl', 'v')
            pyperclip.copy('일 ')
            pg.hotkey('ctrl', 'v')

            pyperclip.copy(title_day.get_text())
            pg.hotkey('ctrl', 'v')
            pyperclip.copy('요일')
            pg.hotkey('ctrl', 'v')

            pg.write("]")
            pg.hotkey('shift', 'enter')
            pg.hotkey('shift', 'enter')

            pg.write("[")
            pyperclip.copy("중식")
            pg.hotkey('ctrl', 'v')
            pg.write("]")
            pg.hotkey('shift', 'enter')

            pyperclip.copy(title.get_text())
            pg.hotkey('ctrl', 'v')
            

            if (weekday != 2) :
                 url = 'http://seongdeok.gen.hs.kr/xboard/board.php?tbnum=35'
                 response = requests.get(url)
                 html_night = response.text
                 soup_night = BeautifulSoup(html_night, 'html.parser')
                 title_night = soup_night.select_one('#xb_fm_list > div.calendar > ul:nth-child(3) > li.today > div > dl > dd.con3 > div.content_info > span')
                 if (title_night == None) :
                    title_night = soup_night.select_one('#xb_fm_list > div.calendar > ul:nth-child(4) > li.today > div > dl > dd.con3 > div.content_info > span')
                 if (title_night == None) :
                    title_night = soup_night.select_one('#xb_fm_list > div.calendar > ul:nth-child(5) > li.today > div > dl > dd.con3 > div.content_info > span')
                 if (title_night == None) :
                    title_night = soup_night.select_one('#xb_fm_list > div.calendar > ul:nth-child(6) > li.today > div > dl > dd.con3 > div.content_info > span')
                 #print(title_night.get_text())
                 
                 pg.hotkey('shift', 'enter')
                 pg.hotkey('shift', 'enter')
                 pg.write("[")
                 pyperclip.copy("석식")
                 pg.hotkey('ctrl', 'v')
                 pg.write("]")
                 pg.hotkey('shift', 'enter')

                 pyperclip.copy(title_night.get_text())
                 pg.hotkey('ctrl', 'v')


            pg.write("\n")

            while (pg.locateOnScreen('Room X.png') == None) :
                print('Error 101. Waiting...')
                time.sleep(1)
            RoomXloc = pg.center(pg.locateOnScreen('Room X.png'))      
            pg.moveTo(RoomXloc)
            pg.doubleClick()
            time.sleep(1)

            while (pg.locateOnScreen('X.png') == None) :
                print('Error 101. Waiting...')
                time.sleep(1)
            Xloc = pg.center(pg.locateOnScreen('X.png'))
            pg.moveTo(Xloc)
            pg.doubleClick()
            time.sleep(1)


            now = dt.datetime.now()


        else : 
            print("Error 404. => ", response.status_code)
            break
    else :
        now = dt.datetime.now()
        weekday = dt.datetime.today().weekday()

        print("Not the Time... => ", now.replace(microsecond = 0))
        

    time.sleep(1)