import os

def get_filename(path_1,filepath):
    name_1 = os.listdir(path_1)

    for a in name_1:
        file = open(filepath,"a")
        file.write("\n"*2 + a)    #写入文件夹名

        path_2 = path_1 + "//" + a    #原文件二级目录
        name_2 = os.listdir(path_2)
        for b in name_2:
            r = os.path.splitext(b)
            file.write("\n" + r[0])    #写入无后缀文件名

path_1 = r"I:/新建文件夹"    #原文件一级目录
filepath = r"G:\python\fanhao.txt"  #写入并保存至新目录
get_filename(path_1,filepath)