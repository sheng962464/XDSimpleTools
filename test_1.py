# -*- coding: utf-8 -*-

# coding: utf-8

# coding=utf-8

# -*- coding: cp936 -*-

# -*- coding: ascii -*-

import os
import re
import numpy


# 获取文件夹下所有文件的绝对路径
def FolderReading(xFolderPath):
    List_Of_FilePath_In_Folder = []  # 用于存放文件夹中文件的绝对路径
    if os.path.isdir(xFolderPath):
        List_Of_FileName_In_Folder = os.listdir(xFolderPath)  # 读取文件夹中所有的文件名
        for File in List_Of_FileName_In_Folder:
            FilePath = os.path.join(xFolderPath, File)  # 生成文件的绝对路径
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
def DataReading(xFilePath):
    List_Of_Points = []
    with open(xFilePath) as f:
        for line in f:
            temp = line.split(',')  # 行内数据按','分割
            if -200 < float(temp[2]) < 200:
                List_Of_Points_In_Line = [float(x) for x in temp]
                List_Of_Points.append(
                    [List_Of_Points_In_Line[0], -List_Of_Points_In_Line[1], List_Of_Points_In_Line[2]])
    f.close()
    Array_Of_Point = numpy.array(List_Of_Points)
    return Array_Of_Point


# 保存数据
def DataSaving(xDataPath, xData):
    numpy.savetxt(xDataPath, xData)
    return True


if __name__ == '__main__':
    # 最外层文件夹路径
    FolderPath = r"C:\Users\18320\Desktop\12312313213\动态重复性\6"
    # 获取最外层文件夹下的子文件夹的名字
    subFolderPathList = os.listdir(FolderPath)
    # 对子文件夹逐个处理
    for x in subFolderPathList:
        subFolderPath = FolderPath + '\\' + x
        FileList = FolderReading(subFolderPath)
        focalFileList = []
        for i in range(len(FileList)):
            # 正则表达式获取focal扫描的点云
            if re.search('Focal', FileList[i]):
                focalFileList.append(FileList[i])
        # 对focal扫描的点云进行镜像
        for i in range(len(focalFileList)):
            SavePath11 = subFolderPath + '\\focal镜像后' + str(i) + '.txt'
            PointList1 = DataReading(focalFileList[i])
            DataSaving(SavePath11, PointList1)
        print(subFolderPath + " ------ over!")
