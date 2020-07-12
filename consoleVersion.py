import requests
import lxml
from bs4 import BeautifulSoup
inputWord = input('Please input the word: ')
headers1 = {'user-agent': 'your-own-user-agent/0.0.1'}
url = requests.get('https://www.collinsdictionary.com/dictionary/english/' + inputWord, headers = headers1)
soup = BeautifulSoup(url.text, 'lxml')
#partOfSpeech
try:
    posSoup = soup.find('span', class_ = 'pos') # pos = partOfSpeech
    posTxt  = posSoup.get_text()
except:
    posTxt = 'Unknown'
#definition number one
try:
    def1Soup = soup.find('div', class_ = 'def')
    def1Txt = def1Soup.get_text()
    def1Txt = def1Txt.replace("\n","")
except:
    def1Txt = 'Unknown'
#examples
try:
    exSoup = soup.find('span', class_ = 'quote')
    exTxt = exSoup.get_text()
    #exTxt = exTxt.replace("\n","")
    exTxt = exTxt.replace("  ", " ")
except:
    exTxt = ' Unknown'
#Video
try:
    videoSoup = soup.find('div', class_ = 'youtube-video')
    videoId = videoSoup['data-embed']
    videoLink = '''https://www.youtube.com/watch?v=''' + videoId
except:
    videoLink = 'Video with pronunciation is not found'
result_txt = 'Part of speech: ' + posTxt  + '\n' + 'Definition: ' + def1Txt  + '\n' + 'Example:'+ exTxt + '\n' + 'Video: ' + videoLink
print(result_txt)
