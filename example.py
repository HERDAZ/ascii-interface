import interface, os

HSIZE = int(os.popen('stty size','r').read().split()[1])
VSIZE = 20

frame = interface.innitFrame(HSIZE,VSIZE)
mainW = interface.Window([0,0],HSIZE,VSIZE)
mainW.setBackground('w')
mainW.addText("Test\nabcd")
mainW.vSplit(clean=False)

renders = interface.getWindowsRenders([mainW])
interface.refreshScreen(frame,VSIZE,verticalLines=renders[0],horizontalLines=renders[1])
