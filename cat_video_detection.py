import cv2 

cap = cv2.VideoCapture('cat.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame,(420,400))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    rects = detector.detectMultiScale(gray, scaleFactor=1.15,
                                      minNeighbors=2, minSize=(40,40))
    # draw rectangle cropping cat face
    if rects != ():
        for (i, (x, y, w, h)) in enumerate(rects):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Cat #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    else :  cv2.putText(frame, "Cat not found", (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    cv2.imshow("Cat Faces", frame)
    k = cv2.waitKey(1)
    if  k%256 == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
    

