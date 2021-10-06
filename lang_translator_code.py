import speech_recognition as spr
import googletrans
from googletrans import Translator
from gtts import gTTS
import os

#Dictionary of the Lanuages Available
Dict = googletrans.LANGUAGES
print("You can choose from the following Lanuages for you translation:\n")
print("  Code\t: Language")

for key in Dict:
    if len(key) < 5: print("*", key, " \t:", Dict[key].upper())
    else: print("*", key, ":", Dict[key].upper())

#User input for Language to translate from and to
from_lang = input("Enter the code for the langauge you want to Translate from: ")
to_lang = input("Enter the code for the langauge you want to Translate to: ")

#Create Recognizer() class objects called recog1 and recog2
recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

#Create microphone instance with device microphone chosen whose index value is 0
mc = spr.Microphone(device_index=0)

#Capture voice
with mc as source:
    print("\nSpeak 'Hello' to initiate the Translation!")
    print("----------------------------")
    audio = recog1.listen(source)

#Based on speech, tranlate the sentence into another language
if 'hello' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    translator = Translator()

    with mc as source:
        print('Speak a sentence...')
        audio = recog2.listen(source)
        # get_sentence = recog2.recognize_google(audio)
        
        try:
            get_sentence = recog2.recognize_google(audio)
            print('Phrase to be Tranlated: '+ get_sentence)
            text_to_translate = translator.translate(get_sentence, src = from_lang, dest = to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang = to_lang, slow = False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("We were unable to understand the input")
        except spr.RequestError as e:
            print("You were unable to provide required output".format(e))

else:
    print("You were unable to provide required output")

