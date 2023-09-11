# добавим необходимый пакет с opencv
import cv2
# присваиваем переменной image изображение из файла
# testfi le.jpg
image = cv2.imread("testfile.jpg")
# выводим изображение image на экран в окне Open
# image
cv2.imshow("Open image", image)
# ожидаем нажатия любой клавиши
cv2.waitKey(0)
