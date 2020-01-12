import cv2
import os
show_height = 40
show_width = 80

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#生成一个ascii字符列表
lenth = len(ascii_char)

def main(file):
    """视频逐帧转灰度图并映射为字符"""
    cap = cv2.VideoCapture(file)    #加载一个视频
    if cap.isOpened():    #判断视频是否正常打开
        ret, frame = cap.read()    #ret返回布尔值，frame为图像矩阵
    else:
        ret = False

    outputList = []    #初始化输出列表
    while ret:    #循环读取视频帧
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    #转化为灰度图
        img = cv2.resize(gray, (show_width, show_height))    #重置灰度图大小
        text = " "
        for pixel_line in img:    #读取灰度值
            for pixel in pixel_line:
                text += ascii_char[int(pixel / 256 * lenth)]
            text += "\n"
        outputList.append(text)
        ret, frame = cap.read()    #重新读取
    print("处理完毕")

    for frame in outputList:
        os.system("cls")    #清屏
        print(frame)    #播放

if __name__ == "__main__":
    main(input("视频路径："))