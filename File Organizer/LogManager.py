import os
import datetime


f = None

def OpenLog():
    folder = "log"
    if not Check_file_is_exist(folder):
        os.mkdir(folder)
    
    OperationNumber = 0
    now = datetime.datetime.now()
    Date = str(now.day) + '_' + str(now.month) + '_' + str(now.year)
    FileName = 'log_' + Date + "_" + str(OperationNumber) + '.txt'
    while Check_file_is_exist(os.path.join(folder, FileName)):
        OperationNumber += 1
        FileName = 'log_' + Date + "_" + str(OperationNumber) + '.txt'
    global f
    f = open(os.path.join(folder, FileName), 'a', encoding="utf-8")


def write(msg):
    global f
    now = datetime.datetime.now()
    TimeText = "[" + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + "]"
    f.write( TimeText + str(msg) + "\n")

def close():
    global f
    f.close()

def Check_file_is_exist(name):
    if os.path.exists(name):
        return True
    else:
        return False