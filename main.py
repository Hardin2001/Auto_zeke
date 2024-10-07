import pyautogui
import time

pyautogui.useImageNotFoundException()

def reconect():
    drop_button1 = None
    drop_button2 = None
    try:
        print("Drop Button searching...")
        drop_button1 = pyautogui.locateOnScreen('drop1.png', confidence=0.9)
    except:
        print("network connected")

    try:
        print("Drop Button searching...")
        drop_button2 = pyautogui.locateOnScreen('drop2.png', confidence=0.9)
    except:
        print("network connected")

    if (drop_button1 is not None or drop_button2 is not None):
        if (drop_button1 is not None):
            drop_button1_center = pyautogui.center(drop_button1)
            pyautogui.click(drop_button1_center)
        if (drop_button2 is not None):
            drop_button1_center = pyautogui.center(drop_button2)
            pyautogui.click(drop_button1_center)
    print("reconected")

def verify_in():
    x = 0
    accept_button_location = None
    print('Looking for button.')
    while x < 10:  
        try:
            print("Verifying...")
            accept_button_location = pyautogui.locateOnScreen('in.png', confidence=0.9)
        except:
            print("Not in game")
        x += 1
        if(accept_button_location is not None):
            print("Currently in game")
            return 0
        else :
            try:
                print("Verifying...")
                accept_button_location = pyautogui.locateOnScreen('in2.png', confidence=0.9)
            except:
                print("Not in game")
        if(accept_button_location is not None):
            print("Currently in game")
            return 0

        time.sleep(0.1)
        print("Currently not in game")
    return 1


def reject_all():
    x = 0
    accept_button_location = None
    print('Looking for button.')
    while x < 3:  
        try:
            print("Button searching...")
            accept_button_location = pyautogui.locateOnScreen('reject.png', confidence=0.9)
        except:
            print("Button not found")
        x += 1
        if(accept_button_location is not None):
            break

    if(accept_button_location is not None):
        accept_button_center = pyautogui.center(accept_button_location)
        pyautogui.click(accept_button_center)
        print("rejected")
    else:
        print("rejection not found")


def accept_all():
    accept_button_location = None
    print('Looking for accept.')
    x = 0
    while x < 5:  
        try:
            print("accept searching...")
            accept_button_location = pyautogui.locateOnScreen('accept2.png', confidence=0.7)
        except:
            print("accept not found")
        x +=1
        if(accept_button_location is not None):
            break
    
    if(accept_button_location is not None):
        accept_button_center = pyautogui.center(accept_button_location)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
        time.sleep(0.5)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
        time.sleep(0.5)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
        time.sleep(0.5)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
        time.sleep(0.5)
        print("accpeted")
    else:
        print("accpetion not found")


def click_accept_button():

    print("Game accepting phase 1")

    accept_button_location = None

    print('Looking for button.')
    while accept_button_location is None:
        reconect()
        try:
            print("Accpet 1 Button searching...")
            accept_button_location = pyautogui.locateOnScreen('accept1.png', confidence=0.7)
        except:
            print("Button not found")

    if(accept_button_location is not None):
        accept_button_center = pyautogui.center(accept_button_location)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
        pyautogui.click(accept_button_center)
    
    while (1):
        if (accept_2() == 0):
            break


def accept_2():
    b9 = None
    b10 = None
    x = 0

    print("Game accepting phase 2")

    while (b9 is None and b10 is None): 
        try:
            print("Button 9 searching...")
            b9 = pyautogui.locateOnScreen('9.png', confidence=0.9)
        except:
            print("Button 9 not found")
        try:
            print("Button 10 searching...")
            b10 = pyautogui.locateOnScreen('10.png', confidence=0.9)
        except:
            print("Button 10 not found")
        if(b9 is not None or b10 is not None):
            break
        x += 1
        if(x > 5):
            break
    if (b9 is None and b10 is None):
        reject_all()
        return 1
    else :
        accept_all()
        return 0
    

def click_exit_button():
    accept_button_location = None

    print('Looking for exiting button.')
    while accept_button_location is None:
        if (verify_in() == 1):
            break  
        time.sleep(1)

        reconect()

        try:
            print("Exit Button searching...")
            accept_button_location = pyautogui.locateOnScreen('return.png', confidence=0.9)
        except:
            print("Button not found")

    if(accept_button_location is not None):
        accept_button_center = pyautogui.center(accept_button_location)
        time.sleep(0.5)
        pyautogui.click(accept_button_center)
        print("Exiting ended game")
    
    print("restart searching games")


def main():
    game_count = 0
    while(1):
        click_accept_button()
        time.sleep(15)
        click_exit_button()
        game_count += 1
        print("game finished count:", game_count)
        time.sleep(0.3)
        reconect()

#
#
###  MAIN STRUCTURE  ###
#
#


main()