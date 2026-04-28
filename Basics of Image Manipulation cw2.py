import cv2
import matplotlib.pyplot as plt
image=cv2.imread("pencils_pic.jpg")

#Convert BGR to RGB
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

#Convert to grayscale
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.title("Grayscale Image")
plt.show()

#Cropping the image
#Assume we know the region we want : rows 100 to 200 and columns 20 to 70
cropped_image=image[100:200,20:70]
cropped_rgb=cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()

#Rotate the image by 45゜around its center
(h,w)=image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,45,1.0) #Rotate by 45 degrees
rotated=cv2.warpAffine(image,M,(w,h))

rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated image")
plt.show()