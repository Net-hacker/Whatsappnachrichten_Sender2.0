#Import
import pywhatkit
import keyboard
import time
import os
import sys
import pyttsx3
import speech_recognition as sr

#Variabeln

zuhörer = sr.Recognizer()
redstimme = pyttsx3.init()
tastatur = keyboard

def zuhören():
    try:
        with sr.Microphone() as source:
            print('Ich höre...')
            stimme = zuhörer.listen(source)
            info = zuhörer.recognize_google(stimme, language='de-DE')
            print(info)
            return info.lower()
            if 'Stopp' in info:
                stop()
    except:
        pass

def rede(text):
    redstimme.say(text)
    redstimme.runAndWait()

def stop():
    sys.exit(0)

kontaktliste = {
    #Kontakte
}

stundenanzahl = {
    '0' : 0, 
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    '11' : 11,
    '12' : 12,
    '13' : 13,
    '14' : 14,
    '15' : 15,
    '16' : 16,
    '17' : 17,
    '18' : 18,
    '19' : 19,
    '20' : 10,
    '21' : 21,
    '22' : 22,
    '23' : 23,
    '24' : 24    
}

minutenanzahl = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    '11' : 11,
    '12' : 12,
    '13' : 13,
    '14' : 14,
    '15' : 15,
    '16' : 16,
    '17' : 17,
    '18' : 18,
    '19' : 19,
    '20' : 20,
    '21' : 21,
    '22' : 22,
    '23' : 23,
    '24' : 24,
    '25' : 25,
    '26' : 26,
    '27' : 27,
    '28' : 28,
    '29' : 29,
    '30' : 30,
    '31' : 31,
    '32' : 32,
    '33' : 33,
    '34' : 34,
    '35' : 35,
    '36' : 36,
    '37' : 37,
    '38' : 38,
    '39' : 39,
    '40' : 40,
    '41' : 41,
    '42' : 42,
    '43' : 43,
    '44' : 44,
    '45' : 45,
    '46' : 46,
    '47' : 47,
    '48' : 48,
    '49' : 49,
    '50' : 50,
    '51' : 51,
    '52' : 52,
    '53' : 53,
    '54' : 54,
    '55' : 55,
    '56' : 56,
    '57' : 57,
    '58' : 58,
    '59' : 59,
    '60' : 0,
}

def nachricht_sender():
    #Das die .txt File gelöscht wird
    if os.path.exists("/pywhatkit_dbs.txt"):
        os.remove("/pywhatkit_dbs.txt")
    print('Hi, hast du Whatsapp schon mit Whatsapp Web verbunden, wenn nicht sag bei der nächsten Frage: Stopp')
    rede('Hi, hast du Whatsapp schon mit Whatsapp Web verbunden, wenn nicht sag bei der nächsten Frage: Stopp')
    time.sleep(1)
    print('An wen soll die Nachricht gehen?')
    rede('An wen soll die Nachricht gehen?')
    name = zuhören()
    namenssuche = kontaktliste[name]
    print(namenssuche)
    print('Was ist deine Nachricht?')
    rede('Was ist deine Nachricht?')
    nachricht = zuhören()
    print('Zu welcher Stunde soll die Nachricht ankommen?')
    rede('Zu welcher Stunde soll die Nachricht ankommen?')
    stunde = zuhören()
    stundensuche = stundenanzahl[stunde]
    print('Zu welcher Minute soll die Nachricht ankommen?')
    rede('Zu welcher Minute soll die Nachricht ankommen?')
    minute = zuhören()
    minutensuche = minutenanzahl[minute]
    print('Ok Nachricht wird vorberreitet und versendet')
    rede('Ok Nachricht wird vorberreitet und versendet')
    pywhatkit.sendwhatmsg('+49 ' + namenssuche, nachricht, stundensuche, minutensuche)
    tastatur.press_and_release('esc')
    time.sleep(1)
    tastatur.press_and_release('enter')
    time.sleep(3)
    tastatur.press_and_release('alt + f4')
    time.sleep(1)
    print('Fertig!')
    time.sleep(1)
    #Das die .txt File gelöscht wird
    if os.path.exists("/pywhatkit_dbs.txt"):
        os.remove("/pywhatkit_dbs.txt")
    sys.exit(0)

nachricht_sender()
