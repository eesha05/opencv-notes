"""median blur is clean the image using middle value of random pixels
it sorts the pixels and find the middle values and noise is replaced by median"""
#blurred = cv2.medianBlur(image, kernel_size)
import cv2
image=cv2.imread("parrot image.jpg")
blurred=cv2.medianBlur(image,3)
cv2.imshow("median blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()