"""
Daily news Reader Using google-news, pyttsx and Speech-Recongnition Module

"""

import speech_recognition
from GoogleNews import GoogleNews
import pyttsx3

googlenews = GoogleNews()
googlenews.get_news('Tesla')
result = googlenews.results()
a="title"
result_title = result[0][a]
print(result_title)