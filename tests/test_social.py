from extract_social_media import matches_string  # , find_links_tree

"""
TODO POS:
http://mp.weixin.qq.com/s?__biz=MzA5NjM5MjU2OA==&mid=249883494&idx=1&sn=fe698c9e27082fe5520777245a752d9e&3rd=MzA3MDU4NTYzMw==&scene=6#rd

TODO NEG:
https://www.youtube.com/yt/copyright/
"""

LINK_SAMPLES = """
http://www.flickr.com/photos/lenovophotolibrary
http://www.weibo.com/elletw?sudaref=data.elle.com.tw
http://www.weibo.com/parentingcw
http://facebook.com/tinybuddha
http://www.facebook.com/3Ireland
http://www.facebook.com/LenovoUKandIreland
http://www.facebook.com/daft.ie
http://www.facebook.com/pages/Marc-and-Angel-Hack-Life-Practical-Tips-for-Productive-Living/60187856377
http://www.facebook.com/pages/SurveyMonkey/65225997627
http://www.facebook.com/pages/Vodafone-Ireland/39948747919?utm_campaign=vfcontactusfb&utm_medium=facebook&utm_source=onlineteamjd&utm_content=vfcontactusfb
http://www.facebook.com/positivelypositive/
http://www.facebook.com/thejournal.ie
https://fr-fr.facebook.com/Caisse.Epargne
https://fr-fr.facebook.com/SFR
https://flipboard.com/@techcrunch
http://instagram.com/lifehackorg?ref=footer-browse-instagram
http://instagram.com/newegg/
https://instagram.com/okcupid
https://instagram.com/pospositive/
https://instagram.com/snapdeal/?hl=en
http://pinterest.com/bange16/marc-and-angel/
http://pinterest.com/lifehack/?ref=footer-browse-pinterest
http://pinterest.com/mindbodygreen
http://pinterest.com/thinksimplenow/
http://www.pinterest.com/instructables
http://www.pinterest.com/thepositivepin/
https://pinterest.com/EmilySchuman
http://plus.google.com/107307393263977088342/about
https://plus.google.com/+Coursera
https://plus.google.com/+Dropbox/posts
https://plus.google.com/+P%C3%BAblico/posts
https://plus.google.com/+duolingo
https://plus.google.com/+snapdeal/posts
https://plus.google.com/100371967013117528205
https://plus.google.com/111984034088692092819?prsrc=3
https://plus.google.com/116623388763634190489
https://plus.google.com/117330593038325285345/posts
https://plus.google.com/u/0/+eventbrite/
https://plus.google.com/u/1/115964001953967461416?pageId=114804279025961350651&authuser=1
https://telegram.me/publico_es
http://twitter.com/#!/SurveyMonkey
http://twitter.com/ThreeIreland
http://twitter.com/VodafoneIreland?utm_campaign=vfcontactustw&utm_medium=twitter&utm_source=onlinejd&utm_content=vfcontactustw
http://twitter.com/thejournal_ie
http://www.twitter.com/MrjWells
http://www.twitter.com/tinybuddha
https://twitter.com/AskAIB
https://twitter.com/Independent_ie
https://twitter.com/XFINITY
https://twitter.com/irishmirror
https://twitter.com/lenovo_uki
https://twitter.com/lifehackorg/?ref=footer-browse-twitter
https://twitter.com/mindbodygreen
https://twitter.com/rte
https://www.twitter.com/Eventbrite
https://www.facebook.com/Atlassian
https://www.facebook.com/DoneDealIreland
https://www.facebook.com/ExploreRTE/
https://www.facebook.com/Independent.ie
https://www.facebook.com/TED
https://www.facebook.com/cupcakesandcashmere
https://www.facebook.com/eir
https://www.facebook.com/lifehackorg/?ref=footer-browse-facebook
https://www.facebook.com/monepositiveblog/
https://www.google.com/+Thechangeblog
https://www.instagram.com/imdb/
https://www.instagram.com/mindvalley
http://www.linkedin.com/company/362798
http://www.linkedin.com/company/aib/products/
http://www.linkedin.com/company/investopedia-ulc
http://www.linkedin.com/company/techcrunch
http://www.linkedin.com/in/mrjwells
https://www.linkedin.com/pub/whois-api/88/573/6b2
https://www.periscope.tv/le_Parisien
https://www.pinterest.com/snapdeal/
https://www.pinterest.com/tednews
https://www.pinterest.com/tinybuddha/pins/
https://www.snapchat.com/add/positivepresent
http://www.youtube.com/ThreeIreland
http://www.youtube.com/aib
http://www.youtube.com/positivelypositive1
http://www.youtube.com/user/instructablestv
http://www.youtube.com/user/mrjWells
http://www.youtube.com/user/positivelypresent
http://www.youtube.com/user/techcrunch
https://www.youtube.com/channel/UCVimQoXNCZuEnZRVAbuYMiw
https://www.youtube.com/channel/UCfHn_8-ehdem86fEvlFg-Gw
https://www.youtube.com/ted
https://www.youtube.com/user/DoneDealers
https://www.youtube.com/user/LifehackOrg/?ref=footer-browse-youtube
https://www.youtube.com/user/rte
https://www.youtube.com/user/xfinity?feature=results_main
https://soundcloud.com/uwebristol
https://feeds.feedburner.com/TroyHunt
https://vimeo.com/kadence
https://eg.linkedin.com/in/sayed-gharib-51b05133?trk=pub-pbmap
https://www.linkedin.com/company/dichter-&-neira-research-network?trk=fc_badge
https://dk.linkedin.com/in/carolinehorten
https://www.youtube.com/watch?v=hW9-jsAOBiA
https://plus.google.com/u/0/111494755084642562984/posts
http://www.slideshare.net/haystackinternational
https://www.facebook.com/pages/Robas-Research/357181737690559
http://www.facebook.com/pages/TNS-Global/55944527541
http://plus.google.com/108198427863983309725/
http://www.youtube.com/tnsglobal
http://feeds.feedburner.com/TnsGlobalPressReleases
https://www.facebook.com/AMR-Advanced-Market-Research-GmbH-152914324834256/timeline/
https://uk.linkedin.com/in/mihajlopopesku
http://www.vkontakte.ru/fom.media
http://www.slideshare.net/fom-media/
https://www.pinterest.com/globalvoxpopuli/
http://fb.co/OReilly
"""
# tumblr, whatsapp, blogspot, PENGYOU, RENREN, KAIXIN 001, TENCENT WEIBO
# SINA WEIBO, Baidu, WECHAT

