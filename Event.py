#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
定义应用中用到的所有事件
'''

import os
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
            List_Of_Points_In_Line = [float(x) for x in temp]
            List_Of_Points.append(List_Of_Points_In_Line)
    f.close()
    Array_Of_Point = numpy.array(List_Of_Points)
    return Array_Of_Point


# 阵列数据转散点数据
def ArrayDataToScatterDate(xArrayData, xData_Column_Num):
    List_Of_Points = []
    for i in range(xArrayData.shape[0]):
        for j in range(0, xArrayData.shape[1], xData_Column_Num):
            if xArrayData[i][j + 2] > -500:
                Point = [xArrayData[i][j], xArrayData[i][j + 1], xArrayData[i][j + 2]]
                List_Of_Points.append(Point)
    Array_Of_Points = numpy.array(List_Of_Points)
    return Array_Of_Points


# 数据采样(均匀采样)
def DataSimpling(xBeforeData, xData_Column_Num, xSampleNum):
    List_Of_Points = []
    if xBeforeData.shape[1] > 4:
        for i in range(xBeforeData.shape[0]):
            List_Of_Points_In_Line = []
            for j in range(0, xBeforeData.shape[1], xData_Column_Num * xSampleNum):
                for k in range(xData_Column_Num):
                    List_Of_Points_In_Line.append(xBeforeData[i][j + k])
            List_Of_Points.append(List_Of_Points_In_Line)
        AfterData = numpy.array(List_Of_Points)
        return AfterData


# 保存数据
def DataSaving(xDataPath, xData):
    numpy.savetxt(xDataPath, xData)
    return True


if __name__ == '__main__':
    DataPath = r"G:\缓存\problem2#\20190513173949BBB"
    SavePath = r"G:\缓存\problem2#\20190513173949BBB\5.txt"
    Point_Column_Num = 4
    Data_Format = '阵列'
    List_Of_File = FolderReading(DataPath)
    if len(List_Of_File) == 0:
        print("文件路径错误！")
    else:
        test = DataReading(List_Of_File[0])
        # 输出正确，下午添加改成numpy.array
        print(test.shape)
        test2 = DataSimpling(test, 4, 32)
        print(test2.shape)
        test3 = ArrayDataToScatterDate(test2, 4)
        print(test3)
        if DataSaving(SavePath, test3):
            print("保存成功")
