from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

#Featured
URL1 = "https://www.npr.org/templates/rss/podcast.php?id=344098539" #WaitWait #30001
URL2 = "https://www.npr.org/rss/podcast.php?id=510313" #HowIbuilt #30002
URL3 = "https://www.npr.org/rss/podcast.php?id=510308" #Hiddenbrain #30003
URL4 = "https://www.npr.org/templates/rss/podcast.php?id=510289" #PlanetMoney #30004
URL5 = "https://www.npr.org/rss/podcast.php?id=510345" #Howtopayforcollege #30005
URL6 = "https://www.npr.org/rss/podcast.php?id=510343" #Whitelies #30006
URL7 = "https://www.npr.org/rss/podcast.php?id=510324" #Roughtrans #30007
URL8 = "https://www.npr.org/rss/podcast.php?id=510299" #Askmeanother #30008

#Daily
#ALT-URL-THINGS = "https://rss-npr-podcasts.herokuapp.com/rss/all-things-considered"
#ALT-URL-MORNING = "https://rss-npr-podcasts.herokuapp.com/rss/morning-edition"
URL9 = "http://npr.pyther.net/podcast/morning-edition"#Morning Edition #30009
URL10 = "http://npr.pyther.net/podcast/all-things-considered"#AllThingsConsidered #30010
URL11 = "https://rss-npr-podcasts.herokuapp.com/rss/weekend-edition-saturday"#WeekendSat #30011
URL12 = "https://rss-npr-podcasts.herokuapp.com/rss/weekend-edition-sunday"#WeekendSun #30012
URL13 = "https://www.npr.org/rss/podcast.php?id=510051" #HereNow #30013
URL14 = "https://www.npr.org/rss/podcast.php?id=510053" #OnpointWBUR #30014
URL15 = "https://www.npr.org/rss/podcast.php?id=510325" #indictatorplanetmoney #30015
URL16 = "https://www.npr.org/rss/podcast.php?id=381444908" #freshair #30016
URL17 = "https://www.npr.org/rss/podcast.php?id=510318" #upfirst #30017
URL18 = "https://www.npr.org/rss/podcast.php?id=510316" #ONEA #30018

#NewsConversations
URL19 = "https://www.npr.org/rss/podcast.php?id=500005" #NPRNewsNow #30019
URL13 = "https://www.npr.org/rss/podcast.php?id=510051" #HereNow #30013
URL14 = "https://www.npr.org/rss/podcast.php?id=510053" #OnpointWBUR #30014
URL15 = "https://www.npr.org/rss/podcast.php?id=510325" #indictatorplanetmoney #30015
URL16 = "https://www.npr.org/rss/podcast.php?id=381444908" #freshair #30016
URL17 = "https://www.npr.org/rss/podcast.php?id=510318" #upfirst #30017
URL18 = "https://www.npr.org/rss/podcast.php?id=510316" #ONEA #30018
URL20 = "https://www.npr.org/rss/podcast.php?id=510326" #Believed #30020
URL21 = "https://www.npr.org/rss/podcast.php?id=510312" #Codesw #30021
URL22 = "https://www.npr.org/rss/podcast.php?id=510311" #Embedded #30022
URL23 = "https://www.npr.org/rss/podcast.php?id=510317" #Itbeenaminute #30023
URL24 = "https://www.npr.org/rss/podcast.php?id=510016" #latinoUSA #30024
URL25 = "https://www.npr.org/rss/podcast.php?id=510310" #NPRpolitics #30025
URL26 = "https://www.npr.org/rss/podcast.php?id=510333" #thoughline #30026
URL27 = "https://www.npr.org/rss/podcast.php?id=510323" #whatsgoodwith #30027
URL28 = "https://www.npr.org/rss/podcast.php?id=4692815" #YRmedia #30028

#StorytellingHumor
URL8 = "https://www.npr.org/rss/podcast.php?id=510299" #Askmeanother #30008
URL29 = "https://www.npr.org/rss/podcast.php?id=510208" #bestofcartalk #30029
URL30 = "https://www.npr.org/rss/podcast.php?id=510309" #bullseye #30030
URL3 = "https://www.npr.org/rss/podcast.php?id=510308" #hiddenbrain #30003
URL2 = "https://www.npr.org/rss/podcast.php?id=510313" #HowIbuilt #30002
URL31 = "https://www.npr.org/templates/rss/podcast.php?id=510307" #invisibila #30031
URL32 = "https://www.npr.org/rss/podcast.php?id=510052" #onlyagame #30032
URL4 = "https://www.npr.org/templates/rss/podcast.php?id=510289" #PlanetMoney #30004
URL1 = "https://www.npr.org/templates/rss/podcast.php?id=344098539" #WaitwaitDont #30001
URL33 = "https://www.npr.org/rss/podcast.php?id=510321" #wowintheworld #30033

