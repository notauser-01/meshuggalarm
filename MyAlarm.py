import datetime
import os
import time

now = str(datetime.datetime.now())[11:16] 
alarm_time = input("When do you want to wake up (HH:MM)? ")

while len(alarm_time) <= 4:
	alarm_time = input("Do it right! (HH:MM) ")

alarm_nums = alarm_time[0:2] + alarm_time[3:]
colon = alarm_time[2]
runclock = False
 
while runclock == False:
	if alarm_nums.isdigit() == True and colon == ":":
			if 0 <= int(alarm_nums[0:2]) <= 23 and 0 <= int(alarm_nums[3:]) <=59:
				runclock = True
	else:
		alarm_time = input("Do it right! (HH:MM) ")
			while len(alarm_time) <= 4:
				alarm_time = input("Do it right! (HH:MM) ")
		alarm_nums = alarm_time[0:2] + alarm_time[3:]
		colon = alarm_time[2]

while now != alarm_time:
	print(f"It is currently {now}, so you can sleep for longer.")
	time.sleep(45)
	now = str(datetime.datetime.now())[11:16]

file = "03 Bleed.flac"
os.startfile(file)