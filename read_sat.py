###

import pandas as pd
import numpy as np


##判断正负（上下行）
def juge_rd(a):
    if a>=0:
        return 1
    else:
        return 0


##读取txt文件
#sat_Num 卫星总数，orbit_Num 轨道总数，start_O 需求初始轨道序号，end_O 需求终止轨道,f_l文件储存位置的母文件夹

def read_txt(sat_Num,orbit_Num,start_O,end_O,f_l):
    sat_per_orbit=int(sat_Num/orbit_Num)
    latvalforallmatrix=[]
    latdirforallmatrix=[]

    for i in range(start_O,end_O+1):#轨道序号
        for j in range(1,sat_per_orbit+1):#轨道星序号
            file_name_tempt="o"+str(i)+"s"+str(j)+"timeLLA.txt"#文件名
            #读取文件
            path=f_l+file_name_tempt
            file_tempt=np.loadtxt(path,skiprows = 7)
            latvalforallmatrix_tempt = []
            latdirforallmatrix_tempt = []
            for t in range(0, len(file_tempt)):
                latvalforallmatrix_tempt.append(file_tempt[t, 1])
                latdirforallmatrix_tempt.append(juge_rd(file_tempt[t, 4]))

            latvalforallmatrix.append(latvalforallmatrix_tempt)
            latdirforallmatrix.append(latdirforallmatrix_tempt)

    print(latdirforallmatrix[0])
    return latvalforallmatrix,latdirforallmatrix



read_txt(120,12,1,2,'D:\\work\\py_project\\try_120\\极轨_120+5\\')