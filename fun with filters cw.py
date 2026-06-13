import cv2

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image"""
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    # Increase colors
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)

    elif filter_type == "increase_green":
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 50)

    elif filter_type == "increase_blue":
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50)

    # Decrease colors
    elif filter_type == "decrease_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], 50)

    elif filter_type == "decrease_green":
        filtered_image[:, :, 1] = cv2.subtract(filtered_image[:, :, 1], 50)

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image


# Load image
image_path = "pandaaaa.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")

else:
    filter_type = "original"

    print("Press the following keys to apply filters:")
    print("r - Red tint")
    print("g - Green tint")
    print("b - Blue tint")
    print("i - Increase Red")
    print("o - Increase Green")
    print("p - Increase Blue")
    print("e - Decrease Red")
    print("f - Decrease Green")
    print("d - Decrease Blue")
    print("n - Original Image")
    print("s - Save Current Image")
    print("q - Quit")

    while True:
        filtered_image = apply_color_filter(image, filter_type)

        # Display the filtered image
        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"

        elif key == ord('g'):
            filter_type = "green_tint"

        elif key == ord('b'):
            filter_type = "blue_tint"

        elif key == ord('i'):
            filter_type = "increase_red"

        elif key == ord('o'):
            filter_type = "increase_green"

        elif key == ord('p'):
            filter_type = "increase_blue"

        elif key == ord('e'):
            filter_type = "decrease_red"

        elif key == ord('f'):
            filter_type = "decrease_green"

        elif key == ord('d'):
            filter_type = "decrease_blue"

        elif key == ord('n'):
            filter_type = "original"

        elif key == ord('s'):
            # Save the currently displayed filtered image to a file

            # Create a filename using the current filter name
            # Example: red_tint.jpg or increase_green.jpg
            filename = filter_type + ".jpg"

            # Save the image to disk
            cv2.imwrite(filename, filtered_image)

            # Confirm that the image was saved
            print("Image saved as", filename)

        elif key == ord('q'):
            print("Exiting...")
            break

        else:
            print("Invalid key! Please press a valid key.")

cv2.destroyAllWindows()