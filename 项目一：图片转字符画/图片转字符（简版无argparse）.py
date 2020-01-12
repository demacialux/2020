from PIL import Image

def get_char(r, g, b, alpha = 256):
    """RGB转灰度值并映射到字符"""
    if alpha == 0:
        return " "
    #创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）反之
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    #RGB转换灰度值公式
    length = len(ascii_char)    #获取字符长度
    x = gray / (alpha + 1.0) * length
    return ascii_char[int(x)]    #返回一个列表中的字符

def write_file(out_file_name,content):
    """文件保存本地"""
    with open(out_file_name,"a") as f:
        f.write(content)

def main(file_name, out_file_name, width = 80, height = 80,):
    """读取图片像素并转化为字符"""
    text = " "
    im = Image.open(file_name)
    im = im.resize((width, height),Image.NEAREST)    #Image.NEAREST表示输出低质量图片
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j,i))    #im.getpixel((j,i))获取坐标RGB像素值，返回一个元组
            text += get_char(*content)
        text += "\n"
    print (text)
    write_file(out_file_name,text)

if __name__ == '__main__':
    a = "G:\python\项目一：图片转字符\小兔子.jpg"
    b = "G:\python\项目一：图片转字符\小兔子.txt"
    main(a, b)
