#需要导入的初始化包
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.core.api import *
import pandas as pd
import time


#程序准备的全局变量，包括文件路径，申请模板，和导入的路径的列号
excel_dir =  r"C:\Users\云云\Desktop\provider.xlsx"
apply = "{}先生。您好，我是成都致悦果蔬商贸有限公司的采购杜经理，我是从1688上面看到能的信息的，您方便通过一下吗？我们主要是寻找好的供应商货源"
col_list = [0,11,12,15]

def log(str):
    #日志函数
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
    print(str_time)
    with open('log.txt','a+') as f:
        logInfo = str_time +  "   " + str
        print(logInfo)
        f.write(logInfo +"\n")
    


def getInfoList(excel_dir,col_list):
    #数据函数，把excel列表中的数据转化为了一个列表
    provider_file = pd.read_excel(excel_dir,usecols=col_list)
    provider_list  = provider_file.values
    print("目前的读取到的数据是")
    print( provider_file.head())
    log('获取到excel数据，转化为了list'+"\n")

    return provider_list



def addFrined(data):
    #遍历循环列表，添加微信好友
    for item in data:
        applyFormat = apply.format(item[3][0])
        name = item[3]
        companyName = item[1]
        phoneNum = item[2]
        description  = item[0]
        remarkName = companyName + " " +name + str(phoneNum)
        print(applyFormat,remarkName,phoneNum,description)
        try:
            situmatedAdd(applyFormat,remarkName,phoneNum,description)
        except:
            log(str(phoneNum) + " " +"发生了异常错误"+"\n")
            sleep(2)
            continue


def situmatedAdd(applyFormat,remarkName,phoneNum,description):
    #使用poco,检测元素，点击，输入，返回
    if(not poco("com.tencent.mm:id/dlc").exists()):
        log(str(phoneNum)+' '+"添加已经频繁了"+"\n")
        sleep(2)
        keyevent("4")
        sleep(50)
    else:
        poco("com.tencent.mm:id/dlc").click()
        sleep(2)
        poco("com.tencent.mm:id/m7").set_text(phoneNum)
        sleep(2)
        poco("com.tencent.mm:id/o_").click()
        sleep(2)
        if(poco("com.tencent.mm:id/c4s").exists()):
            log(str(phoneNum)+' '+"该号码没有被注册为微信号或者添加已经频繁了"+"\n")
            sleep(2)
            keyevent("4")
        else:
            if(poco("com.tencent.mm:id/dd").exists()):
                log(str(phoneNum)+' '+"该号码已经被添加为好友"+"\n")
                sleep(2)
                keyevent("4")     
                sleep(2)
                keyevent("4") 
                sleep(2)
            else:
                poco(text="设置备注和标签").click()
                sleep(2)
                poco("com.tencent.mm:id/b_q").set_text(remarkName)
                poco("com.tencent.mm:id/ba1").set_text(description)
                sleep(2)
                poco("android.support.v7.widget.LinearLayoutCompat").click()
                sleep(2)
                poco("com.tencent.mm:id/d9").click()
                sleep(2)
                if(poco("com.tencent.mm:id/fbi").exists()):
                    log(str(phoneNum)+' '+"该号码不需要申请，也可以自动添加" +"\n")
                    sleep(2)
                    keyevent("4")     
                    sleep(2)
                    keyevent("4") 
                    sleep(2)
                else:
                    sleep(2)
                    poco("com.tencent.mm:id/ejg").set_text(applyFormat)
                    sleep(2)
                    poco("com.tencent.mm:id/ln").click()
                    sleep(2)
                    keyevent("4")            
                    sleep(2)
                    keyevent("4")
                    sleep(60)



data =  getInfoList(excel_dir,col_list)
addFrined(data)




