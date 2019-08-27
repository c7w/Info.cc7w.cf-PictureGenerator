#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from requests_html import HTMLSession
import re
# Create your views here.
def index(request):
    m = getSomething(564032)
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
    score[4] = re.match('(.*)\(UID: (.*)\)', score[1].replace(u'\xa0 ','')).group(2)
    score[1] = re.match('(.*)\(UID: (.*)\)', score[1].replace(u'\xa0 ','')).group(1)
    score[2] = re.match('主题数 (.*)', score[2]).group(1)
    score[3] = re.match('回帖数 (.*)', score[3]).group(1)
    score[5] = re.match('积分(.*)', score[5]).group(1)
    score[6] = re.match('人气(.*) 点', score[6]).group(1)
    score[7] = re.match('金粒(.*) 粒', score[7]).group(1)
    score[8] = re.match('金锭(.*) 块', score[8]).group(1)
    score[9] = re.match('绿宝石(.*) 颗', score[9]).group(1)
    score[10] = re.match('下界之星(.*) 枚', score[10]).group(1)
    score[11] = re.match('贡献(.*) 点', score[11]).group(1)
    score[12] = re.match('爱心(.*) 心', score[12]).group(1)
    score[13] = re.match('钻石(.*) 颗', score[13]).group(1)
    return score
    
#m = getSomething(564032)
#print(m)