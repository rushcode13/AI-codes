
import cv2

#Load the image 
image=cv2.imread('pic_coding.jpg')

#resize the window to a specific size without resizing the image 

cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)#create a resizable window

cv2.resizeWindow('Loaded Image',800,500)#set the window sixe to 800X500 width * height

#convert image to grayscale 
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#display the grayscale image in  a single window 
cv2.imshow('Processed image',gray_image)

#Display the image in the resizes window 
cv2.imshow('Loaded Image',image)

cv2.waitKey(0)#Wait for a key press 

cv2.destroyAllWindows()#Close the window 

#print image properties 
print(f"Image Dimentions: {image.shape}")#Height,Width,Channels




