#!/usr/bin/python
# -*- coding: utf-8 -*-

'''定义应用中用到的所有事件'''

import os
import numpy


# 获取文件夹下所有文件的绝对路径
def FolderReading(FolderPath):
    List_Of_FilePath_In_Folder = []  # 用于存放文件夹中文件的绝对路径
    if (os.path.isdir(FolderPath)):
        List_Of_FileName_In_Folder = os.listdir(FolderPath)  # 读取文件夹中所有的文件名
        for File in List_Of_FileName_In_Folder:
            FilePath = os.path.join(FolderPath, File)  # 生成文件的绝对路径
            if (os.path.isfile(FilePath)):
                if (File[0] == '.'):  # 去除隐藏文件
                    pass
                else:
                    List_Of_FilePath_In_Folder.append(FilePath)
            else:
                List_Of_FilePath_In_Folder.clear()
                break
    return List_Of_FilePath_In_Folder  # 返回空列表表示文件夹或者文件不存在


# 数据读取
def DataReading(FilePath, Data_Column_Num, Data_Format):
    List_Of_Points = []
    with open(FilePath) as f:
        for line in f:
            List_Of_Points_In_Line = line.split(',')  # 行内数据按','分割
            for i in range(0, len(List_Of_Points_In_Line), Data_Column_Num):
                if (float(List_Of_Points_In_Line[i + 2]) < 500):  # 剔除无效点
                    Point = [List_Of_Points_In_Line[i], List_Of_Points_In_Line[i + 1], List_Of_Points_In_Line[i + 2]]
                    Point = [float(x) for x in Point]
                    List_Of_Points.append(Point)
    f.close()
    Array_Of_Point = numpy.array(List_Of_Points)
    return Array_Of_Point

# 阵列数据转散点数据
def ArrayDataToScatterDate(ArratData):
    pass


# 数据采样
def DataSimpling(BeforeData):
    pass


# 矩阵合并
def MatrixMerge(ListOfMatrix):
    pass


# 保存数据
def DataSaving(DataPath, Data):
    pass


if __name__ == '__main__':
    DataPath = r"G:\缓存\problem2#\20190513173949BBB"
    Point_Column_Num = 4
    Data_Format = '阵列'
    List_Of_File = FolderReading(DataPath)
    Array_Of_Points = DataReading(List_Of_File[0], Point_Column_Num, Data_Format)
    # 输出正确，下午添加改成numpy.array
    print(Array_Of_Points)
