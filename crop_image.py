# добавляем необходимый пакет с opencv
import cv2
# загружаем изображение
image = cv2.imread("testfile.jpg")
# вырежем фрагмент изображения, используя срезы
# y1:y2, x1:x2 (левый верхний угол имеет координаты [0][0)
crop = image[400:600, 400:600]
cv2.imshow("Crop image", crop)
# выводим изображение image на экран в окне Original
cv2.imshow("Original", image)
# ожидаем нажатия любой клавиши
cv2.waitKey(0)
