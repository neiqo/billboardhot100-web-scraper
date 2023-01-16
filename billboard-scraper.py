from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Billboard Hot 100 2022'
sheet.append(['Rank', 'Title','Artist'])

try:
    source = requests.get('https://www.billboard.com/charts/year-end/2022/hot-100-songs/') #just change the link for each year
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    content = soup.find_all('div', class_='o-chart-results-list-row-container')


    for songs in content:
        songRank = songs.find('span').text.strip()
        songTitle = songs.find('h3').text.strip()
        songArtist = songs.find('h3').find_next('span').text.strip()

        sheet.append([songRank,songTitle,songArtist])

except Exception as e:
    print(e)

print('Success')

excel.save('Billboard Hot 100 (2022).xlsx')