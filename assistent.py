import os
#text to speech library
import pyttsx3 as tt


tt.speak("Welcome Trupti")
tt.speak("Hey buddy !!! Tell me your requirement :")

while True:
	x=input("Enter your choice :")
	if (("google" in x) or ("chrome" in x)):
			tt.speak("OK here"+ x+ "fore you")
			os.system("start chrome")
	elif (('media' in x) or ("player" in x) or ("music" in x)):
			tt.speak("OK here"+ x+ "fore you")
			os.system("start wmplayer")
	elif (('notepad' in x) or ("editor" in x)):
			tt.speak("ok here"+x + "fore you")
			os.system("notepad")
	elif ('paint' in x):
			tt.speak("ok here"+x+"fore you")
			os.system("start mspaint")
	elif ('excel' in x):  
			tt.speak("OK here"+x+" fore you")
			os.system("start EXCEL")
	elif ('ppt' in x):
			tt.speak("OK here"+x+" fore you")
			os.system("start POWERPNT")
	elif ('date' in x):
			tt.speak("OK here" + x + "fore you")
			os.system("start date")
	elif ('word' in x):
			tt.speak("OK here" + x + "fore you")
			os.system("start WINWORD")
	elif (('cal' in x) or ("calculator" in x)):
			tt.speak("OK here"+ x +" fore you")
			os.system("calc")
	elif (('command' in x) or ("prompt" in x)or ("cmd" in x)):
			tt.speak("OK here"+ x + "fore you")
			os.system("start cmd")
	elif (('control' in x) or ("panel" in x)):
			tt.speak("OK here"+ x + "fore you")
			os.system("control")
	elif ('settings' in x):
			tt.speak("OK here"+ x + "fore you")
			os.system("start ms-settings")
	elif (('SQL' in x) or ("sql server" in x)):
			tt.speak("OK here" + x +"fore you")
			os.system("SQLServerManager12")
	elif (('notes' in x) or ("sticky" in x)):
			tt.speak("OK here" + x + "fore you")
			os.system("StikyNot")
	elif (('stop' in x) or ("exit" in x)):
			tt.speak(" good by ..see you soon")
			break
		
	else:
			tt.speak("Please Enter Correct Choice!!!!")
	
	
	
	
		
	
	
	
