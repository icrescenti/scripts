# Just a dummy code to transcribe audio to text
# Its design for personal use in my specific case

import speech_recognition as sr

r = sr.Recognizer()
pause = False

f = open(input("tag: ") + ".log", "w", encoding="utf-8")

def transcribe():
	global f
	global pause
	text = ""

	with sr.Microphone() as source:
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio, language="ca-ES")
			if (pause == False):
				print(text)
				f.write(text + "\n")
			
			if (len(text) > 18 and text[-19:] == "pausar transcripció"):
				print("[Transcripció pausada]")
				f.write("[Transcripció pausada]" + "\n")
				pause = True
			elif (len(text) > 20 and text[-21:] == "reanudar transcripció"):
				print("[Transcripció reanudada]")
				f.write("[Transcripció reanudada]" + "\n")
				pause = False
		except:
			pass

	if (len(text) < 23 or text[-23:] != "finalitzar transcripció" or text[-23:] != "finalitza transcripció"):
		transcribe()

transcribe()
f.close()