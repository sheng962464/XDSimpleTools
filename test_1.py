# -*- coding: utf-8 -*-

# coding: utf-8

# coding=utf-8

# -*- coding: cp936 -*-

# -*- coding: ascii -*-

import os
import re
import numpy


# 获取文件夹下所有文件的绝对路径
def FolderReading(FolderPath):
    List_Of_FilePath_In_Folder = []  # 用于存放文件夹中文件的绝对路径
    if os.path.isdir(FolderPath):
        List_Of_FileName_In_Folder = os.listdir(FolderPath)  # 读取文件夹中所有的文件名
        for File in List_Of_FileName_In_Folder:
            FilePath = os.path.join(FolderPath, File)  # 生成文件的绝对路径
            if os.path.isfile(FilePath):
                if File[0] == '.':  # 去除隐藏文件
                    pass
                else:
                    List_Of_FilePath_In_Folder.append(FilePath)
            else:
                List_Of_FilePath_In_Folder.clear()
                break
    return List_Of_FilePath_In_Folder  # 返回空列表表示文件夹或者文件不存在


# 数据读取
def DataReading(FilePath):
    List_Of_Points = []
    with open(FilePath) as f:
        for line in f:
            temp = line.split(',')  # 行内数据按','分割
            if -200 < float(temp[2]) < 200:
                List_Of_Points_In_Line = [float(x) for x in temp]
                List_Of_Points.append([List_Of_Points_In_Line[0], -List_Of_Points_In_Line[1], List_Of_Points_In_Line[2]])
    f.close()
    Array_Of_Point = numpy.array(List_Of_Points)
    return Array_Of_Point


# 保存数据
def DataSaving(DataPath, Data):
    numpy.savetxt(DataPath, Data)
    return True


DataPath11 = r"C:\Users\18320\Desktop\12312313213\动态重复性\6"

sss = os.listdir(DataPath11)

for x in sss:
    DataPath123 = DataPath11 + '\\' + x

    FileList11 = FolderReading(DataPath123)
    fffffffflist = []
    for i in range(8):
        # 正则表达式取focal点云
        if re.search('Focal', FileList11[i]):
            fffffffflist.append(FileList11[i])
    for i in range(4):
        SavePath11 = DataPath123 + '\\focal镜像后' + str(i) + '.txt'
        PointList1 = DataReading(fffffffflist[i])
        DataSaving(SavePath11, PointList1)
    print(DataPath123+" ------ over!")
