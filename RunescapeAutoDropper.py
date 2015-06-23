import ctypes
import time

x = 1958
y = 469
timeDelay = 0.4

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
def rightClick():
	ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0,0) # right down
	ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0,0) # right up
	return 

def leftClick():
	ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # left down
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

#last item
time.sleep(timeDelay)
rightClick()
y = y + 12
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()
time.sleep(timeDelay)

#move to next column
x = x + 42
y = 469

dropSmallColumnItems(x,y)

#last item
time.sleep(timeDelay)
rightClick()
y = y + 12
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()
time.sleep(timeDelay)

#move to next column
x = x + 42
y = 442

dropLargeColumnItems(x,y)

#last item
time.sleep(timeDelay)
rightClick()
y = y + 12
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()
time.sleep(timeDelay)

#move to next column
x = x + 42
y = 442

dropLargeColumnItems(x,y)

#last item
time.sleep(timeDelay)
rightClick()
y = y + 12
time.sleep(timeDelay)
ctypes.windll.user32.SetCursorPos(x, y)
leftClick()
time.sleep(timeDelay)

