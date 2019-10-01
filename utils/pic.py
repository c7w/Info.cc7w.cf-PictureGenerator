import base64
from io import BytesIO
from flask import Flask, Response,escape,request,render_template,send_file
from PIL import Image,ImageFont,ImageDraw

def returnImage(img):
    img_io = BytesIO()
    img.save(img_io, 'png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', cache_timeout=0)

def getFont(font,size):
    font = ImageFont.truetype('./templates/font/font'+font+'.ttf',size)
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
def map(start,now,end,colorBar=None,colorComplete=(0,0,0,255),description=('Unknown','A',20),startMessage=('','A',20),nowMessage=('','A',20),endMessage=('','A',20),showPercentage=(True,1,'A',20)):
    img = Image.open('./templates/assets/map.png')
    barWidth = 400
    barHeight = 30
    
    if colorBar:
        for x in range(50,51+barWidth):
            for y in range(50,51+barHeight):
                currentPixel = img.getpixel((x,y))
                if (currentPixel[2] >=180):
                    img.putpixel((x,y),colorBar)


    #percentage 百分比
    #pixel 应绘制的像素值
    delta = now - start
    duration = end - start
    percentage = delta / duration
    
    if percentage>1:
        percentage=1
    
    pixelDelta = int(percentage * 396)
    
    pixelFrom = 50
    pixelTo = 51 + pixelDelta
    
    #绘制进度条
    if colorBar:
        for x in range(50,pixelTo):
            for y in range(50,51+barHeight):
                currentPixel = img.getpixel((x,y))
                if (currentPixel == colorBar):
                    img.putpixel((x,y),colorComplete)
    else:
        for x in range(50,pixelTo):
            for y in range(50,51+barHeight):
                currentPixel = img.getpixel((x,y))
                if (currentPixel[2] >=180):    
                    img.putpixel((x,y),colorComplete)
    
    #添加文字
    writeText(img,description[0],(250,20),align='center',font=description[1],size=description[2])
    writeText(img,startMessage[0],(50,90),align='left',font=startMessage[1],size=startMessage[2])
    writeText(img,nowMessage[0],(250,90),align='center',font=nowMessage[1],size=nowMessage[2])
    writeText(img,endMessage[0],(450,90),align='right',font=endMessage[1],size=endMessage[2])
    if showPercentage[0]:
        percentageMessage = str(round(percentage*100,2)) + '%'
    writeText(img,percentageMessage,(250,55),align='center',font=showPercentage[2],size=showPercentage[3])

    return img