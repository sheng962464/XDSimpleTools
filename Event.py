#!/usr/bin/python
# -*- coding: utf-8 -*-

'''定义应用中用到的所有事件'''

import os


# 读取数据
def DataReading(DataPath, Data, Point_Column_Num, Data_Format):
    List_Of_File_In_Folder = os.listdir(DataPath)
    for File in List_Of_File_In_Folder:
        FilePath = DataPath + '/' + File
        if (os.path.isdir(FilePath)):
            if (File[0] == '.'):  # 去除隐藏文件
                pass
            else:
                pass


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
