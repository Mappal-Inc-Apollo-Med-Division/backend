import nltk
import sr
import gtts
import sys

uid = sys.argv[1]
r = sr.Recognizer()


while True:
	mic = sr.microphone()
	with mic as source:
		rec = sr.record(source)
	line = r.recognize_google(rec)
	lineref = nltk.tokenize(line)
	linetag = nltk.pos_tags(lineref)
	for i in linetag:
		if i.values()=='NN':
			if nltk.lemmatize(i.values()) in nltk.similar('diagnose'):
				subprocess.call(['python diagnose.py',uid])




