import interface, os

HSIZE = int(os.popen('stty size','r').read().split()[1]) # get the width of the window (I know it's janky, but it works on linux)
VSIZE = 20

frame = interface.innitFrame(HSIZE,VSIZE) # innitialise the frame
mainW = interface.Window([0,0],HSIZE,VSIZE) # create the main window
subWindows = mainW.vSplit(ratio = 70) # split it verticaly
subWindows[0].addText("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\nreprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",centering='left') # add text to theleft subWindow
subWindows[1].setBackground('X') # set the background of the right subwindow

renders = interface.getWindowsRenders([mainW,subWindows[0],subWindows[1]]) # get all lines from the windows
interface.refreshScreen(frame,VSIZE,verticalLines=renders[0],horizontalLines=renders[1]) # put the renders on the frame and print it
