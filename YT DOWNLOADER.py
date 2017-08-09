from __future__ import unicode_literals
import youtube_dl
import time
import pafy
import sys, os
from sys import stdout

menu_actions = {}

def GetUrl():
	os.system('cls')
	print('\n Copy the URL from your browser')
	GetUrl.url = input('\n Paste it here:  ')
	if GetUrl.url != "":
		try:
			video = pafy.new(GetUrl.url)
			videoInfo = [video.title, video.author, video.duration]
			GetUrl.title = videoInfo[0]
			GetUrl.author = videoInfo[1]
			GetUrl.length = videoInfo[2]
			print('\n Title: ' + videoInfo[0] + ', '+ 'Author: ' + videoInfo[1] + ', ' + 'Lenght: ' + videoInfo[2])
			okno = input('\n Is this info OK? Y/N   ')
			if okno == 'Y' or okno == 'y':
				Main_menu()
			else:
				GetUrl()
		except:
			print(" \n Error to establish connection with video")
			time.sleep(1)
			GetUrl()
	else:
		print("\n Please insert a valid adress")
		time.sleep(1)
		GetUrl()
	
	return
	
def Main_menu():
	os.system('cls')
	title1 = GetUrl.title
	author1 = GetUrl.author
	length1 = GetUrl.length
	print(" Dev: Isaac Rivas")
	print("\n")
	print(' Title: ' + title1 + ', '+ 'Author: ' + author1 + ', ' + 'Lenght: ' + str(length1 + '\n'))
	print(" **** Menu ****")
	print(" [1] Download to mp4 - Full Resolution Supported")	
	print(" [2] Download to mp3 - High Quality Audio Supported")
	print(" [3] See other audio extensions available")
	print(" [4] See other video extensions available")
	print(" [9] Exit")
	print("\n")
	choice = input(" >>> ")
	ExecutedOption(choice)
	
	return
	
def ExecutedOption(choice):
	os.system('cls')
	ch = choice.lower()
	if ch == '':
		menu_actions['main_menu']()
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print ("Invalid selection, please try again.\n")
			menu_actions['main_menu']()

	return

def Option1():
	print("\n MP4 Download")
	time.sleep(2)
	print("")
	print(" [*]Awaiting connection[*] ")
	time.sleep(3)
	print(" [*]Connection established[*] ")
	time.sleep(3)
	print(" [*]Starting Download[*] \n")
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([GetUrl.url])
	print(" Video succesfully downloaded")
	time.sleep(2)
	print(" \n Moving to Main Menu in...")
	for i in range(1,6,1):
		stdout.write("\r%d" % i)
		stdout.flush()
		time.sleep(1)
	stdout.write("\n")
	Main_menu()
	
	return

def Option2():
	print("\n MP3 Download")
	time.sleep(2)
	print("")
	print(" [*]Awaiting connection[*] ")
	time.sleep(3)
	print(" [*]Connection established[*] ")
	time.sleep(3)
	print(" [*]Starting Download[*] \n")
	ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '320',
		}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([GetUrl.url])
	print(" Audio succesfully downloaded")
	time.sleep(2)
	print(" \n Moving to Main Menu in...")
	for i in range(1,6,1):
		stdout.write("\r%d" % i)
		stdout.flush()
		time.sleep(1)
	stdout.write("\n")
	Main_menu()
	
	return

def Option3():
	print("\n Proximanente...")

def Option4():
	print("\n Proximanente...")

def Exit():
	exit()
	return

menu_actions = {
'main_menu': Main_menu,
'1': Option1,
'2': Option2,
'3': Option3,
'4': Option4,
'9': Exit
}

if __name__ == '__main__':
	GetUrl()
