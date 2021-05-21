import pyautogui
import time
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\18043\AppData\Local\Programs\Tesseract-OCR\\tesseract.exe'


def Reps():
    pyautogui.moveTo(1221, 767)
    pyautogui.click()

    time.sleep(1)

    im = pyautogui.screenshot(region=(1298, 685, 50, 30))
    im.save('yolo.png')

    img = cv2.imread('yolo.png')

    text = pytesseract.image_to_string(img)
    print(text)

    pyautogui.moveTo(500, 300)
    pyautogui.click()

    time.sleep(20)

    pyautogui.moveTo(1221, 767)
    pyautogui.click()

    time.sleep(1)

    im = pyautogui.screenshot(region=(1298, 685, 50, 30))
    im.save('yolo.png')

    img = cv2.imread('yolo.png')

    text1 = pytesseract.image_to_string(img)
    print(text1)

    pyautogui.moveTo(500, 300)
    pyautogui.click()

    if text == text1:
        quit()

    else:
        pyautogui.press('space')
        time.sleep(20 * 60)
        pyautogui.press('space')
        return 'yes'

    return


f = pyautogui.prompt(text='How long would you like the timer to be?(in minutes)', title='Netflix Timer', default='')

try:
    int(f)

except:
    pyautogui.alert(text='Not compatible please try again.', title='Oops')
    quit()

Minutes = int(f) * 60
time.sleep(Minutes)

pyautogui.press('space')

if Reps() == 'yes':
    if Reps() == 'yes':
        if Reps() == 'yes':
            if Reps() == 'yes':
                pass
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass
