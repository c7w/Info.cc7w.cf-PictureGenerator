from requests_html import HTMLSession
import re
import datetime

def getScoreFromUsername(username):
    url = 'https://www.mcbbs.net/home.php?mod=space&username='+ str(username)
    profile = getProfile(url)
    return profile

def getScoreFromUid(uid):
    url = 'https://www.mcbbs.net/home.php?mod=space&uid=' + str(uid)
    profile = getProfile(url)
    return profile

def getProfile(url):
    session = HTMLSession()
    rawData = session.get(url).html.html
    uid = match('<span class="xw0">\(UID: (.*)\)</span>',rawData,1)
    username = match('<meta name="keywords" content="(.*)的个人资料" />',rawData,1)
    usergroup = match('<li>(.*)用户组(.*)target="_blank">(.*)</a></span>  </li>',rawData,3)
    reply = match('<a href="(.*)" target="_blank">好友数 (.*)</a>\n<span class="pipe">\|</span><a href="(.*)" target="_blank">回帖数 (.*)</a>\n<span class="pipe">\|</span>\n<a href="(.*)" target="_blank">主题数 (.*)</a>',rawData,4)
    topic = match('<a href="(.*)" target="_blank">好友数 (.*)</a>\n<span class="pipe">\|</span><a href="(.*)" target="_blank">回帖数 (.*)</a>\n<span class="pipe">\|</span>\n<a href="(.*)" target="_blank">主题数 (.*)</a>',rawData,6)
    onlineTime = match('<li><em>在线时间</em>(.*) 小时</li>',rawData,1)
    regTime = match('<li><em>注册时间</em>(.*)</li>\n<li><em>最后访问</em>(.*)</li>',rawData,1)
    lastLoginTime = match('<li><em>注册时间</em>(.*)</li>\n<li><em>最后访问</em>(.*)</li>',rawData,2)
    score=getScore(rawData)
    medalCount = countMedal(rawData)
    timeutc8 = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    time = timeutc8.strftime("%Y-%m-%d %H:%M:%S")
    profile = {
        'uid': uid,
        'username': username,
        'usergroup': usergroup,
        'topic': topic,
        'reply': reply,
        'onlineTime': onlineTime,
        'regTime': regTime,
        'lastSeenTime': lastLoginTime,
        'score':score,
        'medal':medalCount,
        'time':time
    }
    return profile
    
def match(a,b,n):
    try:
        get = re.search(a, b,re.M).group(n)
    except:
        get = '-'
    return get

def getScore(rawText):
    score=[]
    try:
        get = re.search('<li><em>积分</em>(.*)</li><li><em>人气</em>(.*) 点</li>\n<li><em>金粒</em>(.*) 粒</li>\n<li><em>金锭</em>(.*) 块</li>\n<li><em>绿宝石</em>(.*) 颗</li>\n<li><em>下界之星</em>(.*) 枚</li>\n<li><em>贡献</em>(.*) 点</li>\n<li><em>爱心</em>(.*) 心</li>\n<li><em>钻石</em>(.*) 颗</li>\n',rawText,re.M)
        for i in range(1,10):
            score.append(get.group(i))
    except:
        score = ['-','-','-','-','-','-','-','-','-',]
    return score
    
def countMedal(rawData):
    get = re.compile('<div id="md_(.*)_menu" class="tip tip_4" style="display: none;">').findall(rawData)
    medalCount = len(get)
    return medalCount