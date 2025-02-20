from PIL import Image
import pytesseract
import time
import pyautogui
import PIL
import keyboard


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

time.sleep(2.5)

found = False

img = None

i = 0




def screenshot(show_img, new_line): 
    pyautogui.click(200, 700)
    keyboard.press("d")
    keyboard.release("d")
    time.sleep(3)
    if not new_line:
        img = pyautogui.screenshot(region=(175,440, 1548, 180))
    else:
        img = pyautogui.screenshot(region=(175,510, 1548, 120))
   
    if show_img == True:
        img.show()
    return pytesseract.image_to_string(img), img

img_files = []

typeNedxt = True
result, img = screenshot(False, False)
result = result.lower()
img_files.append(img)

lineModulus = 3

running = True

print(result)

def check_similarities(old, new):
    if new == old:
        return True
    elif new[1:] == old:
        return True
    else:
        return False

if not result[0].isalpha():
    result = result[1:]


duration = 30
startTime = time.time()

reset = False

while running:
    if time.time()-startTime < duration:  
        for char in result: 
            if time.time()-startTime >= duration:
                break
            if char == "\n":
                i += 1
                keyboard.write(" ")
                if i == lineModulus:
                    i = 0
                    lineModulus = 2
                    last_word = result.split()[-1]
                    print("Last word:" + last_word)
                    result, img = screenshot(False, True)
                    result = result.lower().rstrip() + "\n"
                    if not result[0].isalpha():
                        result = result[1:]
                    first_word = result.split()[0]
                    print("First word" + first_word)

                    if check_similarities(last_word, first_word):
                        print("They are the same")
                    

                    img_files.append(img)
                    if "english" in result:
                        running = False
                        break
                    else:
                       continue
                    
            # else:
            # if char.isalpha() or char == " ":
            keyboard.press(char)
            time.sleep(0.02)
            keyboard.release(char)
        # running = False
        # for image in img_files:
        #     print("Showing image")
        #     image.show()
        #     running = False\
    else: running = False

print("Out of loop")
        


for image in img_files:
    image.show()
    running = False
