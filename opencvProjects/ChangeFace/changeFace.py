import cv2

faceModel = cv2.CascadeClassifier("face.xml")
cap = cv2.VideoCapture(0) # Select the video source

while cap.isOpened():
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceModel.detectMultiScale(gray_frame, 1.1, 4)
    faceCounter = len(faces)
    cv2.putText(
        frame,
        "detected face : " + str(faceCounter),
        (30, 30),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (0, 0, 0),
        1,
    )
    if faceCounter == 2:
        x1, y1, w1, h1 = faces[0]
        x2, y2, w2, h2 = faces[1]

        firstFace = frame[y1 : y1 + h1, x1 : x1 + w1]
        secondFace = frame[y2 : y2 + h2, x2 : x2 + w2]

        firstFace = cv2.resize(firstFace, (w2, h2))
        secondFace = cv2.resize(secondFace, (w1, h1))

        frame[y1 : y1 + h1, x1 : x1 + w1] = secondFace
        frame[y2 : y2 + h2, x2 : x2 + w2] = firstFace
    cv2.imshow("Change Face", frame)
    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindows()
cap.release()