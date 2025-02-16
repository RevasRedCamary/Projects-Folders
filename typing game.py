from tkinter import Tk, Label
import time 
import math

root=Tk()
string = "we after late very tell after hours minimum battery percentage does not have to be on that specific month"
count = 0
label = Label(text=string)
first_key = False
start_time = None
player_script = ""
#accuracy formula----correct characters/total characters * 100%
mistakes = 0


def evaluate():
    correct_characters = len(string) - mistakes
    return (correct_characters/len(string))*100
def format(acc):
    #acc = round(acc, 2)
    str_acc = str(acc)
    str_acc = str_acc+"%"
    return str_acc


def key_pressed(event):
    global first_key, count, start_time, player_script, mistakes
    if not first_key:
        first_key = True
        count = 0
        label.config(text=string)
        start_time = time.time()
    if event.keysym == "BackSpace" and count > 0:
        firstsplit = string[0:count-1]
        secondsplit = string[count-1:len(string)]
        label.config(text=firstsplit+"█"+secondsplit)
        player_script = player_script[0:len(player_script)-1]
    elif event.char == string[count]:
        firstsplit = string[0:count+1]
        secondsplit = string[count+1:len(string)]
        label.config(text=firstsplit+"█" + secondsplit)
        player_script = player_script + event.char
        count += 1
    elif event.char != string[count]:
        mistakes += 1
    if count == len(string):
        end_time = time.time()
        elapsed_time = end_time-start_time
        form_elapsed = elapsed_time/60
        wpm = round((len(string)/5)/form_elapsed, 1)
        accuracy = format(evaluate())
        label.config(text="You finished with " + str(wpm) + " WPM and " + accuracy + " accuracy!")
        time.sleep(0.1)
        first_key = False
        print(player_script)
        
label.pack()
root.bind("<Key>",key_pressed)
root.mainloop()
