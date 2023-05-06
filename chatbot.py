import speech_recognition as sr
from gtts import gTTS
import os

class ChatBot():
	text=''
	def __init__(self,name):
		self.name=name
		print('...Hi, I am',self.name,'...')
	
	def speech_to_text(self):
		recogniser=sr.Recognizer()
		with sr.Microphone(device_index=0) as mic:
			print('...Listening...')
			audio=recogniser.listen(mic)
			try:
				self.text=recogniser.recognize_google(audio)
				print('Me -->',self.text)
			except:
				print('AI --> error')
	
	def wake_up(self):
		return True if self.name.lower() in self.text.lower() else False
	
	@staticmethod
	def text_to_speech(text):
		print('AI -->',text)
		audio=gTTS(text=text,lang='en',slow=False)
		audio.save('audio.mp3')
		os.system('start audio.mp3')
		os.remove('audio.mp3')


if __name__=='__main__':
	ai=ChatBot("Jarvis")
	while True:
		ai.speech_to_text()
		if ai.wake_up():
			res="Hello I am Jarvis, What can I do for you?"
		else:
			continue
		ai.text_to_speech(res)
		break