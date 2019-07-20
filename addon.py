
from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

#Featured
URL-HIDDEN = "https://www.npr.org/rss/podcast.php?id=510308" #Hiddenbrain #30003
URL-BUILT = "https://www.npr.org/rss/podcast.php?id=510313" #HowIbuilt #30002
URL-WAIT = "https://www.npr.org/templates/rss/podcast.php?id=344098539" #WaitWait #30001
URL-PLANET = "https://www.npr.org/templates/rss/podcast.php?id=510289" #PlanetMoney #30004
URL-COLLEGE = "https://www.npr.org/rss/podcast.php?id=510345" #Howtopayforcollege #30005
URL-WHITE = "https://www.npr.org/rss/podcast.php?id=510343" #Whitelies #30006
URL-ROUGH = "https://www.npr.org/rss/podcast.php?id=510324" #Roughtrans #30007
URL-ASK = "https://www.npr.org/rss/podcast.php?id=510299" #Askmeanother #30008

#Daily
#ALT-URL-THINGS = "https://rss-npr-podcasts.herokuapp.com/rss/all-things-considered"
#ALT-URL-MORNING = "https://rss-npr-podcasts.herokuapp.com/rss/morning-edition"
URL-WEEKENDSAT = "https://rss-npr-podcasts.herokuapp.com/rss/weekend-edition-saturday"#WeekendSat #30011
URL-WEEKENDSUN = "https://rss-npr-podcasts.herokuapp.com/rss/weekend-edition-sunday"#WeekendSun #30012
URL-MORNING = "http://npr.pyther.net/podcast/morning-edition"#Morning Edition #30009
URL-THINGS = "http://npr.pyther.net/podcast/all-things-considered"#AllThingsConsidered #30010
URL-HERE = "https://www.npr.org/rss/podcast.php?id=510051" #HereNow #30013
URL-ONPOINT = "https://www.npr.org/rss/podcast.php?id=510053" #OnpointWBUR #30014
URL-INDICATOR = "https://www.npr.org/rss/podcast.php?id=510325" #indictatorplanetmoney #30015
URL-FRESH = "https://www.npr.org/rss/podcast.php?id=381444908" #freshair #30016
URL-UP = "https://www.npr.org/rss/podcast.php?id=510318" #upfirst #30017
URL-1A = "https://www.npr.org/rss/podcast.php?id=510316" #1A #30018

#NewsConversations
URL-NOW = "https://www.npr.org/rss/podcast.php?id=500005" #NPRNewsNow #30019
URL-HERE = "https://www.npr.org/rss/podcast.php?id=510051" #HereNow #30013
URL-ONPOINT = "https://www.npr.org/rss/podcast.php?id=510053" #OnpointWBUR #30014
URL-INDICATOR = "https://www.npr.org/rss/podcast.php?id=510325" #indictatorplanetmoney #30015
URL-FRESH = "https://www.npr.org/rss/podcast.php?id=381444908" #freshair #30016
URL-UP = "https://www.npr.org/rss/podcast.php?id=510318" #upfirst #30017
URL-1A = "https://www.npr.org/rss/podcast.php?id=510316" #1A #30018
URL-BELIEVED = "https://www.npr.org/rss/podcast.php?id=510326" #Believed #30020
URL-CODE = "https://www.npr.org/rss/podcast.php?id=510312" #Codesw #30021
URL-EMBEDDED = "https://www.npr.org/rss/podcast.php?id=510311" #Embedded #30022
URL-ITBEEN = "https://www.npr.org/rss/podcast.php?id=510317" #Itbeenaminute #30023
URL-LATINO = "https://www.npr.org/rss/podcast.php?id=510016" #latinoUSA #30024
URL-POLITICS = "https://www.npr.org/rss/podcast.php?id=510310" #NPRpolitics #30025
URL-THROUGH = "https://www.npr.org/rss/podcast.php?id=510333" #thoughline #30026
URL-WHATS = "https://www.npr.org/rss/podcast.php?id=510323" #whatsgoodwith #30027
URL-YR = "https://www.npr.org/rss/podcast.php?id=4692815" #YRmedia #30028

#StorytellingHumor
URL-ASK = "https://www.npr.org/rss/podcast.php?id=510299" #Askmeanother #30008
URL-CAR = "https://www.npr.org/rss/podcast.php?id=510208" #bestofcartalk #30029
URL-BULLSEYE = "https://www.npr.org/rss/podcast.php?id=510309" #bullseye #30030
URL-HIDDEN = "https://www.npr.org/rss/podcast.php?id=510308" #hiddenbrain #30003
URL-BUILT = "https://www.npr.org/rss/podcast.php?id=510313" #HowIbuilt #30002
URL-INVISIBILIA = "https://www.npr.org/templates/rss/podcast.php?id=510307" #invisibila #30031
URL-ONLY = "https://www.npr.org/rss/podcast.php?id=510052" #onlyagame #30032
URL-PLANET = "https://www.npr.org/templates/rss/podcast.php?id=510289" #PlanetMoney #30004
URL-WAIT = "https://www.npr.org/templates/rss/podcast.php?id=344098539" #WaitwaitDont #30001
URL-WOW = "https://www.npr.org/rss/podcast.php?id=510321" #wowintheworld #30033

