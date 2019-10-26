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

###########################################################
# 图片: map
# 描述: 进度条
# 起始点 (50,50) 终止点 (450,80)
# 进度条颜色 (255,255,255) 进度条边框颜色 (21,100,43)
###########################################################
# 参数: 
#[i] - 初始值
#<v> - 当前值
#<f> - 最终值
#[mode]:
#   [normal] - 正常模式
#   time - 时间间隔 输入时间戳
#   bbs - BBS积分
#[c] - 进度条颜色（空） [(235,205,226,255)]
#[cc] - 进度条颜色（填满） [(143,240,152,255)]
#[font] - 字体 (字体标号,hm字体大小,信息字体大小,百分比大小) [('A',20,18,20)]
#[im] - 初始值信息
#[vm] - 当前值信息
#[fm] - 最终值信息
#[hm] - 标题 ['Unknown']
#[percent] - 是否展示百分比 [(True,2)]
###########################################################
@app.route('/map')
def map():
    def getParam(param,default):
        return request.args.get(param,default)
    try:
        i = float(request.args.get('i'))
        v = float(request.args.get('v'))
        f = float(request.args.get('f'))
    except:
        return index()
    mode = getParam('mode','normal')
    c = tuple(eval(getParam('c','(235,205,226,255)')))
    cc = tuple(eval(getParam('cc','(143,240,152,255)')))
    font = tuple(eval(getParam('font','("A",20,18,20)')))
    im = getParam('im','')
    vm = getParam('vm','')
    fm = getParam('fm','')
    hm = getParam('hm','Unknown')
    percent = tuple(eval(getParam('percent','(True,2)')))
    return pic.returnImage(pic.map(i,v,f,mode,c,cc,font,im,vm,fm,hm,percent))
    
if __name__ == '__main__':
    app.run()