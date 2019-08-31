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
    items = [
#        {
#            'label': plugin.get_string(30105),#MUSIC
#            'path': plugin.url_for('all_music'),
#            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f-s400-c85.png"},
        {
            'label': plugin.get_string(30001),#WAIT
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/screen-shot-2019-05-23-at-8.46.21-am_sq-7dcea391e7a87ca3569fe3d2047dda0144e5d86f-s200-c85.png"},
        {
            'label': plugin.get_string(30002),#HOW
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hibt_podcasttile_sq-98320b282169a8cea04a406530e6e7b957665b3f-s200-c85.jpg"},
        {
            'label': plugin.get_string(30003),#HIDDEN
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/03/npr_hiddenbrain_podcasttile_sq-270ab642de6948802f485c6ad1f087239ef6e324-s200-c85.jpg"},
        {
            'label': plugin.get_string(30004),#PLANET
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/02/npr_planetmoney_podcasttile_sq-7b7fab0b52fd72826936c3dbe51cff94889797a0-s200-c85.jpg"},
        {
            'label': plugin.get_string(30005),#COLLEGE
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://media.npr.org/assets/img/2019/05/23/npr_lifekit_studentdebt_4__sq-50c0e7692458fc46a7c6cc0189037e364e97253c-s200-c85.png"},
        {
            'label': plugin.get_string(30006),#WHITE
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://media.npr.org/assets/img/2019/04/16/white-lies_final_sq-b1391789cfa7562bf3a4cd0c9cdae27fc4fa01b9-s200-c85.jpg"},
        {
            'label': plugin.get_string(30007),#ROUGH
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/02/npr_roughtranslation_podcasttile1_sq-3ebceaa9b4811221618fa96a6a685e4db60673d5-s800-c15.jpg"},
        {
            'label': plugin.get_string(30008),#ASK
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://media.npr.org/assets/img/2019/04/05/npr_ama_podcasttile_sq-98e83d8d54ccc8468dc48f07ed0540ef56f8ffa0-s800-c15.jpg"},
        {
            'label': plugin.get_string(30009),#MORNING
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://media.npr.org/assets/img/2018/08/06/npr_me_podcasttile_sq-4036eb96471eeed96c37dfba404bb48ea798e78c.jpg?s=12"},
        {
            'label': plugin.get_string(30010),#THINGS
            'path': plugin.url_for('episodes10'),
            'thumbnail': "http://mediad.publicbroadcasting.net/p/nwpr/files/201201/AllThingsConsidered_2.jpg"},
        {
            'label': plugin.get_string(30011),#WEEKENDSAT
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/weekendsat.png"},
        {
            'label': plugin.get_string(30012),#WEEKENDSUN
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/weekendsun.png"},
        {
            'label': plugin.get_string(30013),#HERENOW
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/herenow.jpg"},
        {
            'label': plugin.get_string(30014),#ONPOINT
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/onpoint.jpg"},
        {
            'label': plugin.get_string(30015),#INDICATORPLANETMONEY
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/indicatorplanet.jpg"},
        {
            'label': plugin.get_string(30016),#FRESHAIR
            'path': plugin.url_for('episodes16'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/fresh.jpg"},
        {
            'label': plugin.get_string(30017),#UPFIRST
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/upfirst.jpg"},
        {
            'label': plugin.get_string(30018),#ONEA
            'path': plugin.url_for('episodes18'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/onea.jpg"},
        {
            'label': plugin.get_string(30019),#NPRNewsNow
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/NPRnewsnow.jpg"},
        {
            'label': plugin.get_string(30020),#BELIEVED
            'path': plugin.url_for('episodes20'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/believed.jpg"},
        {
            'label': plugin.get_string(30021),#CODESW
            'path': plugin.url_for('episodes21'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/codesw.jpg"},
        {
            'label': plugin.get_string(30022),#EMBEDDED
            'path': plugin.url_for('episodes22'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/embedded.jpg"},
        {
            'label': plugin.get_string(30023),#ITSBEEN
            'path': plugin.url_for('episodes23'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/itsbeen.jpg"},
        {
            'label': plugin.get_string(30024),#LATINOUSA
            'path': plugin.url_for('episodes24'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/latinousa.jpg"},
        {
            'label': plugin.get_string(30025),#NPRPOLITICS
            'path': plugin.url_for('episodes25'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/NPRpolitics.jpg"},
        {
            'label': plugin.get_string(30026),#THROUGHLINE
            'path': plugin.url_for('episodes26'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/through.png"},
        {
            'label': plugin.get_string(30027),#WHATSGOODWITH
            'path': plugin.url_for('episodes27'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/whatsgood.jpg"},
        {
            'label': plugin.get_string(30028),#YRMEDIA
            'path': plugin.url_for('episodes28'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/YRmedia.png"},
        {
            'label': plugin.get_string(30029),#BESTOFCARTALK
            'path': plugin.url_for('episodes29'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/car.jpg"},
        {
            'label': plugin.get_string(30030),#BULLSEYE
            'path': plugin.url_for('episodes30'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/bullseye.jpg"},
        {
            'label': plugin.get_string(30031),#INVISIBILIA
            'path': plugin.url_for('episodes31'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/invisibilia.jpg"},
        {
            'label': plugin.get_string(30032),#ONLYAGAME
            'path': plugin.url_for('episodes32'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/only.jpg"},
        {
            'label': plugin.get_string(30033),#WOWINTHEWORLD
            'path': plugin.url_for('episodes33'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/wow.jpg"},
        {
            'label': plugin.get_string(30034),#ALLSONGS
            'path': plugin.url_for('episodes34'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/allsongs.jpg"},
        {
            'label': plugin.get_string(30035),#TINYDESK
            'path': plugin.url_for('episodes35'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/tiny.jpg"},
        {
            'label': plugin.get_string(30036),#ALTLATINO
            'path': plugin.url_for('episodes36'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/altlatino.jpg"},
        {
            'label': plugin.get_string(30037),#NPRMOUNTAIN
            'path': plugin.url_for('episodes37'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/mountain.jpg"},
        {
            'label': plugin.get_string(30038),#FROMTHETOP
            'path': plugin.url_for('episodes38'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/from.jpeg"},
        {
            'label': plugin.get_string(30039),#LIVEINCONCERTALLSONGSCONS
            'path': plugin.url_for('episodes39'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/live.jpg"},
        {
            'label': plugin.get_string(30040),#BEPOWERFUL
            'path': plugin.url_for('episodes40'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/be.png"},
        {
            'label': plugin.get_string(30041),#PBSFRONTLINE
            'path': plugin.url_for('episodes41'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/PBS.png"},
        {
            'label': plugin.get_string(30042),#INNOVATIONHUB
            'path': plugin.url_for('episodes42'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/innovation.jpeg"},
        {
            'label': plugin.get_string(30043),#GROUNDTRUTHPROJ
            'path': plugin.url_for('episodes43'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/ground.jpg"},
        {
            'label': plugin.get_string(30044),#BIGLISTEN
            'path': plugin.url_for('episodes44'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/big.png"},
        {
            'label': plugin.get_string(30045),#LIFEKITALLGUIDES
            'path': plugin.url_for('episodes45'),
            'thumbnail': "https://raw.githubusercontent.com/leopheard/NPRpodcasts/master/resources/media/lifekitallguides.png"},

    ]
    return items

#@plugin.route('/all_music/')
#def all_music():
#    items = [
#        {
#            'label': plugin.get_string(30001),#WAIT
#            'path': plugin.url_for('episodes1'),
#            'thumbnail': ""},
#    ]

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(URL4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(URL5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(URL6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(URL7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(URL8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(URL9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(URL10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(URL11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(URL12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(URL13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(URL14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/episodes15/')
def  episodes15():
    soup15 = mainaddon.get_soup15(URL15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/episodes16/')
def  episodes16():
    soup16 = mainaddon.get_soup16(URL16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/episodes17/')
def  episodes17():
    soup17 = mainaddon.get_soup17(URL17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/episodes18/')
def  episodes18():
    soup18 = mainaddon.get_soup18(URL18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/episodes19/')
def  episodes19():
    soup19 = mainaddon.get_soup19(URL19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items
@plugin.route('/episodes20/')
def  episodes20():
    soup20 = mainaddon.get_soup20(URL20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items
@plugin.route('/episodes21/')
def  episodes21():
    soup21 = mainaddon.get_soup21(URL21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items
@plugin.route('/episodes22/')
def  episodes22():
    soup22 = mainaddon.get_soup22(URL22)
    playable_podcast22 = mainaddon.get_playable_podcast22(soup22)
    items = mainaddon.compile_playable_podcast22(playable_podcast22)
    return items
@plugin.route('/episodes23/')
def  episodes23():
    soup23 = mainaddon.get_soup23(URL23)
    playable_podcast23 = mainaddon.get_playable_podcast23(soup23)
    items = mainaddon.compile_playable_podcast23(playable_podcast23)
    return items
@plugin.route('/episodes24/')
def  episodes24():
    soup24 = mainaddon.get_soup24(URL24)
    playable_podcast24 = mainaddon.get_playable_podcast24(soup24)
    items = mainaddon.compile_playable_podcast24(playable_podcast24)
    return items
@plugin.route('/episodes25/')
def  episodes25():
    soup25 = mainaddon.get_soup25(URL25)
    playable_podcast25 = mainaddon.get_playable_podcast25(soup25)
    items = mainaddon.compile_playable_podcast25(playable_podcast25)
    return items
@plugin.route('/episodes26/')
def  episodes26():
    soup26 = mainaddon.get_soup26(URL26)
    playable_podcast26 = mainaddon.get_playable_podcast26(soup26)
    items = mainaddon.compile_playable_podcast26(playable_podcast26)
    return items
@plugin.route('/episodes27/')
def  episodes27():
    soup27 = mainaddon.get_soup27(URL27)
    playable_podcast27 = mainaddon.get_playable_podcast27(soup27)
    items = mainaddon.compile_playable_podcast27(playable_podcast27)
    return items
@plugin.route('/episodes28/')
def  episodes28():
    soup28 = mainaddon.get_soup28(URL28)
    playable_podcast28 = mainaddon.get_playable_podcast28(soup28)
    items = mainaddon.compile_playable_podcast28(playable_podcast28)
    return items
@plugin.route('/episodes29/')
def  episodes29():
    soup29 = mainaddon.get_soup29(URL29)
    playable_podcast29 = mainaddon.get_playable_podcast29(soup29)
    items = mainaddon.compile_playable_podcast29(playable_podcast29)
    return items
@plugin.route('/episodes30/')
def  episodes30():
    soup30 = mainaddon.get_soup30(URL30)
    playable_podcast30 = mainaddon.get_playable_podcast30(soup30)
    items = mainaddon.compile_playable_podcast30(playable_podcast30)
    return items
@plugin.route('/episodes31/')
def episodes31():
    soup31 = mainaddon.get_soup31(URL31)
    playable_podcast31 = mainaddon.get_playable_podcast31(soup31)
    items = mainaddon.compile_playable_podcast31(playable_podcast31)
    return items
@plugin.route('/episodes32/')
def  episodes32():
    soup32 = mainaddon.get_soup32(URL32)
    playable_podcast32 = mainaddon.get_playable_podcast32(soup32)
    items = mainaddon.compile_playable_podcast32(playable_podcast32)
    return items
@plugin.route('/episodes33/')
def  episodes33():
    soup33 = mainaddon.get_soup33(URL33)
    playable_podcast33 = mainaddon.get_playable_podcast33(soup33)
    items = mainaddon.compile_playable_podcast33(playable_podcast33)
    return items
@plugin.route('/episodes34/')
def  episodes34():
    soup34 = mainaddon.get_soup34(URL34)
    playable_podcast34 = mainaddon.get_playable_podcast34(soup34)
    items = mainaddon.compile_playable_podcast34(playable_podcast34)
    return items
@plugin.route('/episodes35/')
def  episodes35():
    soup35 = mainaddon.get_soup35(URL35)
    playable_podcast35 = mainaddon.get_playable_podcast35(soup35)
    items = mainaddon.compile_playable_podcast35(playable_podcast35)
    return items
@plugin.route('/episodes36/')
def  episodes36():
    soup36 = mainaddon.get_soup36(URL36)
    playable_podcast36 = mainaddon.get_playable_podcast36(soup36)
    items = mainaddon.compile_playable_podcast36(playable_podcast36)
    return items
@plugin.route('/episodes37/')
def  episodes37():
    soup37 = mainaddon.get_soup37(URL37)
    playable_podcast37 = mainaddon.get_playable_podcast37(soup37)
    items = mainaddon.compile_playable_podcast37(playable_podcast37)
    return items
@plugin.route('/episodes38/')
def  episodes38():
    soup38 = mainaddon.get_soup38(URL38)
    playable_podcast38 = mainaddon.get_playable_podcast38(soup38)
    items = mainaddon.compile_playable_podcast38(playable_podcast38)
    return items
@plugin.route('/episodes39/')
def  episodes39():
    soup39 = mainaddon.get_soup39(URL39)
    playable_podcast39 = mainaddon.get_playable_podcast39(soup39)
    items = mainaddon.compile_playable_podcast39(playable_podcast39)
    return items
@plugin.route('/episodes40/')
def  episodes40():
    soup40 = mainaddon.get_soup40(URL40)
    playable_podcast40 = mainaddon.get_playable_podcast40(soup40)
    items = mainaddon.compile_playable_podcast40(playable_podcast40)
    return items
@plugin.route('/episodes41/')
def  episodes41():
    soup41 = mainaddon.get_soup41(URL41)
    playable_podcast41 = mainaddon.get_playable_podcast41(soup41)
    items = mainaddon.compile_playable_podcast41(playable_podcast41)
    return items
@plugin.route('/episodes42/')
def  episodes42():
    soup42 = mainaddon.get_soup42(URL42)
    playable_podcast42 = mainaddon.get_playable_podcast42(soup42)
    items = mainaddon.compile_playable_podcast42(playable_podcast42)
    return items
@plugin.route('/episodes43/')
def  episodes43():
    soup43 = mainaddon.get_soup43(URL43)
    playable_podcast43 = mainaddon.get_playable_podcast43(soup43)
    items = mainaddon.compile_playable_podcast43(playable_podcast43)
    return items
@plugin.route('/episodes44/')
def  episodes44():
    soup44 = mainaddon.get_soup44(URL44)
    playable_podcast44 = mainaddon.get_playable_podcast44(soup44)
    items = mainaddon.compile_playable_podcast44(playable_podcast44)
    return items
@plugin.route('/episodes45/')
def  episodes45():
    soup45 = mainaddon.get_soup45(URL45)
    playable_podcast45 = mainaddon.get_playable_podcast45(soup45)
    items = mainaddon.compile_playable_podcast45(playable_podcast45)
    return items

if __name__ == '__main__':
    plugin.run()
