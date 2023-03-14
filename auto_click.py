import datetime
import time
import pyttsx3
import time
import os
import subprocess
import re
import time
import os
import subprocess
# import pygame
import pyautogui
import datetime
import threading
import keyboard

from color_log_print import *
import time
import datetime
#pip install pyautogui #for auto click on the screen
import pyautogui
#pip install keyboard #keyboard
import keyboard
import threading

#color text
cClear = '\033[0m'
cBlack = '\033[30m'
cRed = '\033[31m'
cGreen = '\033[32m'
cYellow = '\033[33m'
cBlue = '\033[34m'
cMagenta = '\033[35m'
cCyan = '\033[36m'
cWhite = '\033[37m'
cBright_Black = '\033[30;1m'    #or '\033[1;30m
cBright_Red = '\033[31;1m'      #or '\033[1;31m
cBright_Green = '\033[32;1m'    #or '\033[1;32m
cBright_Yellow = '\033[33;1m'   #or '\033[1;33m
cBright_Blue = '\033[34;1m'     #or '\033[1;34m
cBright_Magenta = '\033[35;1m'  #or '\033[1;35m
cBright_Cyan = '\033[36;1m'     #or '\033[1;36m
cBright_White = '\033[37;1m'    #or '\033[1;37m
cLight_Gray = '\033[90m'
cDark_Red = '\033[91m'
cDark_Green = '\033[92m'
cDark_Yellow = '\033[93m'

#==================================================[Auto click]============================================================
buffer_keyboard_typed = []
# Set the position where you want to click
x_location, y_location = 5, 5 #1999, 1418
enable_auto_click = False
auto_click_timer = 3 #minute
enable_move_cursor_smartly = False
x_location_current_bak = -1
y_location_current_bak = -1
count_toggle = 0 #for toggle

minute_backup1 = -1     
# Loop forever
def auto_click(input_minute):
    global minute_backup1
    global count_toggle
    global x_location_current_bak, y_location_current_bak
    global buffer_keyboard_typed

    if input_minute != minute_backup1:
        minute_backup1 = input_minute
    else:
        return
    # Wait for 1s
    # time.sleep(1)
    x_location_current, y_location_current = pyautogui.position()
    # print(f"begin {x_location_current_bak}, {y_location_current_bak}")  
    # print(f"check {x_location_current}, {y_location_current}")  
    if not enable_move_cursor_smartly:
        pyautogui.click(x=x_location, y=y_location)
        #move to previos position before cliking
        pyautogui.moveTo(x_location_current, y_location_current)
        print(f"\t\t{cGreen}--> auto click at: [x = {x_location}, y = {y_location}]{cClear}")
    else:
        if len(buffer_keyboard_typed) == 0 and x_location_current == x_location_current_bak and y_location_current == y_location_current_bak:
            pyautogui.click(x=x_location, y=y_location)
            #move to previos position before cliking
            count_toggle += 1
            if count_toggle > 100:
                count_toggle = 0
            if count_toggle % 2 == 0:
                pyautogui.moveTo(x_location_current+1, y_location_current+1)
            else:
                pyautogui.moveTo(x_location_current-1, y_location_current-1)
            print(f"\t\t{cGreen}--> smart auto [clicked], can't detect [cursor moving or typing] in the [time = {auto_click_timer}] minutes, at: [x = {x_location}, y = {y_location}]{cClear}")  
        else:
            if len(buffer_keyboard_typed) != 0:
                buffer_keyboard_typed = []
                print(f"\t\t{cRed}--> smart auto [not click], detect [typing] in the [time = {auto_click_timer}] minutes{cClear}")   
            else:
                print(f"\t\t{cRed}--> smart auto [not click], detect [cursor moving] in the [time = {auto_click_timer}] minutes{cClear}")   

#Setting mouse cursor for auto click
while True:
    try:
        enable_auto_click_ = input(f"\n==> Auto click, {cGreen}[YES: type any thing] {cRed}[NO: enter]{cClear}\t")
        if enable_auto_click_ !=  "":
            enable_auto_click = True
            #for set timer click
            print("\t- current timer for auto click: [time = {auto_click_timer}] minutes".format(auto_click_timer = auto_click_timer))
            change_timer = input(f"\t- change timer? {cGreen}[YES: type number of minute in range (2-59)] {cRed}[NO: enter]{cClear}\t")
            if change_timer != "":
                auto_click_timer = int(change_timer)
                if auto_click_timer < 2:
                    auto_click_timer = 2
            print("\t- timer set: [time = {auto_click_timer}] minutes".format(auto_click_timer = auto_click_timer))
            # auto_click_timer = auto_click_timer*60 #convert to second
            move_cursor_smartly_not_click = input(f"\t- move cursor smartly, auto detect moving? {cRed}[No: type any thing] {cGreen}[YES: enter]{cClear}\t")
            if move_cursor_smartly_not_click != "":
                #for set position click
                print("\t- current position: [x = {x}, y = {y}]".format(x = x_location, y = y_location))
                change_position = input(f"\t- change position? {cGreen}[YES: type any thing] {cRed}[NO: enter]{cClear}\t")
                if change_position != "":
                    print("\t- move the cursor to new position and waiting 10 seconds to get current cursor")
                    for i in range(1,10):
                        time.sleep(1)
                    x_location, y_location = pyautogui.position()
                print("\t- auto click [ON] and new position set: [x = {x}, y = {y}]".format(x = x_location, y = y_location))
            else:
                enable_move_cursor_smartly = True
                print("\t- auto move cursor smartly [ON]")
        break
    except:
        enable_auto_click = False
        print("\n==> Error when Setting mouse cursor for auto click, Try again!")

def handle_keyboard_events():
    global buffer_keyboard_typed
    print("\n==> Create thread to detect typing")
    while True:
        time.sleep(2)
        key = keyboard.read_event()
        if key.event_type == 'down':
            buffer_keyboard_typed.append(key.name)
        if len(buffer_keyboard_typed) > 100:
            buffer_keyboard_typed = []
            buffer_keyboard_typed.append("Init")

if enable_auto_click:
    keyboard_thread = threading.Thread(target=handle_keyboard_events)
    keyboard_thread.daemon = True
    keyboard_thread.start()

#================================================================[MAIN]======================================================
#Loop forever every 1s
if enable_auto_click:
    print("\n==> All ok, let timer begin!")

while enable_auto_click:
    #count timer each second
    time.sleep(1)
    #for print check if alive
    now = datetime.datetime.now()
    seconds = int(now.strftime("%S"))
    minutes = int(now.strftime("%M"))
    hours  = int(now.strftime("%H"))
    days   = int(now.strftime("%d"))
    months = int(now.strftime("%m"))
    year   = int(now.strftime("%Y"))

    # Convert to 12-hour format and determine AM/PM
    hour = hours
    am_pm = ""
    if hours >= 12:
        am_pm = "PM"
        hour -= 12

    arrow = " " + "=" * seconds + ">"
    print(f"\r{cMagenta}{cBright_White} {days}/{months}/{str(year)[2:4]} {cBright_Blue}{hour}:{minutes}:{seconds} {cMagenta} {am_pm} {cLight_Gray}{arrow}{cClear}", end="")
    #reset timer
    if enable_auto_click and minutes % auto_click_timer == 0:
        auto_click(minutes)    
        # time.sleep(0.2)
        x_location_current_bak, y_location_current_bak = pyautogui.position()   
        # print(f"end {x_location_current_bak}, {y_location_current_bak}")                 
#====================================================[Nothing]============================================================
#just for not disapear in the terminal windown
print("\n==> End program!")
ttt = input()