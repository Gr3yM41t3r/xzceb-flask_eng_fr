"""
This module uses the MyMemoryTranslator from the deep_translator package
to define two functions: english_to_french and french_to_english.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Function to translate English text to French using MyMemoryTranslator
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Function to translate French text to English using MyMemoryTranslator
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
