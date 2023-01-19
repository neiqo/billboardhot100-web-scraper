from bs4 import BeautifulSoup
import requests, openpyxl, os

originalcwd = os.getcwd()
if not os.path.exists(originalcwd + "/Excel Files/"):
    os.mkdir("Excel Files")
    os.chdir("Excel Files")
    print('Folder Made')
else:
    os.chdir("Excel Files")
    print('Folder already created\n'
          '---------------------------------------------------------')

try:
    year = 2006

    for x in range(20):

        url = 'https://www.billboard.com/charts/year-end/'+str(year)+'/hot-100-songs/'
        source = requests.get(url)

        if year == 2023:
            print('Program Finished')
            break
        else:
            soup = BeautifulSoup(source.text, 'html.parser')
            content = soup.find_all('div', class_='o-chart-results-list-row-container')

            excel = openpyxl.Workbook()
            sheet = excel.active
            sheet.title = 'Billboard Hot 100'+str(year)  # change year to whatever year
            sheet.append(['Rank', 'Title', 'Artist'])

            for songs in content:
                songRank = songs.find('span').text.strip()
                songTitle = songs.find('h3').text.strip()
                songArtist = songs.find('h3').find_next('span').text.strip()

                sheet.append([songRank, songTitle, songArtist])

            excel_file = 'Billboard Hot 100 ('+str(year)+').xlsx'
            excel.save(excel_file)
            print('Excel File with data from year '+str(year)+' made\n'
                  'File is in '+os.getcwd()+'\n'
                  '---------------------------------------------------------')

            year += 1
except Exception as e:
    print(e)
