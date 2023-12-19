from notifypy import Notify
import time


def main():
    study_time, break_time = get_input()
    study_time *= 60
    break_time *= 60
    take_break, back_to_work = make_notifs(study_time, break_time)
    run = True
    while run:
        time.sleep(study_time)
        take_break.send()
        time.sleep(break_time)
        back_to_work.send()


def make_notifs(study_time, break_time):
    # Notification to take a break
    take_break = Notify()
    take_break.title = "Time for a break!"
    take_break.message = f"You've been studying for {study_time/60} minutes. Take a {break_time/60} break!"
    # make icon

    # Notification to get back to work
    back_to_work = Notify()
    back_to_work.title = "Back to work!"
    back_to_work.message = f"Your break is over. Get THE FUCK back to work!"

    return take_break, back_to_work


def get_input():
    study_time = input("How long do you want to study for? (in minutes) ")
    break_time = input("How long do you want to break for? (in minutes) ")
    return int(study_time), int(break_time)


if __name__ == '__main__':
    main()
