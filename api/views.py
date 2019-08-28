#coding=utf-8
from requests_html import HTMLSession
import re

from http.server import BaseHTTPRequestHandler

# Create your views here.
def index(request):
    uid = request.GET.get('uid',1)
    score = getSomething(int(uid))
    #return HttpResponse(m)
    return render(request,'index.html',{'score':score})
    
def getSomething(n):
    session = HTMLSession()
    url = 'https://www.mcbbs.net/home.php?mod=space&uid=' + str(n)
    print(n)
    m = session.get(url)
    score = []
    
    selname = '#ct > div > div.bm.bw0 > div > div.bm_c.u_profile > div:nth-child(1) > h2'
    seltopic = '#ct > div > div.bm.bw0 > div > div.bm_c.u_profile > div:nth-child(1) > ul.cl.bbda.pbm.mbm > li > a:nth-child(6)'
    selcomment = '#ct > div > div.bm.bw0 > div > div.bm_c.u_profile > div:nth-child(1) > ul.cl.bbda.pbm.mbm > li > a:nth-child(4)'
    seltime = '#pbbs > li:nth-child(1)'
    selscore = '#psts > ul > li:nth-child(2)'
    selrq = '#psts > ul > li:nth-child(3)'
    seljl = '#psts > ul > li:nth-child(4)'
    seljd = '#psts > ul > li:nth-child(5)'
    sellbs = '#psts > ul > li:nth-child(6)'
    selxjzx = '#psts > ul > li:nth-child(7)'
    selgx = '#psts > ul > li:nth-child(8)'
    selax = '#psts > ul > li:nth-child(9)'
    selzs = '#psts > ul > li:nth-child(10)'
    
    D = {"1":selname,
    "2":seltopic,
    "3":selcomment,
    "5":selscore,
    "6":selrq,
    "7":seljl,
    "8":seljd,
    "9":sellbs,
    "10":selxjzx,
    "11":selgx,
    "12":selax,
    "13":selzs}
    score = [0]
    for f in range(1,14):
        try:
            t = m.html.find(D[str(f)])
            score.append(t[0].text)
        except:
            score.append('')
            # score[f] = t[0].text
    print(score[1].replace(u'\xa0 ','')) 
    score[4] = match('(.*)\(UID: (.*)\)', score[1].replace(u'\xa0 ',''),2)
    score[1] = match('(.*)\(UID: (.*)\)', score[1].replace(u'\xa0 ',''),1)
    score[2] = match('主题数 (.*)', score[2],1)
    score[3] = match('回帖数 (.*)', score[3],1)
    score[5] = match('积分(.*)', score[5],1)
    score[6] = match('人气(.*) 点', score[6],1)
    score[7] = match('金粒(.*) 粒', score[7],1)
    score[8] = match('金锭(.*) 块', score[8],1)
    score[9] = match('绿宝石(.*) 颗', score[9],1)
    score[10] = match('下界之星(.*) 枚', score[10],1)
    score[11] = match('贡献(.*) 点', score[11],1)
    score[12] = match('爱心(.*) 心', score[12],1)
    score[13] = match('钻石(.*) 颗', score[13],1)
    try:
        score.append( int(score[7]) + int(score[8]) * 100 )
    except:
        score.append("-")
    return score
def match(a,b,n):
    try:
        get = re.match(a, b).group(n)
    except:
        get = '-'
    return get
#m = getSomething(564032)
#print(m)