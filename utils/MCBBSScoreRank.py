import utils.getMcbbsScore as getMcbbsScore
import utils.database as database

def getProfile(n):
    profile = getMcbbsScore.getScoreFromUid(n)
    return profile

def delline(n):
    sql = 'DELETE FROM score WHERE uid='+str(n)+';'
    database.execute(sql)

def addline(profile):
    value = ''
    value=addlineProcess(value,profile.get('time'),isText=True)
    value=addlineProcess(value,profile.get('uid'))
    value=addlineProcess(value,profile.get('username'),isText=True)
    value=addlineProcess(value,profile.get('usergroup'),isText=True)
    value=addlineProcess(value,profile.get('topic'))
    value=addlineProcess(value,profile.get('reply'))
    value=addlineProcess(value,profile.get('onlineTime'),isText=True)
    value=addlineProcess(value,profile.get('regTime'),isText=True)
    value=addlineProcess(value,profile.get('lastSeenTime'),isText=True)
    value=addlineProcess(value,profile.get('medal'))
    value=addlineProcess(value,profile.get('score')[1])
    value=addlineProcess(value,profile.get('score')[2])
    value=addlineProcess(value,profile.get('score')[3])
    value=addlineProcess(value,profile.get('score')[4])
    value=addlineProcess(value,profile.get('score')[5])
    value=addlineProcess(value,profile.get('score')[6])
    value=addlineProcess(value,profile.get('score')[7])
    value=addlineProcess(value,profile.get('score')[8])
    value=addlineProcess(value,profile.get('score')[0],isLast=True)
    sql = 'INSERT INTO score ( time,uid,username,usergroup,topic,reply,onlineTime,regTime,lastSeenTime,medal,rq,jl,jd,lbs,xjzx,gx,ax,zs,score ) VALUES ( '+ value +' );'
    database.execute(sql)

def addlineProcess(value,currentVal,isText=None,isLast=None):
    if isText == True:
        value = str(value) + "'" + str(currentVal) + "'"
    else:
        value = str(value) + str(currentVal)
    if isLast:
        return value
    else:
        value = value + ","
        return value

def createTable():
    sql1 = """CREATE TABLE if not exists score(
    `time` VARCHAR(40) NOT NULL NOT NULL,
    `uid` INT NOT NULL,
    `username` VARCHAR(40) NOT NULL,
    `usergroup` VARCHAR(40) NOT NULL,
    `topic` INT NOT NULL,
    `reply` INT NOT NULL,
    `onlineTime` VARCHAR(40) NOT NULL,
    `regTime` VARCHAR(40) NOT NULL NOT NULL,
    `lastSeenTime` VARCHAR(40) NOT NULL NOT NULL,
    `medal` INT NOT NULL,
    `rq` INT NOT NULL,
    `jl` INT NOT NULL,
    `jd` INT NOT NULL,
    `lbs` INT NOT NULL,
    `xjzx` INT NOT NULL,
    `gx` INT NOT NULL,
    `ax` INT NOT NULL,
    `zs` INT NOT NULL,
    `score` INT NOT NULL,
    PRIMARY KEY ( `uid` )
    );"""
    sql2 = """CREATE TABLE IF NOT EXISTS user_list(
   `ID` INT UNSIGNED AUTO_INCREMENT,
   `UID` INT NOT NULL,
   `UserName` VARCHAR(40) NOT NULL,
    PRIMARY KEY ( `ID` )
    );"""
    database.execute(sql1)
    database.execute(sql2)

def updateProfile(uidlist):
    for uid in uidlist:
        profile = getProfile(uid)
        delline(uid)
        addline(profile)

def get():
    result = database.get()
    return result
    
def startJob(app):
    createTable()
    updateProfile([2722,679293,59136,3038,284709,3467,136103,1286708,54491,564032,165947,160123,62102,265839,910117,41816,1770442,27076,1073223,265600])
    result = app.apscheduler.add_job(func=updateProfile,args=[[2722,679293,59136,3038,284709,3467,136103,1286708,54491,564032,165947,160123,62102,265839,910117,41816,1770442,27076,1073223,265600]], id='1', trigger='interval', seconds=7200)
    print(result)