SOCIAL_NEGATIVE = """
https://www.linkedin.com/salary/
https://www.linkedin.com/learning/me
https://about.twitter.com/company
https://www.youtube.com/t/terms
https://www.youtube.com/yt/policyandsafety/
https://www.facebook.com/privacy/explanation
https://www.facebook.com/directory/celebrities/
https://www.facebook.com/mobile/?ref=pf
https://www.facebook.com/directory/people/
https://www.facebook.com/places/
https://www.facebook.com/games/
https://www.facebook.com/careers/?ref=pf
https://about.pinterest.com/en
https://www.pinterest.com/_/_/about/
https://www.instagram.com/about/us/
https://www.instagram.com/developer/
https://www.instagram.com/legal/terms/
https://business.instagram.com/
https://www.snapchat.com/geofilters
https://www.snapchat.com/jobs
https://www.snapchat.com/terms
https://www.snapchat.com/beta/
https://business.snapchat.com/
https://www.flickr.com/cameras
https://www.flickr.com/about
https://www.flickr.com/explore/
https://www.flickr.com/jobs
https://www.xing.com/news/pages/f-a-z-wirtschaft-finanzen-90
"""


def split_lines(lines):
    return [x for x in lines.split('\n') if x.strip()]


def test_positives():
    for sample in split_lines(LINK_SAMPLES):
        assert matches_string(sample), (sample, )


def not_running_negatives():
    for sample in split_lines(SOCIAL_NEGATIVE):
        assert not matches_string(sample), (sample, )
