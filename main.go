package main

import (
	"fmt"
	"time"

	"github.com/gen2brain/beeep"
)

func get_input() (int, int) {
	var study_time, break_time int
	fmt.Println("How long do you want to study for? (in minutes) ")
	fmt.Scanln(&study_time)
	fmt.Println("How long do you want to break for? (in minutes) ")
	fmt.Scanln(&break_time)
	return study_time, break_time
}

func send_notif(study_time, break_time int) {
	//make the notifications
	starting := beeep.Notify("Study Timer Deployed!", "I've been deployed at" + time.Now().Format("15:04:05") + " I will notify you when it is time to take a break.", "assets/img/letsgo.jpeg")
	take_break := beep.

	return starting, take_break, back_to_work
}

func main() {
	var study_time, break_time int = get_input()
	study_time = study_time * 60
	break_time = break_time * 60
	fmt.Println("Started successfully! Happy studying!")
	// print time
	for run := true; run; {
		//wait study_time
		time.Sleep(time.Duration(study_time) * time.Second)
		//send notif
		starting
		//wait break_time
		time.Sleep(time.Duration(break_time) * time.Second)
		//send notif
	}
}
