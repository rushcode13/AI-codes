# Import OpenCV for webcam access, image processing, and drawing on frames
import cv2

# Import DeepFace for emotion detection
from deepface import DeepFace

# Load OpenCV's pre-trained face detector
# This file helps OpenCV find faces in an image
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open the default webcam (0 = first webcam connected to the computer)
camera = cv2.VideoCapture(0)

# Keep running until the user presses 'q'
while True:

    # Read one frame (image) from the webcam
    success, frame = camera.read()

    # If no frame was captured, stop the program
    if not success:
        break

    # DeepFace works best with RGB images
    # OpenCV uses BGR format by default, so convert it
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert image to grayscale
    # Face detection is faster in grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray_frame,      # image to search
        scaleFactor=1.1, # how much the image size is reduced each scan
        minNeighbors=5,  # higher value = fewer false detections
        minSize=(30, 30) # smallest face size to detect
    )

    # loop through every detected face
    for (x, y, width, height) in faces:

        # Crop only the face area from the image
        face = rgb_frame[y:y + height, x:x + width]

        try:
            # ask DeepFace to analyze the face
            # We only want emotion detection
            result = DeepFace.analyze(
                face,
                actions=["emotion"],
                enforce_detection=False
            )

            # Get the emotion with the highest confidence
            emotion = result[0]["dominant_emotion"]

            # Draw a green rectangle around the face
            cv2.rectangle(
                frame,
                (x, y),                       # top-left corner
                (x + width, y + height),     # bottom-right corner
                (0, 255, 0),                 # green color
                2                            # line thickness
            )

            # Display the detected emotion above the face
            cv2.putText(
                frame,
                emotion,
                (x, y - 10),                 # position of text
                cv2.FONT_HERSHEY_SIMPLEX,    # font style
                0.9,                         # font size
                (0, 255, 0),                 # green color
                2                            # thickness
            )

        except Exception:
            # Skip this face if DeepFace cannot analyze it
            continue

    # Show the webcam feed with rectangles and emotion labels
    cv2.imshow("Real-time Emotion Detection", frame)

    # Wait 1 millisecond for a key press
    # If user presses 'q', exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam so other programs can use it
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()