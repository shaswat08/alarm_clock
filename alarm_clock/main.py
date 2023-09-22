from playsound import playsound  #module to play sound
import time  #time module

CLEAR = "\033[2J" 
CLEAR_AND_RETURN = "\033[H"

def alarm_clock(second):

    time_elapsed = 0
    print(CLEAR)  #clears the screen
    
    while time_elapsed < second:

        time.sleep(1)
        time_elapsed += 1

        time_left = second - time_elapsed

        mins = time_left // 60  #to calculate minute
        secs = time_left % 60  #to calculate seconds

        print(f"{CLEAR_AND_RETURN}The alarm will go off on {mins:02d}:{secs:02d}")

    playsound("alarm.mp3")  #plays the sound

minutes = int(input("Enter the minute: "))  #takes user input
seconds = int(input("Enter the seconds: "))

total = minutes * 60 + seconds 

alarm_clock(total)