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

def get_soup4(URL4): #PLANET
    page = requests.get(URL4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup4)
    return soup4
get_soup4("https://www.npr.org/templates/rss/podcast.php?id=510289")

def get_soup5(URL5): #COLLEGE
    page = requests.get(URL5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup5)
    return soup5
get_soup5("https://www.npr.org/rss/podcast.php?id=510345")

def get_soup6(URL6): #WHITE
    page = requests.get(URL6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup6)
    return soup6
get_soup6("https://www.npr.org/rss/podcast.php?id=510343")

def get_soup7(URL7): #ROUGH
    page = requests.get(URL7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup7)
    return soup7
get_soup3("https://www.npr.org/rss/podcast.php?id=510324")

def get_soup8(URL8): #ASK
    page = requests.get(URL8)
    soup8 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup8)
    return soup8
get_soup8("https://www.npr.org/rss/podcast.php?id=510299")

def get_soup9(URL9): #MORNING
    page = requests.get(URL9)
    soup9 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup9)
    return soup9
get_soup9("http://npr.pyther.net/podcast/morning-edition")

def get_soup3(URL10): #ALLTHINGS
    page = requests.get(URL10)
    soup10 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup10)
    return soup10
get_soup10("http://npr.pyther.net/podcast/all-things-considered")

def get_soup11(URL11): #WEEKENDSAT
    page = requests.get(URL11)
    soup11 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup11)
    return soup11
get_soup11("https://rss-npr-podcasts.herokuapp.com/rss/weekend-edition-saturday")

def get_soup12(URL12): #WEEKENDSUN
    page = requests.get(URL12)
    soup12 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup12)
    return soup12
get_soup12("https://rss-npr-podcasts.herokuapp.com/rss/weekend-edition-sunday")

def get_soup13(URL13): #HERENOW
    page = requests.get(URL13)
    soup13 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup13)
    return soup13
get_soup13("https://www.npr.org/rss/podcast.php?id=510051")

def get_soup14(URL14): #ONPOINT
    page = requests.get(URL14)
    soup14 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup14)
    return soup14
get_soup14("https://www.npr.org/rss/podcast.php?id=510053")


def get_soup15(URL15): #INDICATORPLANETMONEY
    page = requests.get(URL15)
    soup15 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup15)
    return soup15
get_soup15("https://www.npr.org/rss/podcast.php?id=510325")

def get_soup16(URL16): #FRESH
    page = requests.get(URL16)
    soup16 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup16)
    return soup16
get_soup16("https://www.npr.org/rss/podcast.php?id=381444908")

def get_soup17(URL17): #UPFIRST
    page = requests.get(URL17)
    soup17 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup17)
    return soup17
get_soup17("https://www.npr.org/rss/podcast.php?id=510318")

def get_soup18(URL18): #ONEA
    page = requests.get(URL3)
    soup18 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup18)
    return soup18
get_soup18("https://www.npr.org/rss/podcast.php?id=510316")

def get_soup19(URL19): #NPRNEWS
    page = requests.get(URL19)
    soup19 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup19)
    return soup19
get_soup3("https://www.npr.org/rss/podcast.php?id=500005")

def get_soup20(URL20): #BELIEVED
    page = requests.get(URL20)
    soup20 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup20)
    return soup20
get_soup20("https://www.npr.org/rss/podcast.php?id=510326")

def get_soup21(URL21): #CODESW
    page = requests.get(URL21)
    soup21 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup21)
    return soup21
get_soup21("https://www.npr.org/rss/podcast.php?id=510312")

def get_soup22(URL22): #EMBEDDED
    page = requests.get(URL22)
    soup22 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup22)
    return soup22
get_soup22("https://www.npr.org/rss/podcast.php?id=510311")

def get_soup23(URL23): #ITSBEEN
    page = requests.get(URL23)
    soup23 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup23)
    return soup23
get_soup23("https://www.npr.org/rss/podcast.php?id=510317")

def get_soup24(URL24): #LATINOUSA
    page = requests.get(URL24)
    soup24 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup24)
    return soup24
get_soup24("https://www.npr.org/rss/podcast.php?id=510016")

def get_soup25(URL25): #NPRpolitics
    page = requests.get(URL25)
    soup25 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup25)
    return soup25
get_soup25("https://www.npr.org/rss/podcast.php?id=510310")

def get_soup26(URL26): #THROUGH
    page = requests.get(URL26)
    soup26 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup26)
    return soup26
get_soup26("https://www.npr.org/rss/podcast.php?id=510333")

def get_soup27(URL27): #WHATSGOOD
    page = requests.get(URL27)
    soup27 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup27)
    return soup27
get_soup27("https://www.npr.org/rss/podcast.php?id=510323")

def get_soup28(URL28): #YRMEDIA
    page = requests.get(URL28)
    soup28 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup28)
    return soup28
get_soup28("https://www.npr.org/rss/podcast.php?id=4692815")

def get_soup29(URL29): #CAR
    page = requests.get(URL29)
    soup29 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup29)
    return soup29
