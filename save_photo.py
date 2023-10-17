import cv2
image = cv2.imread("pic.jpg")
new_image = cv2.flip(image,1)
cv2.imshow("original", image)
cv2.imshow("Flip image", new_image)
cv2.imwrite("new.jpg", new_image)
cv2.waitKey(0)
