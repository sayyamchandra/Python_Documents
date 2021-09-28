#importation
import gtts
from playsound import playsound



#taking the input from the user
print("Hi, Welcome to online GTTS")
print()
print()
address = input("Enter the file location or file name if the file is in same folder ad program!OK>>")


#handling the file
f  = open(address)
mytext = f.read()

#taking the file name from the user
filename = input("Enter the file name for output>>")



#conversion of text to speech statement
tts = gtts.gTTS(text = mytext,lang ='en', tld ='co.in' ,slow='False')

#save the file in the same folder
tts.save(filename + ".mp3")

#playing the sound
#playsound("myaudio.mp3")
f.close()
