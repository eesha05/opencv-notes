import cv2
"""
image filtering is change a pixel acc to near pixels so image change slightly
blurring is soften the image less sharp
noise is unwanted pixels or unwanted color dot
smoothing is making areas make sharp
kernel is 3*3 grid
"""
#gaussian blur to soften the image and remove sharpness,noise
#blurred_image = cv2.GaussianBlur(image, (kernel_size_x, kernel_size_y), sigma)
image=cv2.imread("parrot image.jpg")
blurred = cv2.GaussianBlur(image, (7,7), 3)
#kernel size is always odd (3,3)is light blur
#(9,9) is strong blur and (21,21) is super blur
#sigma is how strong the blur is
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
