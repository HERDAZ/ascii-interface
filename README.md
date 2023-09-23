# ascii-interface

A python code to create ascii interface in the command line

## Features

**Split windows**

window.hSplit(ratio=50,spliter='-',fillSubWindows=False)

Split the window with a horizontal line with whatever spliter is set to. (If
window has background, the subwindow wont inherit the background unless
fillSubWindows = True)
Return the left and right subwindow in a tuple.

window.vSplit(ratio=50,spliter='|',fillSubWindows=False)

Split the window with a vertical line with whatever spliter is set to. (If
window has background, the subwindow wont inherit the background unless
fillSubWindows = True)
Return the top and bottom subwindow in a tuple.

**Set window's background**

window.setBackground(filler='.')

Fills the window with whatever character you want. (If the window is splited,
it's background will be deleted. To prevent that, use clean = False when
splitting)

**Add text**

addText(self,text,centering="left")

Add text to the window (duh). text has to only include character and newlines.
The text will automaticaly be arranged to not wut words in half, until I
implement the option to not have it arranged.
``` centering ``` determine where hozintaly on the window the text will be. For
now, the only choice for ``` centering ``` is 'left' or 'right'. A 'middle'
option is to come.

## Updating the frame

innitFrame(HSIZE,VSIZE,filling = " ")

When starting, you must generate a frame, which is an array of array filled
with a character. ``` HSIZE ``` and ``` VSIZE ``` are the dimetion of your main
window.

getWindowsRenders(windows)

To update the frame, you need to collect all the horizontal and vertical lines
of the windows that you want to update. (Spliting lines are part of the splited
window)

refrechScreen(previousFrame,VSIZE,horizontalLines=[],verticalLines=[]):

Goes thru the horizontal and vertical lines provided and update the previous
frame, so that it only update the line that need updating.
