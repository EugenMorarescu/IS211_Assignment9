from bs4 import BeautifulSoup
import urllib.request


url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(),features='lxml')

#print(soup.prettify())
games = []
table = soup.find("table",{'cols': '4'})
rows = table.findChildren(['tr'])
for td in rows:
    games.append(td.text.strip().split('\n'))
    
teamList = [
    
    'Philadelphia','NY Giants',
    'Cleveland','Cincinnati',
    'Dallas','Washington',
    'Atlanta','Detroit',
    'New Orleans','Carolina',
    'Buffalo','NY Jets',
    'Green Bay','Houston',
    'Seattle','Arizona',
    'New England','San Francisco',
    'Kansas City','Denver',
    'Tampa Bay','Las Vegas',
    'Tennessee','Pittsburgh',
    'LA Chargers','Jacksonville']

for i in teamList:
    print(i)
inp = input("Enter Team: ")
inp = inp.lower()


for i in games:
    if inp in i[3].lower() or inp in i[1].lower():
        print('Favorite: {} | Underdog: {} | Spread: {}'.format(i[1],i[3],i[2]))