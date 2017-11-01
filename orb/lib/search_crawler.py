

def is_search_crawler(user_agent):
    spiders = {'Googlebot',
               'Yammybot',
               'Openbot',
               'Yahoo',
               'Slurp',
               'msnbot',
               'ia_archiver',
               'Lycos',
               'Scooter',
               'AltaVista',
               'Teoma',
               'Gigabot',
               'Googlebot-Mobile',
               'MJ12bot',
               'bingbot',
               'LinkedInBot',
               'baiduspider',
               'facebookexternalhit',
               'spider',
               'domainreanimator.com',
               'seznambot',
               'ahrefsbot',
               'spbot',
               'wbsearchbot',
               'dotbot',
               'betabot',
               'Python-urllib',
               'Twitterbot',
               'YandexBot',
               'Exabot',
               'rogerbot',
               'bitlybot',
               'ZoomBot',
               'LinqiaCrawler',
               'Fyrebot',
               'Fountain bot',
               'YandexImages',
               'RSSingBot',
               'SBL-BOT',
               'wonderbot',
               'LinqiaScrapeBot',
               'IstellaBot',
               'Plukkie',
               'TurnitinBot',
               'BuzzSumo',
               'Clickagy',
               'alsRobot2',
               'YodaoBot',
               'zitebot',
               'EveryoneSocialBot',
               'TweetmemeBot',
               'Applebot',
               'Kraken',
               'PaperLiBot',
               'linkdexbot',
               'Wotbox',
               'Nutch',
               'XoviBot',
               'LivelapBot',
               'ContextAd',
               'ShowyouBot',
               'Climatebot',
               'Mail.RU_Bot',
               'SEOkicks-Robot',
               'uMBot-LN',
               'SMTBot',
               'Slackbot',
               'Findxbot',
               'SafeDNSBot',
               'BLEXBot',
               'MojeekBot',
               'YandexMobileBot',
               'SemrushBot',
               'Girafabot',
               'Laserlikebot',
               'SocialRankIOBot',
               'Buzzbot',
               'K7MLWCBot',
               'TinEye-bot',
               'archive.org_bot',
               'Veoozbot', 
               'LinkosmosBot',
               'Cliqzbot',
               'Pinterest',
               'mbot',
               'Mediatoolkitbot',
               'trendictionbot',
               'CCBot',
               'DeuSu',  
               'ArchiveBot',  
               'Go-http-client',
               'DJEcoBot',
               'Yeti',
               'ExtLinksBot',
               'OpenHoseBot',
               }
    for s in spiders:
        if s.lower() in user_agent.lower():
            return True
    return False
