#Importing needed modules
from PIL import Image
import sys

#Function obamicon: Takes a given path to image, takes the image, and turns it into the values of the Obama presidential campaign
def obamicon(image):
	#Opens Image from path
	im = Image.open(image)
	#Defines the needed colors from the campaign
	darkBlue = (0, 51, 76)
	red = (217, 26, 33)
	lightBlue = (112, 150, 158)
	yellow = (252, 227, 166)
	#Get the pixels intensity from the picture
	pxlImage = list(im.getdata())
	#Create a new image
	newIm = Image.new("RGB", im.size)
	#Loop through each pixel; See what intensity is the pixel and change that pixel's color accordingly
	for i in range(len(pxlImage)):
		intensity = pxlImage[i][0] + pxlImage[i][1] + pxlImage[i][2]
		if intensity < 182:
			pxlImage[i] = darkBlue
		elif intensity < 364:
			pxlImage[i] = red
		elif intensity < 546:
			pxlImage[i] = lightBlue
		else:
			pxlImage[i] = yellow
	#Put the data of the changed pixels into the new image
	newIm.putdata(pxlImage)
	#Show the image
	newIm.show()

#When run, see if an argument is given. If so, run obamicon on each argument (which should be a path to the image)

if len(sys.argv) == 1: 
	img = raw_input("Enter the image destination: ")
	try: 
		obamicon(img)
	except IOError: 
		print("The image you entered does not exist.")
else:
	try: 
		images = sys.argv
		for i in range(1, len(images)):
			obamicon(images[i])
	except IOError:
		print("One (or more) of the images you entered does not exist.") 





