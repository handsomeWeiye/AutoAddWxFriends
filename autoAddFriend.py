
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import pandas as pd
import time

#首先通过pandas读取excel表中的数据

excel_dir =  r"C:\Users\云云\Desktop\provider.xlsx"
col_list = [0,11,12,15]

def log(str):
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
    print(str_time)
    with open('log.txt','a+') as f:
        logInfo = str_time +  "   " + str
        print(logInfo)
        f.write(logInfo)
    


def getInfoList(excel_dir,col_list):

    provider_file = pd.read_excel(excel_dir,usecols=col_list)
    provider_list  = provider_file.values
    print("目前的读取到的数据是")
    print( provider_file.head())
    log('获取到excel数据，转化为了list')

    return provider_list

data =  getInfoList(excel_dir,col_list)

apply = "{}先生。您好，我是成都致悦果蔬商贸有限公司的采购杜经理，我是从1688上面看到能的信息的，您方便通过一下吗？我们主要是寻找好的货源".format(data)

# print(provider.head())




