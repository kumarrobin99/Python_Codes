import os
print("Heyy.. Welcome\nI am your personal assistant for opening applications on your computer\n")
while True:
	print("Enter the name of application you want to open:", end = '')
	a = input()
	
	if (("open" in a) or ("run" in a) or ("execute" in a)) and (("media player" in a) or ("windows media player" in a)):
		os.system("wmplayer")
		
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("chrome" in a) or ("google chrome" in a)):
		os.system("chrome")
		
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("notepad" in a) or ("editor" in a)):
		os.system("notepad")
		
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("vlc" in a)):
		os.system("vlc")
		
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("calculator" in a) or ("calc" in a)):
		os.system("calc")
		
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("ms word" in a) or ("word" in a) or ("word editor" in a)):
		os.system("winword")
	
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("ms powerpoint" in a) or ("powerpoint" in a) or ("presentation" in a)):
		os.system("powerpnt")
		
	elif (("open" in a) or ("run" in a) or ("execute" in a)) and (("ms excel" in a) or ("excel" in a) or ("spreadsheet" in a)):
		os.system("excel")
		
	elif ("exit" in a) or ("quit" in a) or ("close" in a):
		break
	
	else:
		print("Sorry.. Command not supported !!!")