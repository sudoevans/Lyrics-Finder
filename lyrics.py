#lyrics Search
import colorama
from colorama import Fore
colorama.init(autoreset=True)


import requests
song_name=input("Enter the name of the song: ")
artist=input("Enter artist Name: ")

try:
	api=("https://api.lyrics.ovh/v1/{}/{}")
	# print (api)
	print(Fore.YELLOW+"Searching Song Lyrics...")
	

	song=requests.get(api.format(artist,song_name)).json()
	for key   in song:
		if key=='error':
			print(song['error']+" Try using specific Keywords")
		else:
			print(song['lyrics'])
except requests.ConnectionError as e:
	print(Fore.RED+"NO INTERNET!")
except requests.Timeout as e:
    print("OOPS!! Request Timeout")
    pass
except requests.RequestException as e:
    print("OOPS!! General Error")
    pass
except KeyboardInterrupt:
    print("Program Cancelled by User")















