import cv2
import datetime as datetime

cam = cv2.VideoCapture(0)
ret, img = cam.read()
data = datetime.datetime.now()
datastr = "{}{}{}-{:02}.{:02}.{:02}".format(
		int(data.year),
		int(data.month),
		int(data.day),
		int(data.hour),
		int(data.minute),
		int(data.second))
filename = datastr + ".png"
cv2.imwrite(filename,img)
print("Saved image with {}".format(filename))
cam.release()

