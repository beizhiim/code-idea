"""
十进制 与 十六进制的色值 链接：https://baike.baidu.com/item/%E8%89%B2%E5%80%BC/5148574
"""
from machine import PWM, Pin
import time

#定义对象 红/绿/蓝LED控制的PWM 输出
rgbR = PWM(Pin(2), freq=1000,duty=0)
rgbG = PWM(Pin(4), freq=1000,duty=0)
rgbB = PWM(Pin(16), freq=1000,duty=0)

# 十进制颜色值
RGB_color = ['红','绿','蓝','黄','青' , '橙','紫','白','黑','灰']
RGB_value = ['(255,0,0)','(0,255,0)','(0,0,255)','(255, 255, 0)','(0, 255, 255)',
            '(255, 165, 0)', '(128, 0, 128)','(255,255,255)','(0,0,0)','(128, 128, 128)']
color_dict = dict(zip(RGB_color, RGB_value))
# 十六进制颜色值
colorhex = {"红": "FF0000", "绿": "00FF00", "蓝": "0000FF", "黄": "FFFF00", "紫": "FF00FF", 
            "白": "FFFFFF", "黑": "000000", "碧绿": "70DB93", "巧克力": "5C3317", "米": "f5f5dc"}

import json
def read_colortxt(txt_path):
    """注释：
        *****给一个txt文本路径，获取内容并用json转换为字典。
        *****注意：文本保存的格式应符合 json字符串转字典的要求
        *****文本保存内容格式为：{"name": "XiaoMing", "age": "17", "address": "China"}
    param txt_path : 保存颜色的TXT文本路径，（例如："d/colors.txt"）
    返回值： 一个保存颜色hex数据的字典
    """
    try :
        with open(txt_path,  mode='r', encoding="uft-8") as file:
            dcit =json.loads(file.read())
        return dcit
    except Exception as e:
        print(f'读取发生错误: {e}')
        return None


#  给一个color_dict字典里的键(颜色的中文名)，换一个对应的RGB十进制颜色值  
def get_color(color):
    value = eval(color_dict[color])
    print(f"{color}色为：{value}")
    r = value[0]
    g = value[1]
    b = value[2]
    set_color(r, g, b)

# 将RGB颜色从十六进制的转换为十进制值，并转入 set_color() 函数
def coler_HexDec(hex_color):
    # 将十六进制颜色码转换为RGB十进制值
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    set_color(r,g,b)

# 设置颜色函数 ”改变的是三个rgb颜色LED的PWM占空比，分成255等分“
def set_color(red, green, blue):
    rgbR.duty(int(red * 1023 / 255))
    rgbG.duty(int(green * 1023 / 255))
    rgbB.duty(int(blue * 1023 / 255))

if __name__ == '__main__':
    
#     set_color(255, 0, 0)  # 纯红色
#     set_color(0, 255, 0)  # 纯绿色
#     set_color(0, 0, 255)  # 纯蓝色
#     coler_HexDec('ff0000')  #红
#     coler_HexDec('00ff00')  #绿
#     coler_HexDec('0000ff')  #蓝
#     colors = read_colortxt("RGBcolors.txt") #打开并获取RGBcolors.txt的颜色
#     coler_HexDec(colors['白'])

# #  循环点亮 color_dict 字典里的颜色
#     for i  in range(len(colorname)):
#         get_color(colorname[i])
#         time.sleep(2)

#  循环点亮 colorhex 字典里的颜色
    HEX_colors = tuple(colorhex.keys())
    HEX_values = tuple(colorhex.values())
    for i in range(len(HEX_values)):
        coler_HexDec(HEX_values[i])
        print(f'{HEX_colors[i]}色：{HEX_values[i]}')
        time.sleep_ms(800)
 
#  循环点亮 "RGBcolors.txt"文本里的颜色
    txtcolors = read_colortxt("RGBcolors.txt")
    HEX_colors = tuple(txtcolors.keys())
    HEX_values = tuple(txtcolors.values())
    for i in range(len(HEX_values)):
        coler_HexDec(HEX_values[i])
        print(f'{HEX_colors[i]}色：{HEX_values[i]}')
        time.sleep_ms(500)

#     get_color("紫")
#     time.sleep(0.5)
#     coler_HexDec(colorhex['紫'])
    
