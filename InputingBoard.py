from PIL import Image
import webbrowser
import os
import glob

def getColor(col):
    rnorm = col[0]/255.0
    gnorm = col[1]/255.0
    bnorm = col[2]/255.0
    cmax = max(rnorm, gnorm, bnorm)
    cmin = min(rnorm, gnorm, bnorm)
    delta = cmax - cmin
    if max(col) == col[0]:
        hue = ((((gnorm - bnorm)/ delta)) % 6) * 60
    elif max(col) == col[1]:
        hue = ((((bnorm - rnorm)/ delta)) + 2) * 60
    else:
        hue = ((((rnorm - gnorm)/ delta)) + 4)  * 60

    if hue >= 5 and hue <= 35:
        color = "r"
    elif hue >= 40 and hue <= 90:
        color = "l"
    elif hue >= 100 and hue <= 155:
        color = "g"
    elif hue >= 180 and hue <= 240:
        color = "b"
    elif hue >= 270 and hue <= 315:
        color = "d"
    elif hue >= 316 and hue <= 355:
        color = "h"

    return color

newest = max(glob.iglob('C:\\Users\Ian\Google Drive\ScreenShotBackup\\*.[Pp][Nn][Gg]'), key=os.path.getctime)
board = Image.open(newest)
pic = board.load( )
    
        
totalcount = 1
countrow = 0
countcol = 0
xpos = 95
ypos = 940

bstring = ""

while countrow < 5:
    while countcol < 6:
        print(str(totalcount) + " " + str(getColor(pic[xpos,ypos])))
        bstring = bstring + getColor(pic[xpos,ypos])
        countcol +=1
        xpos += 177
        totalcount += 1
    countcol = 0
    countrow += 1
    xpos = 96
    ypos += 177

webbrowser.open_new("http://pad.dawnglare.com/?patt=" + bstring)
