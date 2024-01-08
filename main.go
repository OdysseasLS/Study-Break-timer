package main

import (
	"fmt"
	"time"
)

func get_input() int {
	var study_time, break_time int
	fmt.Println("How long do you want to study for? (in minutes) ")
	fmt.Scanln(&study_time)
	fmt.Println("How long do you want to break for? (in minutes) ")
	fmt.Scanln(&break_time)
	return study_time, break_time
}

func send_notif(study_time, break_time int) {
	//make the notifications
}

func main() {
	var study_time, break_time int = get_input()
	study_time = study_time * 60
	break_time = break_time	* 60
	fmt.Println("Started successfully! Happy studying!")
	// print time
	for var run bool = true; run; {
		//wait study_time
		//send notif
		//wait break_time
		//send notif
	}
}