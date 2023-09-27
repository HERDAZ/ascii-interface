# ascii-interface

A python code to create ascii interface in the command line
## Features

**Spliting windows**

``` python
window.hSplit(self,ratio=50,spliter='-',fillSubWindows=False)
```

Splits the window with a horizontal line with whatever spliter is set to. (If window has background, the subwindow wont inherit the background unless ```fillSubWindows = True```)
Return the left and right subwindow in a tuple.

``` python
window.vSplit(self,ratio=50,spliter='|',fillSubWindows=False)
```

Split the window with a vertical line with whatever spliter is set to. (If window has background, the subwindow wont inherit the background unless ```fillSubWindows = True```)
Returns the top and bottom subwindow in a tuple.

**Setting window's background**

``` python
window.setBackground(self,filler='.')
```

Fills the window with whatever character you want. (If the window is splited, it's background will be deleted. To prevent that, use ```clean = False``` when splitting)

**Adding text**

``` python
window.addText(self,text,centering="left")
```

Adds text to the window (duh). ```text``` has to only include character and newlines. The text will automaticaly be arranged to not cut words in half, until I implement the option to not have it arranged.```centering``` determine where horizontaly on the window the text will be. For now, the only choices for ```centering``` are ```"left"``` or ```"right"```. A ```"center"``` option is to come.

## Creating,updating and printing the frame

``` python
Window(startCoords,HSIZE,VSIZE,outline='*',subWindow=False)
```

Creates the window with lenght ```VSIZE``` and width ```HSIZE```.```startCoords``` determines where on the screen the top left of the window is (in most cases, you only set it once with [0,0], and the subwindow's startCoords are automaticaly calculated).``` outline ``` adds line on the 4 edges of the window, reducing the usable dimentions by 2. It needs ```subwindow = True``` to be effective.

``` python
innitFrame(HSIZE,VSIZE,filling = " ")
```

When starting, you must generate a frame, which is an array of array filled with a character. ``` HSIZE ``` and ``` VSIZE ``` are the dimetion of your main window.

``` python
getWindowsRenders(windows)
```

To update the frame, you need to collect all the horizontal and vertical lines of the windows that you want to update. (Spliting lines are part of the split window). Returns 2 arrays of lines, horizontals and verticals lines.

``` python
refreshScreen(previousFrame,VSIZE,horizontalLines=[],verticalLines=[]):
```

Goes trough the horizontal and vertical lines provided and update the previous frame, so that it only update the lines that need updating.
