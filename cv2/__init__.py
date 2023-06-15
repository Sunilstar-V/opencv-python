import cv2

cap = cv2.VideoCapture(r"sequence.mp4")

if not cap.isOpened():
    print("Error opening video stream or file")

fps = cap.get(cv2.CAP_PROP_FPS)

print("Original FPS:", fps)

desired_fps = 5
cap.set(cv2.CAP_PROP_FPS, desired_fps)

updated_fps = cap.get(cv2.CAP_PROP_FPS)
print("Updated FPS:", updated_fps)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()