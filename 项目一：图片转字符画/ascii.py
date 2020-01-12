# -*- coding=utf-8 -*-

from PIL import Image
import argparse

#cmd命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')    #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80)    #输出字符画宽
parser.add_argument('--height', type = int, default = 80)    #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file    #输入的图片文件路径
WIDTH = args.width    #输出字符画的宽度
HEIGHT = args.height    #输出字符画的高度
OUTPUT = args.output    #输出字符画的路径


#创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    """RGB值转灰度值再转字符"""
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    #灰度值转换公式

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]    #返回一个列表中的字符


if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)    #Image.NEAREST表示输出低质量图片

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))    #im.getpixel((j,i))获取得到坐标RGB像素值，返回一个元组
        txt += '\n'

    print(txt)
    
    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)    #如果执行时配置了输出文件，将打开文件将 txt 输出到文件
    else:
        with open("G:\python\output.txt",'w') as f:
            f.write(txt)