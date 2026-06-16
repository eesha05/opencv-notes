import cv2
#resized = cv2.resize(src, dsize, fx, fy, interpolation)
"""src is the original image
dsize is the pixels of new dimension (width,height)
fx and fy are scale factors
"""
image=cv2.imread("parrot image.jpg")
if image is None:
    print("not successful")
else:
    print("successful")
    resized=cv2.resize(image,(300,300))
    cv2.imshow("original image",image)
    cv2.imshow("resized image",resized)
    cv2.imwrite("resizedimg.jpg",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()