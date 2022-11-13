import os
from rich import print
import random
from rich.panel import Panel

def titleName(RC, RC2, RC3, RC4, RC5, RC6, RC7):
    """ Prints a banner

    Args:
        RC (string): Random color from "titleNameStart" function
        RC2 (string): Random color from "titleNameStart" function
        RC3 (string): Random color from "titleNameStart" function
        RC4 (string): Random color from "titleNameStart" function
        RC5 (string): Random color from "titleNameStart" function
        RC6 (string): Random color from "titleNameStart" function
        RC7 (string): Random color from "titleNameStart" function
    """
    
    space = ' '
    name = f"[bold {RC}] _    _ _   _ _____ _____ _____ _____ _   _ _   _[/]\n[bold {RC2}]| |  | | | | |_   _|_   _|  ___/  ___| | | | \ | |[/]\n[bold {RC3}]| |  | | |_| | | |   | | | |__ \ `--.| | | |  \| |[/]\n[bold {RC4}]| |/\| |  _  | | |   | | |  __| `--. \ | | | . ` |[/]\n[bold {RC5}]\  /\  / | | |_| |_  | | | |___/\__/ / |_| | |\  |[/]\n[bold {RC6}] \/  \/\_| |_/\___/  \_/ \____/\____/ \___/\_| \_/[/]"
    print(Panel.fit(name, title=f"[bold {RC7}]У Бога верујемо[/]"))
    
def titleNameStart():
    """ Grabs 6 random colors from the given list """
    
    colors = ["black","red","green","yellow","blue","magenta","cyan","white","bright_black","bright_red","bright_green","bright_yellow","bright_blue","bright_magenta","bright_cyan","bright_white","grey0","navy_blue","dark_blue","blue3","blue1","dark_green","deep_sky_blue4","dodger_blue3","dodger_blue2","green4","spring_green4","turquoise4","deep_sky_blue3","dodger_blue1","dark_cyan","light_sea_green","deep_sky_blue2","deep_sky_blue1","green3","spring_green3","cyan3","dark_turquoise","turquoise2","green1","spring_green2","spring_green1","medium_spring_green","cyan2","cyan1","purple4","purple3","blue_violet","grey37","medium_purple4","slate_blue3","royal_blue1","chartreuse4","pale_turquoise4","steel_blue","steel_blue3","cornflower_blue","dark_sea_green4","cadet_blue","sky_blue3","chartreuse3","sea_green3","aquamarine3","medium_turquoise","steel_blue1","sea_green2","sea_green1","dark_slate_gray2","dark_red","dark_magenta","orange4","light_pink4","plum4","medium_purple3","slate_blue1","wheat4","grey53","light_slate_grey","medium_purple","light_slate_blue","yellow4","dark_sea_green","light_sky_blue3","sky_blue2","chartreuse2","pale_green3","dark_slate_gray3","sky_blue1","chartreuse1","light_green","aquamarine1","dark_slate_gray1","deep_pink4","medium_violet_red","dark_violet","purple","medium_orchid3","medium_orchid","dark_goldenrod","rosy_brown","grey63","medium_purple2","medium_purple1","dark_khaki","navajo_white3","grey69","light_steel_blue3","light_steel_blue","dark_olive_green3","dark_sea_green3","light_cyan3","light_sky_blue1","green_yellow","dark_olive_green2","pale_green1","dark_sea_green2","pale_turquoise1","red3","deep_pink3","magenta3","dark_orange3","indian_red","hot_pink3","hot_pink2","orchid","orange3","light_salmon3","light_pink3","pink3","plum3","violet","gold3","light_goldenrod3","tan","misty_rose3","thistle3","plum2","yellow3","khaki3","light_yellow3","grey84","light_steel_blue1","yellow2","dark_olive_green1","dark_sea_green1","honeydew2","light_cyan1","red1","deep_pink2","deep_pink1","magenta2","magenta1","orange_red1","indian_red1","hot_pink","medium_orchid1","dark_orange","salmon1","light_coral","pale_violet_red1","orchid2","orchid1","orange1","sandy_brown","light_salmon1","light_pink1","pink1","plum1","gold1","light_goldenrod2","navajo_white1","misty_rose1","thistle1","yellow1","light_goldenrod1","khaki1","wheat1","cornsilk1","grey100"]
    randomColor = random.choice(colors)
    randomColor2 = random.choice(colors)
    randomColor3 = random.choice(colors)
    randomColor4 = random.choice(colors)
    randomColor5 = random.choice(colors)
    randomColor6 = random.choice(colors)
    randomColor7 = random.choice(colors)
    titleName(randomColor, randomColor2, randomColor3, randomColor4, randomColor5, randomColor6, randomColor7)