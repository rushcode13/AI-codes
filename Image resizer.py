#This is the classwork activity 2 done in class 1 of this module. It has been typed as hw "image resizer from the same class"
import cv2  # Import the OpenCV library for image processing

# Load the image from the specified file path
image = cv2.imread('example.jpg')  # Reads the image as a NumPy array in BGR format

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found. Please check the file path.")
    exit()  # Stop execution if image is missing

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
# cvtColor() converts image color spaces
# COLOR_BGR2GRAY converts a 3-channel BGR image to a single-channel grayscale image

# Resize the grayscale image to 224x224 pixels
resized_image = cv2.resize(gray_image, (224, 224))  
# resize() changes image size → (width, height)
# 224x224 is commonly used for machine learning models

# Display the resized grayscale image in a window
cv2.imshow('Processed Image', resized_image)  
# Opens a window titled "Processed Image" showing the processed image

# Wait for a key press indefinitely
key = cv2.waitKey(0)  
# waitKey(0) pauses the program until any key is pressed
# Returns ASCII value of the pressed key

# Check if the "s" key was pressed
if key == ord('s'):  
    # ord('s') converts character 's' into its ASCII value for comparison
    
    # Save the processed image if 's' is pressed
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)  
    # imwrite() saves the image to disk in the current directory
    
    print("Image saved as grayscale_resized_image.jpg")  # Confirmation message
else:
    print("Image not saved")  # If any other key is pressed

# Close all OpenCV windows
cv2.destroyAllWindows()  
# Ensures all GUI windows are properly closed

# Print the dimensions of the processed image
print(f"Processed Image Dimensions: {resized_image.shape}")  
# shape returns (height, width) for grayscale images
# Example output: (224, 224)