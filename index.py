import utils.getMcbbsScore as score
import utils.pic as pic


from PIL import Image
from datetime import datetime,timedelta
from flask import Flask, Response,escape,request,render_template,send_file
from requests_html import HTMLSession

app = Flask(__name__)

##### 路由设置 #####
@app.route('/')
def index():
    return render_template('index.html')

##################################################
# 图片: map
# 描述: 进度条
# 参数: 
#####初始值: start
#####当前值: now
#####目标值: end
#####进度条颜色: colorBar  默认值 None  示例输入(0,0,0,255)
#####完成进度条颜色: colorComplete  默认值 (0,0,0,255)  示例输入(0,0,0,255)
#####进度条介绍: description  默认值 ('Unknown','A',20)  示例输入('介绍','A',12)
#####初始值介绍: startMessage  默认值 ('','A',20)
#####当前值介绍: nowMessage  默认值 ('','A',20)
#####目标值介绍: endMessage  默认值 ('','A',20)
#####是否展示百分比: showPercentage  默认值(True,1,'A',20)
# 起始点 (50,50) 终止点 (450,80)
# 进度条颜色 (255,255,255) 进度条边框颜色 (21,100,43)
@app.route('/map')
def map():
    def getParam(param,default):
        return request.args.get(param) or default
    start = float(getParam('start',0))
    now = float(getParam('now',50))
    end = float(getParam('end',100))
    colorBar = tuple(eval(getParam('colorBar','(235,205,226,255)')))
    colorComplete = tuple(eval(getParam('colorComplete','(143,240,152,255)')))
    startMessage = tuple(eval(getParam('startMessage','("","A",20)')))
    nowMessage = tuple(eval(getParam('nowMessage','("","A",20)')))
    endMessage = tuple(eval(getParam('endMessage','("","A",20)')))
    description = tuple(eval(getParam('description','("Unknown","A",20)')))
    showPercentage = tuple(eval(getParam('showPercentage','(True,1,"A",20)')))

    if now == 564032:
        now = int(score.getScoreFromUid(564032).get('score')[0])
        startMessage = eval(getParam('s','["","A",20]'))
        nowMessage = eval(getParam('n','["","A",20]'))
        endMessage = eval(getParam('e','["","A",20]'))
        nowMessage[0] = "当前积分: "+str(now)
        startMessage = tuple(startMessage)
        nowMessage = tuple(nowMessage)
        endMessage = tuple(endMessage)
    return pic.returnImage(pic.map(start,now,end,colorBar=colorBar,colorComplete=colorComplete,startMessage=startMessage,nowMessage=nowMessage,endMessage=endMessage,description=description,showPercentage=showPercentage))
    
if __name__ == '__main__':
    app.run()