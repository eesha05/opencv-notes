import cv2 
"""a video is a collection of images shown very fast
a frame is a photo which is a part of a video
frame by frame processing is when do one single task in all the frames one by one
"""
#cap = cv2.VideoCapture(source) to open the camera and to load the videofile so that we can start reading the frames
#source is 0 if webcam of computer else 1 if external camera
cap=cv2.VideoCapture(0)
while True:
    ret,frame= cap.read() #ret is return it gives true or false, false means no frame got
    #cap.read reads an image from the frame of the webcam
    #frame is the actual image captured
    if not ret:
        print("could not read frame")
        break
    cv2.imshow("webcam feed",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):#ord converts the value to ascii
        #0xFF returns the lowest 8 bits of the character
        #1 is passed to wait 1 milisecond
        #if q is pressed then exit the loop
        #waitkey returns -1 if no key pressed and the ascii code of the character if it is pressed
        print("quitting")
        break
cap.release()#to shut down the camera
cv2.destroyAllWindows()