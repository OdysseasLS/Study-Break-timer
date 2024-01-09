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

func main() {
	var study_time, break_time int = get_input()
	study_time = study_time * 60
	break_time = break_time * 60

	beeep.Notify("Study Timer Deployed!", "I've been deployed at "+time.Now().Format("15:04:05")+" I will notify you when it is time to take a break.", "assets/img/letsgo.jpeg")
	fmt.Println("Started successfully! Happy studying!")
	fmt.Println(time.Now().Format("15:04:05"))
	for run := true; run; {
		//wait study_time
		time.Sleep(time.Duration(study_time) * time.Second)
		//send notif
		beeep.Notify("Time for a break!", "You've been studying for "+string(study_time/60)+"minutes. Take a "+string(break_time/60)+" minute break!", "assets/img/brk_icon.jpeg")
		//wait break_time
		time.Sleep(time.Duration(break_time) * time.Second)
		//send notif
		beeep.Notify("Back to work!", "Your break is over. Get THE FUCK back to work!", "assets/img/btw_icon.jpg")
	}
}
