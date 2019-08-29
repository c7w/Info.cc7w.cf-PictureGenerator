import utils.getMcbbsScore as score

from flask import Flask, Response, escape,request,render_template
from requests_html import HTMLSession

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/get-mcbbs-score',methods=['GET', 'POST'])
@app.route('/get-mcbbs-score/<int:uid>')
def get_mcbbs_score(uid=None):
    #快捷方式 直接通过UID直接获取
    if uid:
        if uid >= 1:
            #Do Something Here
            profile = score.getScoreFromUid(uid)
            return render_template('./get-mcbbs-score/score.html',list=profile)
        else:
            return render_template('./get-mcbbs-score/error.html',list = ['uid',uid])
    
    #处理表单 获取数据
    if request.method=="POST":
        source = request.form.get('source')
        val = request.form.get('val')
        
        if val == '':
            return render_template('./get-mcbbs-score/error.html',list = [source,val])
        if source == 'uid':
            try:
                val = int(val)
            except:
                return render_template('./get-mcbbs-score/error.html',list = [source,val])
            profile = score.getScoreFromUid(val)
        else:
            profile = score.getScoreFromUsername(val)
            
        #Do Something Here
        return render_template('./get-mcbbs-score/score.html',list=profile)
    
    #尝试处理 get 请求
    getUid = request.args.get('uid')
    getName = request.args.get('username')
    if getUid:
        try:
            uid = int(getUid)
        except:
            return render_template('./get-mcbbs-score/error.html',list = [source,getUid])
        profile = score.getScoreFromUid(getUid)
        return render_template('./get-mcbbs-score/score.html',list=profile)
    if getName:
        profile = score.getScoreFromUsername(getName)
        return render_template('./get-mcbbs-score/score.html',list=profile)
    
    #没有输入账号信息
    #进入提醒页面 提醒输入数据
    return render_template('./get-mcbbs-score/index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    list = {
        1: name,
        2: 2333
            }
    return render_template('index.html' , list = list)

if __name__ == '__main__':
    app.run()