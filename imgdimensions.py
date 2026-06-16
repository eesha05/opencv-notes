import cv2
image=cv2.imread("parrot image.jpg")
if image is None:
    print("not successful")
else:
    print("successful")
"""to get the image dimensions use the .shape attribute, it give height width
and number of color channels of the image
if grayscale then third value is not shown"""
print(image.shape)
h, w, c = image. shape
print(f"Image Loaded: \nHeight: {h}\nWidth: {w}\nChannels: {c}")

"""to convert the image to grayscale, if image in grayscale the 
processing time and complexity reduces 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)"""
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("parrot image.jpg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()