#Music
URL34 = "https://www.npr.org/rss/podcast.php?id=510019&uid=n1qe4e85742c986fdb81d2d38ffa0d5d53" #AllSONGS #30034
URL35 = "https://www.npr.org/templates/rss/podcast.php?id=510306"#TinyDesk  #30035
URL36 = "https://www.npr.org/templates/rss/podcast.php?id=510305"#Altlatino #30036
URL37 = "https://feedpress.me/mountainstagepodcast"#NPRMountainStage #30037
URL38 = "https://www.npr.org/rss/podcast.php?id=510026" #Fromthetop #30038
URL39 = "https://www.npr.org/rss/podcast.php?id=510253" #LiveInConcertAllSongsCons #30039

URL40 = "https://www.npr.org/rss/podcast.php?id=510347" #BeAPowerful #30040
URL41 = "http://feeds.feedburner.com/TheFrontlineDispatch" #PBSFrontline #30041
URL42 = "https://feeds.wgbh.org/106/feed-rss.xml" #Innovationhub #30042
URL43 = "https://f.prxu.org/156/feed-rss.xml" #GROUNDTRUTHPROJ #30043

URL44 = "http://npr.org/rss/podcast.php?id=510314" #BIGLISTEN #30044
URL45 = "https://www.npr.org/rss/podcast.php?id=510338" #LIFEKIT #30045

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
#        {
#            'label': plugin.get_string(30105),#MUSIC
#            'path': plugin.url_for('all_music'),
#            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f-s400-c85.png"},
        {
            'label': plugin.get_string(30001),#WAIT
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/wait.jpg"},
        {
            'label': plugin.get_string(30002),#HOW
            'path': plugin.url_for('all_episodes2'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/how.jpg"},
        {
            'label': plugin.get_string(30003),#HIDDEN
            'path': plugin.url_for('all_episodes3'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/hidden.jpg"},
        {
            'label': plugin.get_string(30004),#PLANET
            'path': plugin.url_for('all_episodes4'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/planet.jpg"},
        {
            'label': plugin.get_string(30005),#COLLEGE
            'path': plugin.url_for('all_episodes5'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/college.png"},
        {
            'label': plugin.get_string(30006),#WHITE
            'path': plugin.url_for('all_episodes6'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/white.jpg"},
        {
            'label': plugin.get_string(30007),#ROUGH
            'path': plugin.url_for('all_episodes7'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/rough.jpg"},
        {
            'label': plugin.get_string(30008),#ASK
            'path': plugin.url_for('all_episodes8'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/ask.png"},
        {
            'label': plugin.get_string(30009),#MORNING
            'path': plugin.url_for('all_episodes9'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/morning.jpg"},
        {
            'label': plugin.get_string(30010),#THINGS
            'path': plugin.url_for('all_episodes10'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/things.jpg"},
        {
            'label': plugin.get_string(30011),#WEEKENDSAT
            'path': plugin.url_for('all_episodes11'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/weekendsat.png"},
        {
            'label': plugin.get_string(30012),#WEEKENDSUN
            'path': plugin.url_for('all_episodes12'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/weekendsun.png"},
        {
            'label': plugin.get_string(30013),#HERENOW
            'path': plugin.url_for('all_episodes13'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/herenow.jpg"},
        {
            'label': plugin.get_string(30014),#ONPOINT
            'path': plugin.url_for('all_episodes14'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/onpoint.jpg"},
        {
            'label': plugin.get_string(30015),#INDICATORPLANETMONEY
            'path': plugin.url_for('all_episodes15'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/indicatorplanet.jpg"},
        {
            'label': plugin.get_string(30016),#FRESHAIR
            'path': plugin.url_for('all_episodes16'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/fresh.jpg"},
        {
            'label': plugin.get_string(30017),#UPFIRST
            'path': plugin.url_for('all_episodes17'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/upfirst.jpg"},
        {
            'label': plugin.get_string(30018),#ONEA
            'path': plugin.url_for('all_episodes18'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/onea.jpg"},
        {
            'label': plugin.get_string(30019),#NPRNewsNow
            'path': plugin.url_for('all_episodes19'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/NPRnewsnow.jpg"},
        {
            'label': plugin.get_string(30020),#BELIEVED
            'path': plugin.url_for('all_episodes20'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/believed.jpg"},
        {
            'label': plugin.get_string(30021),#CODESW
            'path': plugin.url_for('all_episodes21'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/codesw.jpg"},
        {
            'label': plugin.get_string(30022),#EMBEDDED
            'path': plugin.url_for('all_episodes22'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/embedded.jpg"},
        {
            'label': plugin.get_string(30023),#ITSBEEN
            'path': plugin.url_for('all_episodes23'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/itsbeen.jpg"},
        {
            'label': plugin.get_string(30024),#LATINOUSA
            'path': plugin.url_for('all_episodes24'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/latinousa.jpg"},
        {
            'label': plugin.get_string(30025),#NPRPOLITICS
            'path': plugin.url_for('all_episodes25'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/NPRpolitics.jpg"},
        {
            'label': plugin.get_string(30026),#THROUGHLINE
            'path': plugin.url_for('all_episodes26'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/through.png"},
        {
            'label': plugin.get_string(30027),#WHATSGOODWITH
            'path': plugin.url_for('all_episodes27'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/whatsgood.jpg"},
        {
            'label': plugin.get_string(30028),#YRMEDIA
            'path': plugin.url_for('all_episodes28'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/YRmedia.png"},
        {
            'label': plugin.get_string(30029),#BESTOFCARTALK
            'path': plugin.url_for('all_episodes29'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/car.jpg"},
        {
            'label': plugin.get_string(30030),#BULLSEYE
            'path': plugin.url_for('all_episodes30'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/bullseye.jpg"},
        {
            'label': plugin.get_string(30031),#INVISIBILIA
            'path': plugin.url_for('all_episodes31'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/invisibilia.jpg"},
        {
            'label': plugin.get_string(30032),#ONLYAGAME
            'path': plugin.url_for('all_episodes32'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/only.jpg"},
        {
            'label': plugin.get_string(30033),#WOWINTHEWORLD
            'path': plugin.url_for('all_episodes33'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/wow.jpg"},
        {
            'label': plugin.get_string(30034),#ALLSONGS
            'path': plugin.url_for('all_episodes34'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/allsongs.jpg"},
        {
            'label': plugin.get_string(30035),#TINYDESK
            'path': plugin.url_for('all_episodes35'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/tiny.jpg"},
        {
            'label': plugin.get_string(30036),#ALTLATINO
            'path': plugin.url_for('all_episodes36'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/altlatino.jpg"},
        {
            'label': plugin.get_string(30037),#NPRMOUNTAIN
            'path': plugin.url_for('all_episodes37'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/mountain.jpg"},
        {
            'label': plugin.get_string(30038),#FROMTHETOP
            'path': plugin.url_for('all_episodes38'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/from.jpeg"},
        {
            'label': plugin.get_string(30039),#LIVEINCONCERTALLSONGSCONS
            'path': plugin.url_for('all_episodes39'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/live.jpg"},
        {
            'label': plugin.get_string(30040),#BEPOWERFUL
            'path': plugin.url_for('all_episodes40'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/be.png"},
        {
            'label': plugin.get_string(30041),#PBSFRONTLINE
            'path': plugin.url_for('all_episodes41'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/PBS.png"},
        {
            'label': plugin.get_string(30042),#INNOVATIONHUB
            'path': plugin.url_for('all_episodes42'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/innovation.jpeg"},
        {
            'label': plugin.get_string(30043),#GROUNDTRUTHPROJ
            'path': plugin.url_for('all_episodes43'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/ground.jpg"},
        {
            'label': plugin.get_string(30044),#BIGLISTEN
            'path': plugin.url_for('all_episodes44'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/big.png"},
        {
            'label': plugin.get_string(30045),#LIFEKITALLGUIDES
            'path': plugin.url_for('all_episodes45'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/lifekitallguides.png"},

    ]
    return items

#@plugin.route('/all_music/')
#def all_music():
#    items = [
#        {
#            'label': plugin.get_string(30001),#WAIT
#            'path': plugin.url_for('all_episodes1'),
#            'thumbnail': ""},
#    ]

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/all_episodes2/')
def all_episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/all_episodes3/')
def all_episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/all_episodes4/')
def all_episodes4():
    soup4 = mainaddon.get_soup4(URL4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/all_episodes5/')
def all_episodes5():
    soup5 = mainaddon.get_soup5(URL5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/all_episodes6/')
def all_episodes6():
    soup6 = mainaddon.get_soup6(URL6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/all_episodes7/')
def all_episodes7():
    soup7 = mainaddon.get_soup7(URL7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/all_episodes8/')
def all_episodes8():
    soup8 = mainaddon.get_soup8(URL8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/all_episodes9/')
def all_episodes9():
    soup9 = mainaddon.get_soup9(URL9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/all_episodes10/')
def all_episodes10():
    soup10 = mainaddon.get_soup10(URL10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/all_episodes11/')
def all_episodes11():
    soup11 = mainaddon.get_soup11(URL11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/all_episodes12/')
def all_episodes12():
    soup12 = mainaddon.get_soup12(URL12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/all_episodes13/')
def all_episodes13():
    soup13 = mainaddon.get_soup13(URL13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/all_episodes14/')
def all_episodes14():
    soup14 = mainaddon.get_soup14(URL14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/all_episodes15/')
def  all_episodes15():
    soup15 = mainaddon.get_soup15(URL15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/all_episodes16/')
def  all_episodes16():
    soup16 = mainaddon.get_soup16(URL16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/all_episodes17/')
def  all_episodes17():
    soup17 = mainaddon.get_soup17(URL17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/all_episodes18/')
def  all_episodes18():
    soup18 = mainaddon.get_soup18(URL18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/all_episodes19/')
def  all_episodes19():
    soup19 = mainaddon.get_soup19(URL19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items
@plugin.route('/all_episodes19/')
def  all_episodes20():
    soup20 = mainaddon.get_soup20(URL20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items
@plugin.route('/all_episodes20/')
def  all_episodes21():
    soup21 = mainaddon.get_soup21(URL21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items
@plugin.route('/all_episodes22/')
def  all_episodes22():
    soup22 = mainaddon.get_soup22(URL22)
    playable_podcast22 = mainaddon.get_playable_podcast22(soup22)
    items = mainaddon.compile_playable_podcast22(playable_podcast22)
    return items
@plugin.route('/all_episodes23/')
def  all_episodes23():
    soup23 = mainaddon.get_soup23(URL23)
    playable_podcast23 = mainaddon.get_playable_podcast23(soup23)
    items = mainaddon.compile_playable_podcast23(playable_podcast23)
    return items
@plugin.route('/all_episodes24/')
def  all_episodes24():
    soup24 = mainaddon.get_soup24(URL24)
    playable_podcast24 = mainaddon.get_playable_podcast24(soup24)
    items = mainaddon.compile_playable_podcast24(playable_podcast24)
    return items
@plugin.route('/all_episodes25/')
def  all_episodes25():
    soup25 = mainaddon.get_soup25(URL25)
    playable_podcast25 = mainaddon.get_playable_podcast25(soup25)
    items = mainaddon.compile_playable_podcast25(playable_podcast25)
    return items
@plugin.route('/all_episodes26/')
def  all_episodes26():
    soup26 = mainaddon.get_soup26(URL26)
    playable_podcast26 = mainaddon.get_playable_podcast26(soup26)
    items = mainaddon.compile_playable_podcast26(playable_podcast26)
    return items
@plugin.route('/all_episodes27/')
def  all_episodes27():
    soup27 = mainaddon.get_soup27(URL27)
    playable_podcast27 = mainaddon.get_playable_podcast27(soup27)
    items = mainaddon.compile_playable_podcast27(playable_podcast27)
    return items
@plugin.route('/all_episodes28/')
def  all_episodes28():
    soup28 = mainaddon.get_soup28(URL28)
    playable_podcast28 = mainaddon.get_playable_podcast28(soup28)
    items = mainaddon.compile_playable_podcast28(playable_podcast28)
    return items
@plugin.route('/all_episodes29/')
def  all_episodes29():
    soup29 = mainaddon.get_soup29(URL29)
    playable_podcast29 = mainaddon.get_playable_podcast29(soup29)
    items = mainaddon.compile_playable_podcast29(playable_podcast29)
    return items
@plugin.route('/all_episodes30/')
def  all_episodes30():
    soup30 = mainaddon.get_soup30(URL30)
    playable_podcast30 = mainaddon.get_playable_podcast30(soup30)
    items = mainaddon.compile_playable_podcast30(playable_podcast30)
    return items
@plugin.route('/all_episodes31/')
def all_episodes31():
    soup31 = mainaddon.get_soup31(URL31)
    playable_podcast31 = mainaddon.get_playable_podcast31(soup31)
    items = mainaddon.compile_playable_podcast31(playable_podcast31)
    return items
@plugin.route('/all_episodes32/')
def  all_episodes32():
    soup32 = mainaddon.get_soup32(URL32)
    playable_podcast32 = mainaddon.get_playable_podcast32(soup32)
    items = mainaddon.compile_playable_podcast32(playable_podcast32)
    return items
@plugin.route('/all_episodes33/')
def  all_episodes33():
    soup33 = mainaddon.get_soup33(URL33)
    playable_podcast33 = mainaddon.get_playable_podcast33(soup33)
    items = mainaddon.compile_playable_podcast33(playable_podcast33)
    return items
@plugin.route('/all_episodes34/')
def  all_episodes34():
    soup34 = mainaddon.get_soup34(URL34)
    playable_podcast34 = mainaddon.get_playable_podcast34(soup34)
    items = mainaddon.compile_playable_podcast34(playable_podcast34)
    return items
@plugin.route('/all_episodes35/')
def  all_episodes35():
    soup35 = mainaddon.get_soup35(URL35)
    playable_podcast35 = mainaddon.get_playable_podcast35(soup35)
    items = mainaddon.compile_playable_podcast35(playable_podcast35)
    return items
@plugin.route('/all_episodes36/')
def  all_episodes36():
    soup36 = mainaddon.get_soup36(URL36)
    playable_podcast36 = mainaddon.get_playable_podcast36(soup36)
    items = mainaddon.compile_playable_podcast36(playable_podcast36)
    return items
@plugin.route('/all_episodes37/')
def  all_episodes37():
    soup37 = mainaddon.get_soup37(URL37)
    playable_podcast37 = mainaddon.get_playable_podcast37(soup37)
    items = mainaddon.compile_playable_podcast37(playable_podcast37)
    return items
@plugin.route('/all_episodes38/')
def  all_episodes38():
    soup38 = mainaddon.get_soup38(URL38)
    playable_podcast38 = mainaddon.get_playable_podcast38(soup38)
    items = mainaddon.compile_playable_podcast38(playable_podcast38)
    return items
@plugin.route('/all_episodes39/')
def  all_episodes39():
    soup39 = mainaddon.get_soup39(URL39)
    playable_podcast39 = mainaddon.get_playable_podcast39(soup39)
    items = mainaddon.compile_playable_podcast39(playable_podcast39)
    return items
@plugin.route('/all_episodes40/')
def  all_episodes40():
    soup40 = mainaddon.get_soup40(URL40)
    playable_podcast40 = mainaddon.get_playable_podcast40(soup40)
    items = mainaddon.compile_playable_podcast40(playable_podcast40)
    return items
@plugin.route('/all_episodes41/')
def  all_episodes41():
    soup41 = mainaddon.get_soup41(URL41)
    playable_podcast41 = mainaddon.get_playable_podcast41(soup41)
    items = mainaddon.compile_playable_podcast41(playable_podcast41)
    return items
@plugin.route('/all_episodes42/')
def  all_episodes42():
    soup42 = mainaddon.get_soup42(URL42)
    playable_podcast42 = mainaddon.get_playable_podcast42(soup42)
    items = mainaddon.compile_playable_podcast42(playable_podcast42)
    return items
@plugin.route('/all_episodes43/')
def  all_episodes43():
    soup43 = mainaddon.get_soup43(URL43)
    playable_podcast43 = mainaddon.get_playable_podcast43(soup43)
    items = mainaddon.compile_playable_podcast43(playable_podcast43)
    return items
@plugin.route('/all_episodes44/')
def  all_episodes44():
    soup44 = mainaddon.get_soup44(URL44)
    playable_podcast44 = mainaddon.get_playable_podcast44(soup44)
    items = mainaddon.compile_playable_podcast44(playable_podcast44)
    return items
@plugin.route('/all_episodes45/')
def  all_episodes45():
    soup45 = mainaddon.get_soup45(URL45)
    playable_podcast45 = mainaddon.get_playable_podcast45(soup45)
    items = mainaddon.compile_playable_podcast45(playable_podcast45)
    return items

if __name__ == '__main__':
    plugin.run()
