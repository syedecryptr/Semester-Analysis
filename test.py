from PIL import Image
import pytesser
import numpy as np
import cv2
import pyscreenshot as ImageGrab
import time
import pickle
import pyautogui
data = ["Empty"]
if __name__ == '__main__':
	time.sleep(2)
	for var in xrange(60):
		imageOriginal = np.array(ImageGrab.grab(bbox =(0, 61, 1350,711)))
		# imageOriginal = cv2.imread("capture.png")
		imageOriginal= cv2.copyMakeBorder(imageOriginal,10,10,10,50,cv2.BORDER_CONSTANT,value=(255, 255, 255))
		pyautogui.press('pagedown',0.01)
		# cv2.imshow("Original",imageOriginal)
		# print (np.shape(imageOriginal))
		#Converting to Gray colour Image from Original
		imageGray = cv2.cvtColor(imageOriginal, cv2.COLOR_BGR2GRAY)
		# cv2.imshow("Gray",imageGray)
		#Applying Threshold to the gray Image
		val, imageThresh = cv2.threshold(imageGray, 240, 255, cv2.THRESH_BINARY)


		#Eroding the Image to find the contours.
		kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
		erosion = cv2.erode(imageThresh,kernel,iterations = 8)

		# cv2.imshow("erosion",erosion)
		# cv2.waitKey(-1)
		#Applying Gausian Blur to the Image
		erosion = cv2.GaussianBlur(erosion, (5, 5), 0)
		#cv2.imshow("eroded", erosion)
		#Finding all the contours in the Image
		cnts,_ = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		#Now try to find "6" that corresponds to the sixth semester in the image by filtering contours by size window.
		# cv2.drawContours(imageOriginal, cnts, -1,(0,255,0),2)
					

		# cv2.waitKey(-1)
		for cnt in cnts: 
			x,y,w,h = cv2.boundingRect(cnt)
			if(20<w<50and 20<h<50):
				cropimg = imageOriginal[y:y+h, x:x+h]
				#converting the image to PIL for using tesseract.
				PILimg = Image.fromarray(cropimg)
				string = pytesser.image_to_string(PILimg)
				string = string[:1]
				# print string
				if string == "6":
					sem6Image = imageThresh[y:y+h, 0:np.shape(imageOriginal)[1]]
					# cv2.imshow("6th semester Strip", sem6Image)
					# cv2.waitKey(-1)
					PILsemImg = Image.fromarray(sem6Image)
					stringSem = pytesser.image_to_string(PILsemImg)
					if len(stringSem) > 15 and data[-1]!= stringSem:
							data.append(stringSem[0:-2])
							
	# cv2.rectangle(imageOriginal, (x,y),(x+w,y+h),(0,255,0),2)
	# cv2.imshow("Rects", imageOriginal)
	# cv2.waitKey(-1)
	num = 0
	with open("DataFileGrades.txt", 'w') as f:
		for s in data:
			f.write(s + '\n')
			print num, s
			num += 1
		# pim = Image.fromarray(im)
		# print(pytesser.image_to_string(pim))

		#print(pytesseract.image_to_string(Image.open('Capture.PNG')))
	 #agar contour k andar 6 mil jae to uss comlumn ko crop kar k ... 