class Window():
    def __init__(self,startCoords,width,height,outline='*',subWindow=False):
        self.startCoords = startCoords
        self.width = width
        self.height = height
        if subWindow:
            self.verticalLines = []
            self.horizontalLines = []
        else :
            self.verticalLines = [[startCoords[0],0,height,outline],[startCoords[0],startCoords[0]+width-1,height,outline]]
            self.horizontalLines = [[startCoords[1],0,width,outline],[startCoords[0]+height-1,0,width,outline]]
        self.subWindow = subWindow
        self.background = ''


    def addText(self,text,centering='left'):
        text += '\n'
        word = ''
        line = ''
        n = 0 # line number
        a = 0 if self.subWindow else 1
        for i in text:
            if i == '\n':
                if len(word) + 1 + len(line) > self.width:
                    if centering == 'left':
                        self.horizontalLines.append([self.startCoords[1]+n+a,self.startCoords[0]+a,line])
                        n += 1
                        self.horizontalLines.append([self.startCoords[1]+n+a,self.startCoords[0]+a,word])
                        n += 1
                    elif centering == 'right':
                        self.horizontalLines.append([self.startCoords[1]+n,self.startCoords[0]+self.width-len(line)-(1-a),line])
                        n += 1
                        self.horizontalLines.append([self.startCoords[1]+n,self.startCoords[0]+self.width-len(word)-(1-a),word])
                        n += 1
                    elif centering == "center":
                        self.horizontalLines.append([self.startCoords[1]+n,int(self.width/2)-int((len(line+word))/2),line])
                        n += 1
                        self.horizontalLines.append([self.startCoords[1]+n,int(self.width/2)-int(len(word)/2),word])
                        n += 1
                else:
                    if centering == 'left':
                        self.horizontalLines.append([self.startCoords[1]+n+a,self.startCoords[0]+a,line+word])
                    elif centering == 'right':
                        self.horizontalLines.append([self.startCoords[1]+n,self.startCoords[0]+self.width-len(word)-len(line)-(1-a),line+word])
                    elif centering == 'center':
                        self.horizontalLines.append([self.startCoords[1]+n,self.startCoords[0]+int((self.width-len(line+word))/2),line+word])
                n += 1
                line,word = '',''

            elif i == ' ':
                if len(word) + 1 + len(line) > self.width:
                    if centering == 'left':
                        self.horizontalLines.append([self.startCoords[1]+n+a,self.startCoords[0]+a,line])
                    elif centering == 'center':
                        self.horizontalLines.append([self.startCoords[1]+n,self.startCoords[0]+int((self.width-len(line))/2),line])
                    n += 1
                    line = ''
                else:
                    line += word + ' '
                    word = ''
            else:
                word += i

    def setBackground(self,filler='.'):
        if self.subWindow:
            for i in range(self.height):
                self.horizontalLines.append([self.startCoords[1]+i,self.startCoords[0],self.width,filler])
        else:
            for i in range(self.height-2):
                self.horizontalLines.append([self.startCoords[1]+1+i,self.startCoords[0],self.width-1,filler])

    def hSplit(self,ratio=50,spliter='-',fillChildrens=False):
        topHeight = int(self.height*(ratio/100))
        top = Window(
        [self.startCoords[0],self.startCoords[1]+1] if self.subWindow else [c+1 for c in self.startCoords]
        ,self.width if self.subWindow else self.width-2
        ,topHeight
        ,subWindow=True)

        bottom = Window(
        [self.startCoords[0] if self.subWindow else self.startCoords[0]+1,self.startCoords[1]+topHeight+1]
        ,self.width if self.subWindow else self.width-2
        ,self.height-topHeight-1
        ,subWindow=True)

        if self.background != '':
            top.setBackground(self.background)
            bottom.setBackground(self.background)

        if self.subWindow:
            self.horizontalLines = []
            self.horizontalLines.append([self.startCoords[1]+topHeight,self.startCoords[0],self.width,spliter])
        else:
            self.horizontalLines = self.horizontalLines[0:2]
            self.horizontalLines.append([self.startCoords[1]+topHeight,self.startCoords[0]+1,self.width-2,spliter])


        return top,bottom


    def vSplit(self,ratio=50,spliter='|',clean = True):
        leftWidth = int(self.width*(ratio/100))
        left = Window(
        [self.startCoords[0],self.startCoords[1]+1] if self.subWindow else [c+1 for c in self.startCoords]
        ,leftWidth
        ,self.height if self.subWindow else self.height-2
        ,subWindow=True)

        right = Window(
        [self.startCoords[0]+leftWidth+1,self.startCoords[1]+1]
        ,self.width-leftWidth-1
        ,self.height if self.subWindow else self.height-2
        ,subWindow=True)

        if self.background != '':
            left.setBackground(self.background)
            right.setBackground(self.background)

        if self.subWindow:
            if clean:
                self.horizontalLines = []
            self.verticalLines.append([self.startCoords[1],self.startCoords[0]+leftWidth,self.height,spliter])
        else:
            if clean:
                self.horizontalLines = self.horizontalLines[0:2]
            self.verticalLines.append([self.startCoords[1]+1,self.startCoords[0]+leftWidth,self.height-2,spliter])

        return left,right


def innitFrame(HSIZE:int,VSIZE:int,filling:str = " "):
    frame = [list(f"{filling*(HSIZE)}") for _ in range(VSIZE)]
    return frame

def getWindowsRenders(windows,getChildrens=False):
    hLines,vLines = [],[]
    for window in windows:
        for line in window.horizontalLines:
            hLines.append(line)
            print(line)
        for line in window.verticalLines:
            vLines.append(line)         
            print(line)
    return vLines,hLines

def refreshScreen(previousFrame,VSIZE,horizontalLines=[],verticalLines=[],printFrame=True):
    for i in range(VSIZE):
        line = previousFrame[i]
        hFinishedLines,vFinishedLines = [],[]
        for hLine in horizontalLines:
            if hLine[0] == i:
                if len(hLine) == 4:
                    for j in range(hLine[2]):
                        line[hLine[1]+j] = hLine[3]
                    hFinishedLines.append(hLine)
                else:
                    for j in range(len(hLine[2])):
                        line[hLine[1]+j] = hLine[2][j]
        for hLine in hFinishedLines:
            horizontalLines.remove(hLine)
        for vLine in verticalLines:
            if vLine[0] <= i:
                line[vLine[1]] = vLine[3]
                vLine[2] -= 1
            if vLine[2] == 0:
                vFinishedLines.append(vLine)
        for vLine in vFinishedLines:
            verticalLines.remove(vLine)
        previousFrame[i] = line
        if printFrame:print(''.join(line))
