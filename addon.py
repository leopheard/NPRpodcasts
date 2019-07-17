from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

#Featured
URL-HIDDEN = "https://www.npr.org/rss/podcast.php?id=510308" #Hiddenbrain
URL-BUILT = "https://www.npr.org/rss/podcast.php?id=510313" #HowIbuilt
URL-WAIT = "https://www.npr.org/templates/rss/podcast.php?id=344098539" #WaitwaitDont
URL-PLANET = "https://www.npr.org/templates/rss/podcast.php?id=510289" #PlanetMoney
URL-COLLEGE = "https://www.npr.org/rss/podcast.php?id=510345" #Howtopayforcollege
URL-WHITE = "https://www.npr.org/rss/podcast.php?id=510343" #Whitelies
URL-ROUGH = "https://www.npr.org/rss/podcast.php?id=510324" #Roughtrans
URL-ASK = "https://www.npr.org/rss/podcast.php?id=510299" #Askmeanother

#Daily
#Weekend Edition Sat
#Weekend Edition Sun
URL-MORNING = "http://npr.pyther.net/podcast/morning-edition"#Morning Edition
URL-THINGS = "http://npr.pyther.net/podcast/all-things-considered"#AllThingsConsidered
URL-HERE = "https://www.npr.org/rss/podcast.php?id=510051" #HereNow
URL-ONPOINT = "https://www.npr.org/rss/podcast.php?id=510053" #OnpointWBUR
URL-INDICATOR = "https://www.npr.org/rss/podcast.php?id=510325" #indictatorplanetmoney
URL-FRESH = "https://www.npr.org/rss/podcast.php?id=381444908" #freshair
URL-UP = "https://www.npr.org/rss/podcast.php?id=510318" #upfirst
URL-1A = "https://www.npr.org/rss/podcast.php?id=510316" #1A

#NewsConversations
URL-NOW = "https://www.npr.org/rss/podcast.php?id=500005" #NPRNewsNow
URL-HERE = "https://www.npr.org/rss/podcast.php?id=510051" #HereNow
URL-ONPOINT = "https://www.npr.org/rss/podcast.php?id=510053" #OnpointWBUR
URL-INDICATOR = "https://www.npr.org/rss/podcast.php?id=510325" #indictatorplanetmoney
URL-FRESH = "https://www.npr.org/rss/podcast.php?id=381444908" #freshair
URL-UP = "https://www.npr.org/rss/podcast.php?id=510318" #upfirst
URL-1A = "https://www.npr.org/rss/podcast.php?id=510316" #1A
URL-BELIEVED = "https://www.npr.org/rss/podcast.php?id=510326" #Believed
URL-CODE = "https://www.npr.org/rss/podcast.php?id=510312" #Codesw
URL-EMBEDDED = "https://www.npr.org/rss/podcast.php?id=510311" #Embedded
URL-ITBEEN = "https://www.npr.org/rss/podcast.php?id=510317" #Itbeenaminute
URL-LATINO = "https://www.npr.org/rss/podcast.php?id=510016" #latinoUSA
URL-POLITICS = "https://www.npr.org/rss/podcast.php?id=510310" #NPRpolitics
URL-THROUGH = "https://www.npr.org/rss/podcast.php?id=510333" #thoughline
URL-WHATS = "https://www.npr.org/rss/podcast.php?id=510323" #whatsgoodwith
URL-YR = "https://www.npr.org/rss/podcast.php?id=4692815" #YRmedia

#StorytellingHumor
URL-ASK = "https://www.npr.org/rss/podcast.php?id=510299" #Askmeanother
URL-CAR = "https://www.npr.org/rss/podcast.php?id=510208" #bestofcartalk
URL-BULLSEYE = "https://www.npr.org/rss/podcast.php?id=510309" #bullseye
URL-HIDDEN = "https://www.npr.org/rss/podcast.php?id=510308" #hiddenbrain
URL-BUILT = "https://www.npr.org/rss/podcast.php?id=510313" #HowIbuilt
URL-INVISIBILIA = "https://www.npr.org/templates/rss/podcast.php?id=510307" #invisibila
URL-ONLY = "https://www.npr.org/rss/podcast.php?id=510052" #onlyagame
URL-PLANET = "https://www.npr.org/templates/rss/podcast.php?id=510289" #PlanetMoney
URL-WAIT = "https://www.npr.org/templates/rss/podcast.php?id=344098539" #WaitwaitDont
URL-WOW = "https://www.npr.org/rss/podcast.php?id=510321" #wowintheworld

