import pandas as pd
import os

def createTable(name,columns):
    global dic
    dic[name] = pd.DataFrame(columns=columns)
    print("---------------------------------")
    print("数据表 " +name+" 创建完成")
    print("---------------------------------")

def getTable(name):
    global dic
    try:
        result = dic[name]
        return result
    except KeyError:
        print("---------------------------------")
        print("数据表 " +name+" 不存在")
        print("---------------------------------")
        return False
    except NameError:
        dic = {}
        print("---------------------------------")
        print("数据库初始化完成")
        print("---------------------------------")
        return

def setConf(conf,value):
	global dic
	dic[conf] = value

def getConf(conf,default=None):
	global dic
	value = dic.get(conf)
	if value:
		return value
	else:
		return default

def setTable(name,df):
	global dic
    dic[name] = df