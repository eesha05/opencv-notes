"""
image - a 2d grid of pixels or a matrix of numbers
pixels - coloured dots. smallest unit of image and holds data of a color
a pixel holds 3 colors if colored image - red,green,blue
width is total number of pixels horizontally
height is total number of pixels vertically
color channel- channel that store one part of the colored info for each pixel
eg grayscale has 1 and rgb has 3
[255,0,0] is pure red
[0,255,0] is pure green
[0,0,255] is pure blue
.jpg is small size file
.png is high quality image
.tiff is super high resolution
"""
import cv2

#to load an image in the memory use read function
#image = cv2.read("relative path of the image",flag) 
#flag=1 means color, 0 means grayscale and -1 means unchanged
image=cv2.imread("parrot image.jpg")#copy relative path of the image

#to show the loaded image
"""
cv2.imshow("Window Title", image) open the image in a window on screen
cv2.waitKey(0) so that window remains on screen 0 beacuse till no key on keyboard pressed window will remain open
cv2.destroyAllWindows() to close the window
"""
if image is not None:
    cv2.imshow("image showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not load the image")

#to save the image after change
#cv2.imwrite("output.jpg", image) output is name of edited file
if image is not None:
    success=cv2.imwrite("output.jpg",image)
    if success:
        print("image saved successfully")
    else:
        print("failed to save an image")
else:
    print("error could not save image")