#Music
URL-SONGS = "https://www.npr.org/rss/podcast.php?id=510019&uid=n1qe4e85742c986fdb81d2d38ffa0d5d53" #AllSONGS #30034
URL-TINY = "https://www.npr.org/templates/rss/podcast.php?id=510306"#TinyDesk  #30035
URL-LATINO = "https://www.npr.org/templates/rss/podcast.php?id=510305"#Altlatino #30036
URL-MOUNTAIN = "https://feedpress.me/mountainstagepodcast"#NPRMountainStage #30037
URL-FTT = "https://www.npr.org/rss/podcast.php?id=510026" #Fromthetop #30038
URL-LIVE = "https://www.npr.org/rss/podcast.php?id=510253" #LiveInConcertAllSongsCons #30039


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
            'label': plugin.get_string(30010),#THINGS
            'path': plugin.url_for('all_episodes10'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/06/npr_atc_podcasttile_sq-bcc33a301405d37aa6bdcc090f43d29264915f4a-s300-c85.jpg"},
        {
            'label': plugin.get_string(30011),#WEEKENDSAT
            'path': plugin.url_for('all_episodes11'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30012),#WEEKENDSUN
            'path': plugin.url_for('all_episodes12'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30013),#HERENOW
            'path': plugin.url_for('all_episodes13'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30014),#ONPOINT
            'path': plugin.url_for('all_episodes14'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30015),#INDICATORPLANETMONEY
            'path': plugin.url_for('all_episodes15'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30016),#FRESHAIR
            'path': plugin.url_for('all_episodes16'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30017),#UPFIRST
            'path': plugin.url_for('all_episodes17'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30018),#1A
            'path': plugin.url_for('all_episodes18'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30019),#NPRNewsNow
            'path': plugin.url_for('all_episodes19'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30020),#BELIEVED
            'path': plugin.url_for('all_episodes20'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30021),#CODESW
            'path': plugin.url_for('all_episodes21'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30022),#EMBEDDED
            'path': plugin.url_for('all_episodes22'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30023),#ITSBEEN
            'path': plugin.url_for('all_episodes23'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30024),#LATINOUSA
            'path': plugin.url_for('all_episodes24'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30025),#NPRPOLITICS
            'path': plugin.url_for('all_episodes25'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30026),#THROUGHLINE
            'path': plugin.url_for('all_episodes26'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30027),#WHATSGOODWITH
            'path': plugin.url_for('all_episodes27'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30028),#YRMEDIA
            'path': plugin.url_for('all_episodes28'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30029),#BESTOFCARTALK
            'path': plugin.url_for('all_episodes29'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30030),#BULLSEYE
            'path': plugin.url_for('all_episodes30'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30031),#INVISIBILIA
            'path': plugin.url_for('all_episodes31'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30032),#ONLYAGAME
            'path': plugin.url_for('all_episodes32'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30033),#WOWINTHEWORLD
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30034),#ALLSONGS
            'path': plugin.url_for('all_episodes34'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30035),#TINYDESK
            'path': plugin.url_for('all_episodes35'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30036),#ALTLATINO
            'path': plugin.url_for('all_episodes36'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30037),#NPRMOUNTAIN
            'path': plugin.url_for('all_episodes37'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30038),#FROMTHETOP
            'path': plugin.url_for('all_episodes38'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30039),#LIVEINCONCERTALLSONGSCONS
            'path': plugin.url_for('all_episodes39'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
            'path': plugin.url_for('all_episodes'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(300),#
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


@plugin.route('/all_episodes2/')
def all_episodes2():
    soup2 = mainaddon.get_soup(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast1(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/all_episodes3/')
def all_episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast1(soup3)
    items = mainaddon.compile_playable_podcast1(playable_podcast3)
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

@plugin.route('/ all_episodes15/')
def  all_episodes15():
    soup15 = mainaddon.get_soup15(URL15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/ all_episodes16/')
def  all_episodes16():
    soup16 = mainaddon.get_soup16(URL16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/ all_episodes17/')
def  all_episodes17():
    soup17 = mainaddon.get_soup17(URL17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/ all_episodes18/')
def  all_episodes18():
    soup18 = mainaddon.get_soup18(URL18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/ all_episodes19/')
def  all_episodes19():
    soup19 = mainaddon.get_soup19(URL19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items@plugin.route('/ all_episodes19/')
def  all_episodes20():
    soup20 = mainaddon.get_soup20(URL20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items@plugin.route('/ all_episodes20/')
def  all_episodes21():
    soup21 = mainaddon.get_soup21(URL21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items
@plugin.route('/ all_episodes22/')
def  all_episodes22():
    soup22 = mainaddon.get_soup22(URL22)
    playable_podcast22 = mainaddon.get_playable_podcast22(soup22)
    items = mainaddon.compile_playable_podcast22(playable_podcast22)
    return items
@plugin.route('/ all_episodes23/')
def  all_episodes23():
    soup23 = mainaddon.get_soup23(URL23)
    playable_podcast23 = mainaddon.get_playable_podcast23(soup23)
    items = mainaddon.compile_playable_podcast23(playable_podcast23)
    return items
@plugin.route('/ all_episodes24/')
def  all_episodes24():
    soup24 = mainaddon.get_soup24(URL24)
    playable_podcast24 = mainaddon.get_playable_podcast24(soup24)
    items = mainaddon.compile_playable_podcast24(playable_podcast24)
    return items
@plugin.route('/ all_episodes25/')
def  all_episodes25():
    soup25 = mainaddon.get_soup25(URL25)
    playable_podcast25 = mainaddon.get_playable_podcast25(soup25)
    items = mainaddon.compile_playable_podcast25(playable_podcast25)
    return items
@plugin.route('/ all_episodes26/')
def  all_episodes26():
    soup26 = mainaddon.get_soup26(URL26)
    playable_podcast26 = mainaddon.get_playable_podcast26(soup26)
    items = mainaddon.compile_playable_podcast26(playable_podcast26)
    return items
@plugin.route('/ all_episodes27/')
def  all_episodes27():
    soup27 = mainaddon.get_soup27(URL27)
    playable_podcast27 = mainaddon.get_playable_podcast27(soup27)
    items = mainaddon.compile_playable_podcast27(playable_podcast27)
    return items
@plugin.route('/ all_episodes28/')
def  all_episodes28():
    soup28 = mainaddon.get_soup28(URL28)
    playable_podcast28 = mainaddon.get_playable_podcast28(soup28)
    items = mainaddon.compile_playable_podcast28(playable_podcast28)
    return items
@plugin.route('/ all_episodes29/')
def  all_episodes29():
    soup29 = mainaddon.get_soup29(URL29)
    playable_podcast29 = mainaddon.get_playable_podcast29(soup29)
    items = mainaddon.compile_playable_podcast29(playable_podcast29)
    return items
@plugin.route('/ all_episodes30/')
def  all_episodes30():
    soup30 = mainaddon.get_soup30(URL30)
    playable_podcast30 = mainaddon.get_playable_podcast30(soup30)
    items = mainaddon.compile_playable_podcast30(playable_podcast3)
    return items
@plugin.route('/all_episodes31/')
def all_episodes31():
    soup31 = mainaddon.get_soup31(URL31)
    playable_podcast31 = mainaddon.get_playable_podcast31(soup31)
    items = mainaddon.compile_playable_podcast31(playable_podcast3)
    return items
@plugin.route('/ all_episodes32/')
def  all_episodes32():
    soup32 = mainaddon.get_soup32(URL32)
    playable_podcast32 = mainaddon.get_playable_podcast32(soup32)
    items = mainaddon.compile_playable_podcast32(playable_podcast3)
    return items
@plugin.route('/ all_episodes33/')
def  all_episodes33():
    soup33 = mainaddon.get_soup33(URL33)
    playable_podcast33 = mainaddon.get_playable_podcast33(soup33)
    items = mainaddon.compile_playable_podcast33(playable_podcast3)
    return items
@plugin.route('/ all_episodes34/')
def  all_episodes34():
    soup34 = mainaddon.get_soup34(URL34)
    playable_podcast34 = mainaddon.get_playable_podcast34(soup34)
    items = mainaddon.compile_playable_podcast34(playable_podcast3)
    return items
@plugin.route('/ all_episodes35/')
def  all_episodes35():
    soup35 = mainaddon.get_soup35(URL35)
    playable_podcast35 = mainaddon.get_playable_podcast35(soup35)
    items = mainaddon.compile_playable_podcast35(playable_podcast3)
    return items
@plugin.route('/ all_episodes36/')
def  all_episodes36():
    soup36 = mainaddon.get_soup36(URL36)
    playable_podcast36 = mainaddon.get_playable_podcast36(soup36)
    items = mainaddon.compile_playable_podcast36(playable_podcast3)
    return items
@plugin.route('/ all_episodes37/')
def  all_episodes37():
    soup37 = mainaddon.get_soup37(URL37)
    playable_podcast37 = mainaddon.get_playable_podcast37(soup37)
    items = mainaddon.compile_playable_podcast37(playable_podcast3)
    return items
@plugin.route('/ all_episodes38/')
def  all_episodes38():
    soup38 = mainaddon.get_soup38(URL38)
    playable_podcast38 = mainaddon.get_playable_podcast38(soup38)
    items = mainaddon.compile_playable_podcast38(playable_podcast3)
    return items
@plugin.route('/ all_episodes39/')
def  all_episodes39():
    soup39 = mainaddon.get_soup39(URL39)
    playable_podcast39 = mainaddon.get_playable_podcast39(soup39)
    items = mainaddon.compile_playable_podcast39(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
