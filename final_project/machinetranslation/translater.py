import json
import os
from deep_translator import MyMemoryTranslator

def englishtoFrench(word):
    frenchtext =  MyMemoryTranslator(source='en',target='fr').translate(word)
    print(frenchtext)
    return frenchtext


def frenchtoEnglish(word):
    englishtext =  MyMemoryTranslator(source='fr',target='en').translate(word)
    print(englishtext)
    return englishtext
frenchtoEnglish("Bonjour")