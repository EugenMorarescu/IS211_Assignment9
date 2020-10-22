from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(),features='lxml')

#print(soup.prettify())

table = soup.find("div", id='TableBase')
players = table.findChildren('tr',class_="TableBase-bodyTr")

for unwanted in soup.find_all('span',class_='CellPlayerName--short'):
    unwanted.extract()

playerList = []

for td in players:
    stats = td.text.strip().split('\n')
    stats = ' '.join(stats).split()
       
    playerList.append(stats)

for i in range(0,len(playerList)):
    if playerList[i][0] == 'Robert':
        playerList[i][1 : 3] = [' '.join(playerList[i][1 : 3])]
        
df = pd.DataFrame(playerList)
df[0] = df[0]+' '+df[1]
df = df[[0,2,3,11]]
df.columns = ['Name','Position','Team','Touchdowns']
df.set_index('Name',inplace=True)
df["Touchdowns"] = pd.to_numeric(df["Touchdowns"])
df.sort_values('Touchdowns',inplace=True,ascending=False)
print(df.head(20))
