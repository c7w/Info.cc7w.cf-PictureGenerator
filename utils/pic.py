import utils.getMcbbsScore as score

import time
import base64
from io import BytesIO
from flask import Flask, Response,escape,request,render_template,send_file
from PIL import Image,ImageFont,ImageDraw

def loadImage(imgName):
    f = open('./templates/assets/'+imgName+'.txt')
    byte_data = base64.b64decode(f.read().rstrip('\n'))
    f.close()
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img

def returnImage(img):
    img_io = BytesIO()
    img.save(img_io, 'png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', cache_timeout=0)

def getFont(font,size):
    try:
        font = ImageFont.truetype('./templates/font/font'+font+'.ttf',size)
        return font
    except:
        font = ImageFont.truetype('./templates/font/fontA.ttf',size)
        return font

def writeText(img,text,pos,align='left',font='A',size=12,color=(0,0,0)):
    if text == '':
        return
    font = getFont(font,size)
    textSize = font.getsize(text)
    if align == 'right':
        pos2 = (pos[0]-textSize[0],pos[1])
    elif align == 'center':
        pos2 = (int(pos[0]-textSize[0]/2),pos[1])
    else:
        pos2 = pos

    imgDraw = ImageDraw.Draw(img)
    imgDraw.text(pos2,text,fill=color,font=font)

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
#[font] - 字体 (字体标号,hm字体大小,信息字体大小,百分比大小) [('A',20,18,15)]
#[im] - 初始值信息
#[vm] - 当前值信息
#[fm] - 最终值信息
#[hm] - 标题 ['Unknown']
#[percent] - 是否展示百分比/保留小数位数 [(True,2)]
###########################################################
def map(i,v,f,mode,c,cc,font,im,vm,fm,hm,percent):
    img = loadImage('map')
    barWidth = 400
    barHeight = 30
    
    #处理模式
    if mode == 'bbs':
        v = int(score.getScoreFromUid(v).get('score')[0])
        vm = "当前积分: "+str(v)
        
    if mode == 'time':
        v = time.time()

    #绘制空进度条
    for x in range(50,51+barWidth):
        for y in range(50,51+barHeight):
            currentPixel = img.getpixel((x,y))
            if (currentPixel[2] >=180):
                img.putpixel((x,y),c)

    #percentage 百分比
    #pixel 应绘制的像素值
    try:
        delta = v - i
        duration = f - i
        percentage = delta / duration
        if percentage > 1:
            percentage = 1
    except:
            percentage = 1
            cc = (0,0,0,255)
            hm = '！！！计算错误！！！'
        
    pixelDelta = int(percentage * 396)
    pixelFrom = 50
    pixelTo = 51 + pixelDelta
    
    #填充进度条
    for x in range(50,pixelTo):
        for y in range(50,51+barHeight):
            currentPixel = img.getpixel((x,y))
            if (currentPixel == c):
                img.putpixel((x,y),cc)
    
    #添加文字
    writeText(img,hm,(250,20),align='center',font=font[0],size=font[1])
    writeText(img,im,(50,90),align='left',font=font[0],size=font[2])
    writeText(img,vm,(250,90),align='center',font=font[0],size=font[2])
    writeText(img,fm,(450,90),align='right',font=font[0],size=font[2])
    if percent[0]:
        pm = str(round(percentage*100,percent[1])) + '%'
    writeText(img,pm,(250,55),align='center',font=font[0],size=font[3])
    return img