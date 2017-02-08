# -*-encoding=utf-8 -*-

import re
import os,sys
LOG_PATH_RE1 = re.compile('(/.*/.*\.log)')
LOG_PATH_RE2 = re.compile('(../.*/.*\.log)')
MLOG = '/opt/MLog/'

def FristERRORlog(path='/opt/UExpt/msgU'):
    result = {}
    doc = open(path).read()
    times = 0
    for line in doc:
        if line.find('.log')>-1:
            times+=1
            result[str(times)]=line
    return result

def findLog(string):
    findString =  'find /opt/ -name "%s" '
    for index in string.split('..'):
        findString = findString + '| grep "%s"'%index
    findString = findString%string.split('/')[-1]
    print findString
    std = os.popen(findString).read()
    getLogPath(std)

def just(kwg):
    logPath, string = kwg
    if os.path.isfile(logPath):
        return logPath
    else:
        return findLog(logPath)
        # logPath = LOG_PATH_RE2.findall(string)
        # if len(logPath) == 0:
        #     return False
        # else:
        #     print logPath
        #     if os.path.isfile(logPath):
        #         return logPath
        #     else:
        #         return findLog(logPath)

def getLogPath(string):
    logPath = LOG_PATH_RE1.findall(string)
    if len(logPath) == 0:
        return False
    else:
        string=string+"++="
        stringList = (string*len(logPath)).split('++=')
        return map(just,tuple(zip(logPath,stringList[:-1])))


def copLog(path):
    if os.path.isfile(path):
        std = os.popen('cp %s %s'%(path,MLOG+'%s'%path.split('/')[-1])).read()

def writeResult(string):
    doc = open(MLOG+'result.txt')
    doc.write(string)
    doc.close()

def Analyze(string='/opt/UExpt/msgU',result=[]):
    doc = open(string)
    pathLog = getLogPath(doc.read())
    doc.close()
    for index in pathLog:
        copLog(index)
        writeResult('cp log' + str(Analyze(index)))
    return pathLog

def AnalyzeMain():
    for key, value in FristERRORlog().iteritems():
        writeResult(key+'/n/t'+value)
        writeResult('cp log'+str(Analyze(value)))




def zips():
    pass

if __name__ == '__main__':
    Analyze()
    # zips()
