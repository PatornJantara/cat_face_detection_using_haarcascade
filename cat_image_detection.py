import cv2 
import os

path = os.getcwd()
path = path +'/image'
file = os.listdir(path)
for name in file :
    print(name)
    image = cv2.imread(path+'/'+name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    rects = detector.detectMultiScale(gray, scaleFactor=1.15,
                                      minNeighbors=4, minSize=(40,40))
    # draw rectangle cropping cat face
    if rects != ():
        for (i, (x, y, w, h)) in enumerate(rects):
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    else :  cv2.putText(image, "Cat not found", (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    cv2.imshow("Cat Faces", image)
    if cv2.waitKey() == 32 : # press spacebar to step to next picture
        print ( "The location of cat  = {} ".format(rects))
        continue 
    else : break
    
    

