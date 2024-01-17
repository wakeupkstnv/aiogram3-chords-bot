from libary import *

def chords_text(name: str):
    url_amdm =  "https://amdm.ru/search/?q="
    user_url = name.split()

    for _ in user_url:
        url_amdm += _ + '+'

    try:
        page = requests.get(url = url_amdm[:-1])
        soup = BeautifulSoup(page.text, "html.parser")
        razborBlock = []
        poisk = soup.select('.artist')[1]

        urlRazbor = poisk.get('href')
        pageRazbor = requests.get(urlRazbor)
        sope = BeautifulSoup(pageRazbor.text, "html.parser")
        razborBlock = sope.findAll('pre', class_="field__podbor_new podbor__text")
        for chords in razborBlock:
            if chords.find('div', class_="podbor__chord") is not None:
                return chords.text
    except IndexError:
        return 'Такой песни увы не сущесвует :('

def song_list(name: str):
    url_amdm =  "https://amdm.ru/search/?q="
    user_url = name.split()

    for _ in user_url:
        url_amdm += _ + '+'

    try:
        page = requests.get(url=url_amdm[:-1])
        soup = BeautifulSoup(page.text, "html.parser")
        razborBlock = []
        all_list = ''
        for i in range(0, 20, 2):
            artist_tag = soup.select('.artist')[i]
            song_tag = soup.select('.artist')[i + 1]
            artist_name = artist_tag.text.strip()  # Use .strip() to remove leading/trailing whitespaces
            song_name = song_tag.text.strip()
            all_list += f'{artist_name} - {song_name}\n'

        return all_list
    except IndexError:
        return 'Такой песни увы не сущесвует :('