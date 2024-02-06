import requests
from bs4 import BeautifulSoup

def getFantasyName(sport):
    url = 'https://www.nbcsports.com/fantasy/' + sport
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    v = soup.find('h1', class_='Page-contextNav-title')
    return v.text.strip()

def getPlayerNews(sport):
    url = 'https://www.nbcsports.com/fantasy/' + sport + '/player-news'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    player_news_Dict = {}
    print(soup)
    for player_news in soup.find_all('li', class_='PlayerNewsModuleList-item'):
        playerFirstName = player_news.find('span', class_= 'PlayerNewsPost-firstName')
        playerLastName = player_news.find('span', class_= 'PlayerNewsPost-lastName')
        playerName = playerFirstName.text.strip() + ' ' + playerLastName.text.strip()
        playerAnalysis = player_news.find('div', class_= 'PlayerNewsPost-headline')
        player_news_Dict[playerName] = playerAnalysis
        
    return player_news_Dict

result = getPlayerNews('basketball')
print(result)