get_soup29("https://www.npr.org/rss/podcast.php?id=510208")

def get_soup30(URL30): #BULLSEYE
    page = requests.get(URL30)
    soup30 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup30)
    return soup30
get_soup30("https://www.npr.org/rss/podcast.php?id=510309")

def get_soup31(URL31): #INVISIBLIA
    page = requests.get(URL31)
    soup31 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup31)
    return soup31
get_soup31("https://www.npr.org/templates/rss/podcast.php?id=510307")

def get_soup32(URL32): #ONLYAGAME
    page = requests.get(URL32)
    soup32 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup32)
    return soup32
get_soup32("https://www.npr.org/rss/podcast.php?id=510052")

def get_soup33(URL33): #WOW
    page = requests.get(URL33)
    soup33 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup33)
    return soup33
get_soup33("https://www.npr.org/rss/podcast.php?id=510321")

def get_soup34(URL34): #ALLSONGS
    page = requests.get(URL34)
    soup34 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup34)
    return soup34
get_soup34("https://www.npr.org/rss/podcast.php?id=510019&uid=n1qe4e85742c986fdb81d2d38ffa0d5d53")

def get_soup35(URL35): #TINY
    page = requests.get(URL35)
    soup35 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup35)
    return soup35
get_soup35("https://www.npr.org/templates/rss/podcast.php?id=510306")

def get_soup36(URL36): #ALTLATINO
    page = requests.get(URL36)
    soup36 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup36)
    return soup36
get_soup36("https://www.npr.org/templates/rss/podcast.php?id=510305")

def get_soup37(URL37): #MOUNTAIN
    page = requests.get(URL37)
    soup37 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup37)
    return soup37
get_soup37("https://feedpress.me/mountainstagepodcast")

def get_soup38(URL38): #FROM
    page = requests.get(URL38)
    soup38 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup38)
    return soup38
get_soup38("https://www.npr.org/rss/podcast.php?id=510026")

def get_soup39(URL39): #ALLSONGSLIVE
    page = requests.get(URL39)
    soup39 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup39)
    return soup39
get_soup39("https://www.npr.org/rss/podcast.php?id=510253")

def get_soup40(URL40): #BEAPOWERFUL
    page = requests.get(URL40)
    soup40 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup40)
    return soup40
get_soup40("https://www.npr.org/rss/podcast.php?id=510347")

def get_soup41(URL41): #PBSFRONTLINE
    page = requests.get(URL41)
    soup41 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup41)
    return soup41
get_soup41("http://feeds.feedburner.com/TheFrontlineDispatch")

def get_soup42(URL42): #INNOVATION
    page = requests.get(URL42)
    soup42 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup42)
    return soup42
get_soup42("https://feeds.wgbh.org/106/feed-rss.xml")

def get_soup43(URL43): #GROUNDTRUTHPROJ
    page = requests.get(URL43)
    soup43 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup43)
    return soup43
get_soup43("https://f.prxu.org/156/feed-rss.xml")


def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/wait.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
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
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/how.jpg"
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
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/hidden.jpg"
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
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/planet.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/college.png"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/white.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/rough.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast8(soup8):
    subjects = []
    for content in soup8.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/ask.png"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast8(playable_podcast8):
    items = []
    for podcast in playable_podcast8:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast9(soup9):
    subjects = []
    for content in soup9.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/morning.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast9(playable_podcast9):
    items = []
    for podcast in playable_podcast9:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast10(soup10):
    subjects = []
    for content in soup10.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/resources/media/things.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast10(playable_podcast10):
    items = []
    for podcast in playable_podcast10:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup11):
    subjects = []
    for content in soup11.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast11(playable_podcast11):
    items = []
    for podcast in playable_podcast11:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast12(soup12):
    subjects = []
    for content in soup12.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast12(playable_podcast12):
    items = []
    for podcast in playable_podcast12:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast13(soup13):
    subjects = []
    for content in soup13.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjectS
def compile_playable_podcast13(playable_podcast13):
    items = []
    for podcast in playable_podcast13:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast14(soup14):
    subjects = []
    for content in soup14.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast14(playable_podcast14):
    items = []
    for podcast in playable_podcast14:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_playable_podcast15(soup15):
    subjects = []
    for content in soup15.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast15(playable_podcast15):
    items = []
    for podcast in playable_podcast15:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast16(soup16):
    subjects = []
    for content in soup16.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast16(playable_podcast16):
    items = []
    for podcast in playable_podcast16:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast17(soup17):
    subjects = []
    for content in soup17.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast17(playable_podcast17):
    items = []
    for podcast in playable_podcast17:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast18(soup18):
    subjects = []
    for content in soup18.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast18(playable_podcast18):
    items = []
    for podcast in playable_podcast18:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast19(soup19):
    subjects = []
    for content in soup19.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast19(playable_podcast19):
    items = []
    for podcast in playable_podcast19:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
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
