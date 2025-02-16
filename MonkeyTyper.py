from PIL import Image
import pytesseract
import time
import pyautogui
import PIL
import keyboard

#

pytesseract.pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/5.2.0/bin/tesseract"

time.sleep(2.5)

found = False

img = None

i = 1



def screenshot(show_img, new_line): 
    pyautogui.click(200, 700)
    keyboard.press("d")
    keyboard.release("d")
    if not new_line:
        img = pyautogui.screenshot(region=(175, 750, 2500, 300))
    else:
        img = pyautogui.screenshot(region=(175, 950, 2500, 100))
   
    if show_img == True:
        img.show()
    return pytesseract.image_to_string(img), img

img_files = []

typeNedxt = True
startTime = time.time()
result, img = screenshot(False, False)
img_files.append(img)

lineModulus = 3



while True:
    if time.time()-startTime < 30:  
        for char in result: 
            if char == "\n":
                i += 1
                keyboard.write(" ")
                if i == lineModulus:
                    i = 1
                    lineModulus = 2
                    result, img = screenshot(False, True)
                    img_files.append(img)
                    if "to save your result" in result:
                        print("broken value: " + result)
                        break
                    else:
                       print(result)
                    
            else:
                if not char == "©":
                    keyboard.press(char)
                    keyboard.release(char)
    else:
       for image in img_files:
           image.show()
       break


