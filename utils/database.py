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
        return 
    except NameError:
        dic = {}
        print("---------------------------------")
        print("数据库初始化完成")
        print("---------------------------------")
        return

def setTable(name,df):
    dic[name] = df