#Music
URL-SONGS = "https://www.npr.org/rss/podcast.php?id=510019&uid=n1qe4e85742c986fdb81d2d38ffa0d5d53" #Allsongconsidered
URL-TINY = "https://www.npr.org/templates/rss/podcast.php?id=510306"#TinyDesk
URL-LATINO = "https://www.npr.org/templates/rss/podcast.php?id=510305"#Altlatino
URL-MOUNTAIN = "https://feedpress.me/mountainstagepodcast"#NPRMountainStage
URL-FTT = "https://www.npr.org/rss/podcast.php?id=510026" #Fromthetop
URL-LIVE = "https://www.npr.org/rss/podcast.php?id=510253" #LiveInConcertAllSongsCons


@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30105),#MUSIC
            'path': plugin.url_for('all_music'),
            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f-s400-c85.png"},
        {
            'label': plugin.get_string(30001),#WAIT
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f-s400-c85.png"},
        {
            'label': plugin.get_string(30002),#HOW
            'path': plugin.url_for('all_episodes2'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hibt_podcasttile_sq-98320b282169a8cea04a406530e6e7b957665b3f-s300-c85.jpg"},
        {
            'label': plugin.get_string(30003),#HIDDEN
            'path': plugin.url_for('all_episodes3'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s300-c85.jpg"},
        {
            'label': plugin.get_string(30004),#PLANET
            'path': plugin.url_for('all_episodes4'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/02/npr_planetmoney_podcasttile_sq-7b7fab0b52fd72826936c3dbe51cff94889797a0-s300-c85.jpg"},
        {
            'label': plugin.get_string(30005),#COLLEGE
            'path': plugin.url_for('all_episodes5'),
            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/npr_lifekit_studentdebt_4__sq-50c0e7692458fc46a7c6cc0189037e364e97253c-s300-c85.png"},
        {
            'label': plugin.get_string(30006),#WHITE
            'path': plugin.url_for('all_episodes6'),
            'thumbnail': "https://media.npr.org/assets/img/2019/04/16/white-lies_final_sq-b1391789cfa7562bf3a4cd0c9cdae27fc4fa01b9-s300-c85.jpg"},
        {
            'label': plugin.get_string(30007),#ROUGH
            'path': plugin.url_for('all_episodes7'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/02/npr_roughtranslation_podcasttile1_sq-3ebceaa9b4811221618fa96a6a685e4db60673d5-s300-c85.jpg"},
        {
            'label': plugin.get_string(30008),#ASK
            'path': plugin.url_for('all_episodes8'),
            'thumbnail': "https://media.npr.org/assets/img/2019/04/05/npr_ama_podcasttile_sq-98e83d8d54ccc8468dc48f07ed0540ef56f8ffa0-s300-c85.jpg"},
        {
            'label': plugin.get_string(30009),#MORNING
            'path': plugin.url_for('all_episodes9'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/06/npr_me_podcasttile_sq-4036eb96471eeed96c37dfba404bb48ea798e78c-s300-c85.jpg"},
        {
            'label': plugin.get_string(3000),#THINGS
            'path': plugin.url_for('all_episodes2'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/06/npr_atc_podcasttile_sq-bcc33a301405d37aa6bdcc090f43d29264915f4a-s300-c85.jpg"},
        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},

        {
            'label': plugin.get_string(3000),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},




    ]

    return items


@plugin.route('/all_music/')
def all_music():
    items = [
        {
            'label': plugin.get_string(30001),#WAIT
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': ""},
    ]

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL-WAIT)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items



if __name__ == '__main__':
    plugin.run()
