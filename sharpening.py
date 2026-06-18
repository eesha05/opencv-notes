import cv2
import numpy as np
image=cv2.imread("parrot image.jpg")
#cv2.filter2D(src, ddepth, kernel)
#kernal is 3*3 matrix that moves to each pixel and performs maths on each
sharpen_kernel = np.array([
[ 0, -1, 0],
[-1, 5, -1],#central pixel is boosted 5 times and neighbouring is lessened by -1 and rest are unchanged
[ 0, -1, 0]])
sharpened=cv2.filter2D(image, -1, sharpen_kernel)
cv2.imshow("sharpen image",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()