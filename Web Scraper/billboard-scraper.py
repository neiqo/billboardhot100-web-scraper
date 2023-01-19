from bs4 import BeautifulSoup
import requests, openpyxl, os

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Billboard Hot 100 2008'#change year to whatever year
sheet.append(['Rank', 'Title','Artist'])

try:
    source = requests.get('https://www.billboard.com/charts/year-end/2008/hot-100-songs/') #just change the link for each year
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    content = soup.find_all('div', class_='o-chart-results-list-row-container')


    for songs in content:
        songRank = songs.find('span').text.strip()
        songTitle = songs.find('h3').text.strip()
        songArtist = songs.find('h3').find_next('span').text.strip()

        sheet.append([songRank,songTitle,songArtist])


    if not os.path.exists(os.getcwd() + "/Excel Files/"):
        os.mkdir('Excel Files')
        os.chdir("Excel Files")
        excel.save('Billboard Hot 100 (2009).xlsx')
    else:
        os.chdir("Excel Files")
        excel.save('Billboard Hot 100 (2009).xlsx')


    print('Success!\nFiles have been extracted to', os.getcwd())
except Exception as e:
    print(e)
