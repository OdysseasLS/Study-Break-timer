from notifypy import Notify
import time
import tkinter as tk


def main():
    study_time, break_time = get_input()
    study_time *= 60
    break_time *= 60
    starting, take_break, back_to_work = make_notifs(study_time, break_time)
    run = True
    print("Started successfully! Happy studying :D!")
    starting.send(block=False)
    print(f"{time.ctime()}")
    while run:
        time.sleep(study_time)
        take_break.send(block=False)
        print(f"break msg sent at {time.ctime()}")
        time.sleep(break_time)
        back_to_work.send(block=False)
        print(f"work msg sent at {time.ctime()}")


def make_notifs(study_time, break_time):

    # Notification when the program starts
    starting = Notify()
    starting.title = "Study Timer Deployed!"
    starting.message = f"I've been deployed at {time.ctime()}. I'll notify you when it's time to take a break."
    starting.icon = "letsgo.jpeg"
    starting.audio = "sound.wav"

    # Notification to take a break
    take_break = Notify()
    take_break.title = "Time for a break!"
    take_break.message = f"You've been studying for {int(study_time//60)} minutes. Take a {int(break_time//60)} break!"
    take_break.icon = "brk_icon.jpeg"
    take_break.audio = "sound.wav"

    # Notification to get back to work
    back_to_work = Notify()
    back_to_work.title = "Back to work!"
    back_to_work.message = f"Your break is over. Get THE FUCK back to work!"
    back_to_work.icon = "btw_icon.jpg"
    back_to_work.audio = "sound.wav"

    return starting, take_break, back_to_work


def get_input():
    study_time = float(input("How long do you want to study for? (in minutes) "))
    break_time = float(input("How long do you want to break for? (in minutes) "))
    return study_time, break_time


if __name__ == '__main__':
    main()
