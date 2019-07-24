import requests
import re
from bs4 import BeautifulSoup

def get_soup1(URL1): #WAIT
    page = requests.get(URL1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup1)
    return soup1
get_soup1("https://www.npr.org/rss/podcast.php?id=344098539")

def get_soup2(URL2): #HOW
    page = requests.get(URL2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup2)
    return soup2
get_soup2("https://www.npr.org/rss/podcast.php?id=510313")

def get_soup3(URL3): #HIDDEN
    page = requests.get(URL3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup3)
    return soup3
get_soup3("https://www.npr.org/rss/podcast.php?id=510308")


def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('description')
#            desc = desc.get_text()

#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f.png?s=1400"
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()

        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hibt_podcasttile_sq-98320b282169a8cea04a406530e6e7b957665b3f-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items


def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects


def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items
