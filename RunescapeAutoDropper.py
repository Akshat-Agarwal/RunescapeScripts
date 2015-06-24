import ctypes
import time


initialYValue = 469
horizontalOffset = 42 #Value needed to get to next column
x = 1958
y = initialYValue
timeDelay = 0.2
timeMousePressDelay = 0.1 #this is the delay between mouse press up and down to portray real human clicks

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
def rightClick():
	ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0,0) # right down
	time.sleep(timeMousePressDelay)
	ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0,0) # right up
	return 

def leftClick():
	ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # left down
	time.sleep(timeMousePressDelay)
	ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # left up
	return 

def dropSmallColumnItems(x,y):
	for iterator in range(0, 5):
		print "We're on location %d %d" % (x,y)
		time.sleep(timeDelay)
		ctypes.windll.user32.SetCursorPos(x, y)
		rightClick()

		y = y+38
		time.sleep(timeDelay)

		ctypes.windll.user32.SetCursorPos(x, y)
		leftClick()

def dropLargeColumnItems(x,y):
	for iterator in range(0, 6):
		print "We're on location %d %d" % (x,y)
		time.sleep(timeDelay)
		ctypes.windll.user32.SetCursorPos(x, y)
		rightClick()

		y = y+38
		time.sleep(timeDelay)

		ctypes.windll.user32.SetCursorPos(x, y)
		leftClick()

time.sleep(timeDelay)
dropSmallColumnItems(x,y)
#set y value to be 5 items below top item
print "Finished first column: %d %d" % (x,y)
#last item
time.sleep(timeDelay)
rightClick()
y = initialYValue + (38*5) + 12 #bad hack, need to make methods update value of Y, but currently they are passed by value
time.sleep(timeDelay)
print "before we set cursor for last item %d %d" % (x,y)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()

# move to next column
x = x + horizontalOffset
y = 469

dropSmallColumnItems(x,y)

#last item
time.sleep(timeDelay)
rightClick()
y = initialYValue + (38*5) + 12 #bad hack, need to make methods update value of Y, but currently they are passed by value
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()

#move to next column
x = x + horizontalOffset
y = 442

dropLargeColumnItems(x,y)

#last item
time.sleep(timeDelay)
rightClick()
y = initialYValue + (38*5) + 12 #bad hack, need to make methods update value of Y, but currently they are passed by value
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()

#move to next column
x = x + horizontalOffset
y = 442

dropLargeColumnItems(x,y)

#last item
time.sleep(timeDelay)
rightClick()
y = initialYValue + (38*5) + 12 #bad hack, need to make methods update value of Y, but currently they are passed by value
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()

