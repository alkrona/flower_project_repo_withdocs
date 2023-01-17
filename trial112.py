import cv2

# Load the Haar cascade classifier for detecting hand gestures
hand_cascade = cv2.CascadeClassifier('hand.xml')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hand gestures in the frame
    hands = hand_cascade.detectMultiScale(gray)

    # Loop over the detected hands
    for (x, y, w, h) in hands:
        # Draw a rectangle around the hand
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Check if the hand is making a thumbs up gesture
        if w > h and w > 75 and h > 75:
            # Draw a circle around the thumb
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            radius = int(w / 2)
            cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)
            cv2.putText(frame, "Thumbs Up", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
